import re
from datetime import datetime
from pathlib import Path
import os
import requests
from slack_sdk import WebClient
from typing import Callable
import time
from PySide6.QtCore import Signal, QObject

from app.model.html_presets.airium_message_gen import message_generator
from app.model.static_globals import (PRIVATE_TOKEN, USER_NAME, USER_ID, TEAM_NAME,
                                      FAILED, INTERRUPTED, COMPLETE, STARTED, TIMEOUT, NO_CONNECTION,
                                      SKIPPED_FILES,
                                      PUBLIC_CHANNEL, PRIVATE_CHANNEL, DIRECT_CHAT,
                                      AUTH_FAILED, DATA_LOAD_FAILED)
from app.model.decorators import singleton, run_in_new_thread, handle_exception, restart_functon_on_fail
from app.view.html_templates import HEAD, BODY_OPEN, BODY_CLOSE, CHAT_NAME, SEPARATOR, INTERRUPTED_TAG
from app.model.config_loader import Config
from app.service.logger import logger
from app.service.auth.test_ping import test_ping


@singleton
class Parser(QObject):
    slack_connection_status = Signal(object)
    backup_local_status = Signal(object)
    backup_result = Signal(str)

    def __init__(self):
        super().__init__()
        self.logger = logger
        self.config = Config()
        self.client = WebClient()
        self.auth_complete = False

        self.__main_path = Path(f'Backups')

        self.__private_channels_path = self.__main_path / Path('private channels')
        self.__public_channels_path = self.__main_path / Path('public channels')
        self.__direct_chats_path = self.__main_path / Path('direct chats')

        self.__chat_dir_path = None
        self.__attachments_dir = None
        self.__attachments_dir_path = None
        self.__html_path = None

        self.users = None
        self.private_channels = None
        self.public_channels = None
        self.direct_channels = None
        self.files = {}
        self.auth_test_data = None

        self.__terminate_backup = False
        self.__backup_is_running = False
        self.reply_amount = 0

    @run_in_new_thread
    def connect_to_slack(self) -> str:
        self.auth_complete = False

        self.client = WebClient(self.config.get_user(PRIVATE_TOKEN))

        if self.__auth_test() is FAILED:
            self.slack_connection_status.emit(AUTH_FAILED)
            self.logger.error(f'Failed to auth by token')
            return FAILED
        self.logger.info(f'API connected. {PRIVATE_TOKEN} is valid')

        if self.__request_team_info() is FAILED:
            self.slack_connection_status.emit(DATA_LOAD_FAILED)
            self.logger.error(f'Failed to load team data')
            return FAILED

        self.logger.info(f'Team data is loaded')

        self.slack_connection_status.emit(COMPLETE)
        self.auth_complete = True
        return COMPLETE

    @handle_exception
    def __auth_test(self) -> str:
        self.auth_test_data = self.client.auth_test()
        return COMPLETE

    @handle_exception
    def __request_team_info(self) -> str:
        self.users = self.__request_user_names()
        if self.users in [None, FAILED]:
            return FAILED
        self.private_channels = self.__request_conversations_list(chat_type=PRIVATE_CHANNEL)
        self.public_channels = self.__request_conversations_list(chat_type=PUBLIC_CHANNEL)
        self.direct_channels = self.__request_conversations_list(chat_type=DIRECT_CHAT)
        if FAILED in [self.private_channels, self.public_channels, self.direct_channels]:
            return FAILED
        self.config.update_user(USER_ID, self.auth_test_data['user_id'])
        self.config.update_user(TEAM_NAME, self.auth_test_data['team'])
        self.config.update_user(USER_NAME, self.users[self.auth_test_data['user_id']])
        self.auth_test_data = None
        return COMPLETE

    @restart_functon_on_fail
    def __request_user_names(self) -> dict:
        response = self.client.users_list()
        users = {}
        for chunk in response:
            for user in chunk['members']:
                if user['is_bot']:
                    users[user['profile'].get('api_app_id')] = user['profile']['real_name']
                else:
                    users[user['id']] = user['profile']['real_name']
        return users

    @restart_functon_on_fail
    def __request_conversations_list(self, chat_type: str) -> dict:
        response = self.client.conversations_list(types=chat_type)
        channels = {}
        for chunk in response:
            for channel in chunk['channels']:
                channels[channel['id']] = self.users.get(channel['user'],
                                                         channel['id']) if chat_type is DIRECT_CHAT else channel['name']
        return channels

    @restart_functon_on_fail
    def __request_conversations_history(self, chat_id: str) -> list[dict]:
        response = self.client.conversations_history(channel=chat_id)
        chat_list = []
        for chunk in response:
            if self.__terminate_backup:
                return INTERRUPTED
            for message in chunk['messages']:
                chat_list.append(self.__extract_one_message(message))
        return chat_list

    @handle_exception
    def __download_files(self, meta: dict) -> str:
        chat_id, chat_name = meta['chat_id'], meta['chat_name']

        files = self.files.copy()
        for i, file in enumerate(files.items(), 1):
            if self.__terminate_backup:
                return INTERRUPTED
            self.__emit_backup_local_status(meta, f'downloading files: {i}/{len(self.files)}')
            if self.__request_and_write_file(file[1]['url'], file[0]) is TIMEOUT:
                return TIMEOUT

        self.logger.info(f"Finished downloading attachments for [{chat_name}]-[{chat_id}]")
        return COMPLETE

    def __request_and_write_file(self, url: str, file_name: str) -> str:
        try:
            response = requests.get(url,
                                    timeout=5,
                                    headers={"Authorization": f"Bearer {self.config.get_user(PRIVATE_TOKEN)}"})
        except requests.exceptions.ReadTimeout as error:
            self.logger.warning(f'Failed to write [{file_name}]. Traceback: {error}')
            return TIMEOUT

        try:
            file_path = self.__attachments_dir_path / file_name
            with open(file_path, 'wb') as f:
                f.write(response.content)
            return COMPLETE

        except Exception as error:
            file_path = self.__chat_dir_path / SKIPPED_FILES
            with open(file_path, 'a') as f:
                f.write(f'{file_name}   ---   {url}\n')
            self.logger.warning(f'Failed to write [{file_name}]. Skip. Traceback: {error}')
            return FAILED

    @restart_functon_on_fail
    def __request_replies(self, chat_id: str, ts: str) -> list[dict]:
        response = self.client.conversations_replies(channel=chat_id, ts=ts)
        replies = []
        for chunk in response:
            for message in chunk['messages']:
                if message['thread_ts'] != message['ts']:
                    replies.append(self.__parse_one_message(message))
        return replies

    @staticmethod
    def __extract_one_message(message: dict) -> dict:
        return {'user': message.get('user'),
                'text': message.get('text'),
                'app_id': message.get('app_id'),
                'ts': message.get('ts'),
                'files': message.get('files'),
                'thread_ts': message.get('thread_ts')
                }

    def __prepare_text(self, text: str) -> str:
        def __replace_tagged_id(tagged_uid):
            user_id = tagged_uid.group(1)
            if user_id in self.users:
                return f'[@{self.users[user_id]}]'
            else:
                return tagged_uid.group(0)

        def __replace_tagged_chat_id(tagged_cid):
            chat_id = tagged_cid.group(1)
            if chat_id in self.private_channels:
                return f'[@{self.private_channels[chat_id]}]'
            elif chat_id in self.public_channels:
                return f'[@{self.public_channels[chat_id]}]'
            else:
                return tagged_cid.group(0)

        def __replace_urls(bordered_url):
            url = bordered_url.group(1).split('|')[0]
            return f'<a href="{url}">{url}</a>'

        def __replace_line_brake(message):
            return message.replace('\n', '<br>')

        convert_uid = re.sub(r'<@(.*?)>', __replace_tagged_id, text)
        convert_cid = re.sub(r'<#(.*?)\|>', __replace_tagged_chat_id, convert_uid)
        convert_links = re.sub(r'<(.*?)>', __replace_urls, convert_cid)

        return __replace_line_brake(convert_links)

    def __parse_one_message(self, message: dict) -> dict:
        user_name = self.users.get(message.get('user'))
        if not user_name:
            user_name = self.users.get(message.get('app_id'))
            if not user_name:
                user_name = 'UNKNOWN'

        files_names_paths = []
        if message.get('files'):
            for file in message.get('files'):
                url = file.get('url_private')
                if url:
                    files_names_paths.append(self.unify_file_name(url))

        message['user'] = user_name
        message['text'] = self.__prepare_text(message['text'])
        message['human_ts'] = datetime.fromtimestamp(float(message.get('ts'))).strftime('%d %B %Y, %H:%M')
        message['file_names_paths'] = files_names_paths
        return message

    def unify_file_name(self, file_url: str) -> dict:
        """
        return {'filename': {'url': str()-(slack file url),
                             'local_path': Path()-(file local storage path),
                             'count': int()-(amount of files with the same old name (needed to calculate index))}}
        """
        file_name = file_url.split('/')[-1]

        if not self.files.get(file_name):
            new_file_name = file_name
        else:
            name, extension = os.path.splitext(file_name)
            new_file_name = f"{name}_{self.files[file_name]['count']}{extension}"
            self.files[file_name]['count'] += 1

        local_path = self.__attachments_dir / new_file_name
        self.files[new_file_name] = {'url': file_url, 'local_path': local_path, 'count': 1}
        return {'name': new_file_name, 'path': local_path}

    @handle_exception
    def __write_html(self, meta: dict) -> str:
        chat_id, chat_name = meta['chat_id'], meta['chat_name']

        self.__emit_backup_local_status(meta, 'fetching data')
        messages_list = self.__request_conversations_history(chat_id)
        if messages_list is INTERRUPTED:
            return INTERRUPTED
        self.logger.info(f'Fetched {len(messages_list)} messages')

        with open(self.__html_path, 'wb') as f:
            f.write(bytes(HEAD, encoding='utf8'))
            f.write(bytes(BODY_OPEN, encoding='utf8'))
            f.write(bytes(CHAT_NAME.format(chat_name), encoding='utf8'))
            f.write(bytes(SEPARATOR, encoding='utf8'))

            for i, message in enumerate(messages_list, 1):
                self.__emit_backup_local_status(meta, f'downloading messages: {i}/{len(messages_list)}')

                if not message.get('thread_ts'):
                    msg = self.__parse_one_message(message)
                    msg_html = message_generator(user_name=msg['user'], date=msg['human_ts'],
                                                 message_text=msg['text'], attachments_list=msg['file_names_paths'])
                    f.write(bytes(msg_html))
                else:
                    if message['thread_ts'] == message['ts']:
                        msg = self.__parse_one_message(message)
                        replies = self.__request_replies(chat_id, message['ts'])
                        msg_html = message_generator(user_name=msg['user'], date=msg['human_ts'],
                                                     message_text=msg['text'], replies_list=replies,
                                                     attachments_list=msg['file_names_paths'])
                        f.write(bytes(msg_html))

                if self.__terminate_backup:
                    f.write(bytes(INTERRUPTED_TAG, encoding='utf8'))
                    f.write(bytes(BODY_CLOSE, encoding='utf8'))
                    return INTERRUPTED

            f.write(bytes(BODY_CLOSE, encoding='utf8'))
        self.logger.info(f"Finished writing html-file for [{chat_name}]-[{chat_id}]")
        return COMPLETE

    # @handle_exception
    def __create_directory_for_chat(self, meta: dict) -> str:
        chat_id, chat_name, chat_type = meta['chat_id'], meta['chat_name'], meta['chat_type']
        chat_type_path = str()
        if chat_type is PRIVATE_CHANNEL:
            chat_type_path = self.__private_channels_path
        elif chat_type is PUBLIC_CHANNEL:
            chat_type_path = self.__public_channels_path
        elif chat_type is DIRECT_CHAT:
            chat_type_path = self.__direct_chats_path

        self.__chat_dir_path = chat_type_path / Path(f'{chat_name}')
        self.__chat_dir_path.mkdir(exist_ok=True, parents=True)

        self.__attachments_dir = Path(f'attachments')
        self.__attachments_dir_path = self.__chat_dir_path / self.__attachments_dir
        self.__attachments_dir_path.mkdir(exist_ok=True)

        self.__html_path = self.__chat_dir_path / f'{chat_name}.html'
        self.logger.info(f"Created directory for [{chat_name}]-[{chat_id}]")
        return COMPLETE

    def terminate_backup(self) -> None:
        if not self.__terminate_backup and self.__backup_is_running:
            self.__terminate_backup = True
            self.logger.warning(f"Backup terminated")

    def __emit_backup_local_status(self, meta: dict, text: str) -> None:
        self.backup_local_status.emit((meta, text))
        self.logger.debug(f"Chat [{meta['chat_name']}]-[{meta['chat_id']}]. {text}")

    def __emit_backup_result(self, result) -> None:
        self.logger.info(f'Backup - {result}')
        self.backup_result.emit(result)

    def __result_handler(self, func: Callable[[dict], str], meta: dict) -> bool:
        if self.__terminate_backup:
            self.__emit_backup_local_status(meta, INTERRUPTED)
            self.backup_result.emit(INTERRUPTED)
            return False

        result = func(meta)

        if result == COMPLETE:
            return True
        elif result == INTERRUPTED:
            self.__emit_backup_local_status(meta, INTERRUPTED)
            self.backup_result.emit(INTERRUPTED)
            return False
        elif result == FAILED:
            self.__emit_backup_local_status(meta, FAILED)
            self.backup_result.emit(FAILED)
            return False
        elif result == TIMEOUT:
            self.__emit_backup_local_status(meta, TIMEOUT)
            self.backup_result.emit(TIMEOUT)
            return False

    def rate_limit_defender(self, sec_to_wait: int) -> None:
        self.logger.info(f'Ratelimit defender started for {sec_to_wait} seconds')
        start = datetime.now()

        while (datetime.now() - start).seconds < sec_to_wait:
            if self.__terminate_backup:
                return
            time.sleep(1)
        self.logger.info('Ratelimit defender finished')

    def calculate_time_execution(self, start_time: datetime) -> None:
        self.__backup_is_running = False
        self.logger.info(
            f"Finished in {datetime.now() - start_time}")

    @run_in_new_thread
    def run_yummy_parser(self, chats: dict) -> None:
        self.__backup_is_running = True
        backup_start_time = datetime.now()

        if not test_ping():
            self.__emit_backup_result(NO_CONNECTION)
            return self.calculate_time_execution(backup_start_time)

        self.__terminate_backup = False
        self.__main_path.mkdir(exist_ok=True)

        self.__emit_backup_result(STARTED)

        for chat_id, meta in chats.items():
            backup_start_time = datetime.now()
            self.files.clear()

            if self.__terminate_backup:
                return self.calculate_time_execution(backup_start_time)

            self.logger.info(f"Current chat for backup: [{meta['chat_name']}]-[{meta['chat_id']}]")

            if not self.__result_handler(self.__create_directory_for_chat, meta):
                return self.calculate_time_execution(backup_start_time)

            if not self.__result_handler(self.__write_html, meta):
                return self.calculate_time_execution(backup_start_time)

            if not self.__result_handler(self.__download_files, meta):
                return self.calculate_time_execution(backup_start_time)

            self.__emit_backup_local_status(meta, COMPLETE)

        self.__emit_backup_result(COMPLETE)

        return self.calculate_time_execution(backup_start_time)


if __name__ == '__main__':
    pass
