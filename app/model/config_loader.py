import os
from pathlib import Path
from app.model.decorators import singleton
import json
from app.model.static_globals import (USER_CACHE_FILE, USER_CACHE_PATH, APP_CONFIG_FILE, APP_CONFIG_PATH,
                                      CLIENT_ID, CLIENT_SECRET, SIGNING_SECRET, AUTH_URL, FILE_VALIDATION,
                                      USER_CACHE_FILE_TEMPLATE, APP_CONFIG_FILE_TEMPLATE, COMPLETE)
from app.service.logger import logger


@singleton
class Config:

    def __init__(self):
        self.logger = logger
        self.__user_cache = {}
        self.__app_config = {}
        self.user_config_is_valid: bool = False
        self.app_config_is_valid: bool = False
        self.start_setup()

    def start_setup(self) -> None:
        self.user_config_is_valid: bool = self.__load_user_cache(Path(USER_CACHE_PATH) / USER_CACHE_FILE)
        self.app_config_is_valid: bool = self.__load_app_config(Path(APP_CONFIG_PATH) / APP_CONFIG_FILE)

    def __load_app_config(self, file_path: Path) -> bool:
        temp_file = self.__open_file(file_path)

        if not self.__verify_app_auth_file(temp_file):
            self.logger.warning(f'Invalid [{file_path}]! Manual [{file_path}] update needed')
            self.write_app_config_template()
            return False
        self.__app_config = temp_file
        self.logger.info(f'Successfully loaded [{file_path}]')
        return True

    def __load_user_cache(self, file_path: Path) -> bool:
        temp_file = self.__open_file(file_path)

        if not self.__verify_user_cache_file(temp_file):
            self.logger.warning(f'Invalid [{file_path}]! Authorisation needed')
            return False
        self.__user_cache = temp_file

        self.logger.info(f'Successfully loaded [{file_path}]')
        return True

    def __open_file(self, file_path: Path) -> dict:
        if not self.__file_exists(file_path):
            self.logger.warning(f"Didn't find [{file_path}] or file is empty")
        else:
            try:
                with open(file_path) as f:
                    temp_file = json.load(f)
                return temp_file
            except Exception as error:
                self.logger.error(f"Failed to load [{file_path}]. Traceback: {error}")
        return {}

    @staticmethod
    def __file_exists(path: Path) -> bool:
        return bool(os.path.exists(path) and os.stat(path).st_size != 0)

    @staticmethod
    def __verify_user_cache_file(cache: dict) -> bool:
        return all(key in cache for key in USER_CACHE_FILE_TEMPLATE.keys())

    @staticmethod
    def __verify_app_auth_file(conf: dict) -> bool:
        return bool(conf.get(CLIENT_ID)
                    and conf.get(CLIENT_SECRET)
                    and conf.get(SIGNING_SECRET)
                    and conf.get(AUTH_URL)
                    and conf.get(FILE_VALIDATION) == COMPLETE)

    def write_app_config_template(self) -> None:
        path = Path(APP_CONFIG_PATH)
        path.mkdir(exist_ok=True, parents=True)

        with open(path / APP_CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(APP_CONFIG_FILE_TEMPLATE, f, ensure_ascii=False, indent=4)
            self.logger.info(f"Successfully created [{APP_CONFIG_FILE}] template.")

    def overwrite_user_cache_file(self) -> None:
        path = Path(USER_CACHE_PATH)
        path.mkdir(exist_ok=True, parents=True)

        with open(path / USER_CACHE_FILE, 'w', encoding='utf-8') as f:
            if not self.__verify_user_cache_file(self.__user_cache):
                self.delete_user_config()
            json.dump(self.__user_cache, f, ensure_ascii=False, indent=4)
        self.logger.info(f"Successfully updated [{USER_CACHE_FILE}]")

    def update_user(self, field_name, field_value=str()) -> None:
        self.__user_cache[field_name] = field_value

    def delete_user_config(self) -> None:
        self.__user_cache = USER_CACHE_FILE_TEMPLATE.copy()

    def get_user(self, field_name: str) -> str:
        return self.__user_cache.get(field_name)

    def get_app(self, field_name: str) -> str:
        return self.__app_config.get(field_name)
