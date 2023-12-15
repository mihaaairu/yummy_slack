import threading
from typing import Tuple

from PySide6.QtWidgets import (QMainWindow,
                               QFrame,
                               QHBoxLayout,
                               QCheckBox,
                               QSizePolicy,
                               QLabel,
                               QApplication,
                               QPushButton)
from PySide6.QtCore import QSize, Qt, QTimer
from PySide6.QtGui import QKeyEvent, QCloseEvent

from app.view.main_window_ui import Ui_MainWindow
from app.service.auth.flask_server import AuthServer
from app.controller.mesage_box_controller import MessageBox
from app.model.static_globals import (PRIVATE_TOKEN, USER_ID, USER_NAME, TEAM_NAME,
                                      MSG_INFO, MSG_WARNING,
                                      COMPLETE, FAILED, INTERRUPTED, STARTED, TIMEOUT, NO_CONNECTION,
                                      AUTH_FAILED, DATA_LOAD_FAILED,
                                      PRIVATE_CHANNEL, PUBLIC_CHANNEL, DIRECT_CHAT, APP_CONFIG_FILE, APP_CONFIG_PATH)
from app.model.config_loader import Config
from app.service.chat_parser import Parser
from app.service.auth.test_ping import test_ping
from app.service.logger import logger


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.logger = logger
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.set_team_info(auth_success=False)

        self.config = Config()
        self.parser = Parser()
        self.server_instances = []
        self.chats_boxes = {}

        self.start_flow()
        self.ui.log_out_pushButton.clicked.connect(self.log_out)
        self.ui.backup_pushButton.clicked.connect(self.start_backup)
        self.ui.search_lineEdit.textChanged.connect(self.search)
        self.parser.slack_connection_status.connect(self.slack_connection_result)
        self.parser.backup_local_status.connect(self.update_chat_backup_status)
        self.parser.backup_result.connect(self.backup_result)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Return:
            if QApplication.keyboardModifiers() == Qt.ShiftModifier:
                self.logger.debug(f'[MANUAL EXEC] Alive threads amount: {threading.active_count()}.  '
                                  f'Enumerate: {threading.enumerate()}')

                msg = f'Active threads amount: {threading.active_count()}\n\n'
                for thread in threading.enumerate():
                    msg += f'{thread}\n'
                MessageBox(msg, MSG_INFO, show_button=False)
                event.accept()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.stop_flask_servers()
        for window in QApplication.topLevelWidgets():
            window.close()
        self.config.overwrite_user_cache_file()
        self.stop_backup()
        self.logger.debug(f'Alive threads count: {threading.active_count()}. {threading.enumerate()}')

    def start_flow(self) -> None:
        self.info_page(show=True, label_text='Loading...')
        if not self.config.app_config_is_valid:
            self.info_page(show=True, button_text='Retry',
                           label_text=f'Update the [{APP_CONFIG_PATH}/{APP_CONFIG_FILE}] file '
                                      f'\naccording to the instructions in it and press Retry',
                           func_to_connect=self.restart_config_load)
            return
        if not test_ping():
            self.info_page(show=True, button_text='Retry',
                           label_text='No internet connection.', func_to_connect=self.start_flow)
            return
        if not self.config.get_user(PRIVATE_TOKEN):
            self.info_page(show=True, button_text='Authorise in Slack', func_to_connect=self.authorise)
            return
        self.parser.connect_to_slack()

    def restart_config_load(self) -> None:
        self.config.start_setup()
        self.start_flow()

    def log_out(self) -> None:
        self.info_page(show=True, button_text='Authorise in Slack', func_to_connect=self.authorise)
        self.config.delete_user_config()

    def slack_connection_result(self, status: str) -> None:
        if status is AUTH_FAILED:
            self.info_page(show=True, button_text='Authorise in Slack',
                           label_text='Failed to authorise with saved private token.', func_to_connect=self.authorise)
        elif status is DATA_LOAD_FAILED:
            self.info_page(show=True, button_text='Retry', label_text='Failed to load team information.',
                           func_to_connect=self.start_flow)

        else:
            self.load_chats_list()
            self.config.update_user(USER_NAME, self.parser.users[self.config.get_user(USER_ID)])
            self.set_team_info(auth_success=True, user_name=self.config.get_user(USER_NAME),
                               team_name=self.config.get_user(TEAM_NAME))
            self.info_page(show=False)

    def authorise(self) -> None:
        if not test_ping():
            self.info_page(show=True, button_text='Retry', label_text='No internet connection.',
                           func_to_connect=self.start_flow)
            return
        self.reconnect_button(self.ui.auth_pushButton, None)
        self.stop_flask_servers()
        flask_auth_server = AuthServer()
        self.server_instances.append(flask_auth_server)
        flask_auth_server.start()
        flask_auth_server.auth_server_received.connect(self.on_flask_server_close)
        QTimer.singleShot(3000, lambda: self.reconnect_button(self.ui.auth_pushButton, self.authorise))

    def on_flask_server_close(self, response: None | dict) -> None:
        self.stop_flask_servers()
        if response:
            self.info_page(show=True, label_text='Loading...')
            self.logger.debug(f"Flask-listener server result: {response['ok']}")
            self.parser.connect_to_slack()

    def stop_flask_servers(self) -> None:
        self.logger.debug(f'Closing {len(self.server_instances)} servers')
        for server in self.server_instances:
            server.stop_server()
        self.server_instances.clear()

    def info_page(self, show: bool, button_text: str = None, label_text: str = None, func_to_connect=None) -> None:
        if show:
            if button_text:
                self.ui.auth_pushButton.show()
                self.ui.auth_pushButton.setText(button_text)
            else:
                self.ui.auth_pushButton.hide()
            if not label_text:
                self.ui.info_label.setVisible(False)
            else:
                self.ui.info_label.setVisible(True)
                self.ui.info_label.setText(label_text)
            if func_to_connect:
                self.reconnect_button(self.ui.auth_pushButton, func_to_connect)
        self.ui.main_work_frame.setVisible(not show)
        self.ui.info_frame.setVisible(show)

    def set_team_info(self, auth_success: bool = False, user_name: str = '', team_name: str = '') -> None:
        self.ui.user_name_label.setVisible(auth_success)
        self.ui.workspace_name_label.setVisible(auth_success)
        if auth_success:
            self.ui.user_name_label.setText(user_name)
            self.ui.workspace_name_label.setText(team_name)

    def reconnect_button(self, button: QPushButton, func_to_connect=None, *args) -> None:
        try:
            button.clicked.disconnect()
            self.logger.debug(f"[{button.objectName()}] has been disconnected")
        except Exception as error:
            self.logger.debug(f'Reconnect button exception: {error}')
            pass
        if func_to_connect:
            button.clicked.connect(lambda: func_to_connect(*args))
            self.logger.debug(f"[{button.objectName()}] connected to [{func_to_connect.__name__}]")

    def load_chats_list(self) -> None:
        for chat_id, meta in self.chats_boxes.items():
            meta['frame'].deleteLater()
        self.chats_boxes.clear()

        for chat_id, chat_name in self.parser.public_channels.items():
            self.chats_boxes.update(self.__add_single_chat_box(parent=self.ui.public_chats_frame,
                                                               chat_id=chat_id,
                                                               chat_name=chat_name,
                                                               chat_type=PUBLIC_CHANNEL))

        for chat_id, chat_name in self.parser.private_channels.items():
            self.chats_boxes.update(self.__add_single_chat_box(parent=self.ui.private_chats_frame,
                                                               chat_id=chat_id,
                                                               chat_name=chat_name,
                                                               chat_type=PRIVATE_CHANNEL))

        for chat_id, chat_name in self.parser.direct_channels.items():
            self.chats_boxes.update(self.__add_single_chat_box(parent=self.ui.direct_chats_frame,
                                                               chat_id=chat_id,
                                                               chat_name=chat_name,
                                                               chat_type=DIRECT_CHAT))

    def backup_result(self, result: str) -> None:
        if result == STARTED:
            MessageBox(f'Backup {STARTED}', MSG_INFO)
        elif result == COMPLETE:
            self.stop_backup()
            MessageBox(f'Backup {COMPLETE}.', MSG_INFO)
        elif result == INTERRUPTED:
            MessageBox(f'Backup {INTERRUPTED}.', MSG_INFO)
        elif result == FAILED:
            self.stop_backup()
            MessageBox(f'A critical error occurred during copying.\nBackup {FAILED}', MSG_WARNING)
        elif result == TIMEOUT:
            self.stop_backup()
            MessageBox(f'Established connection is not stable.\nBackup stopped because of {TIMEOUT}.', MSG_WARNING)
        elif result == NO_CONNECTION:
            self.stop_backup()
            MessageBox(f'No internet connection.', MSG_WARNING)

    @staticmethod
    def update_chat_backup_status(status_data: Tuple[dict, str]) -> None:
        meta, message = status_data

        meta['label'].setText(message)
        if not meta['inner_frame'].isVisible():
            meta['inner_frame'].show()

    def enable_tab_content(self, enable: bool) -> None:
        self.ui.private_chats_frame.setEnabled(enable)
        self.ui.public_chats_frame.setEnabled(enable)
        self.ui.direct_chats_frame.setEnabled(enable)

    def start_backup(self) -> None:
        self.reconnect_button(self.ui.backup_pushButton, self.stop_backup)
        self.ui.log_out_pushButton.setEnabled(False)
        self.enable_tab_content(False)
        for chat_id, meta in self.chats_boxes.items():
            meta['inner_frame'].hide()

        self.ui.backup_pushButton.setText('Stop Backup')

        backup_chats = {chat_id: meta for chat_id, meta in self.chats_boxes.items() if meta['check_box'].isChecked()}

        self.parser.run_yummy_parser(backup_chats)

    def stop_backup(self) -> None:
        self.reconnect_button(self.ui.backup_pushButton, None)
        self.ui.log_out_pushButton.setEnabled(True)
        self.ui.backup_pushButton.setText('Start Backup')
        self.enable_tab_content(True)
        self.parser.terminate_backup()
        QTimer.singleShot(3000, lambda: self.reconnect_button(self.ui.backup_pushButton, self.start_backup))

    @staticmethod
    def separator_line(parent: QFrame, style_sheet: str, max_width: int = 16777215, min_width: int = 0) -> QFrame:
        size_policy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        line = QFrame(parent)
        line.setMinimumSize(QSize(min_width, 1))
        line.setMaximumSize(QSize(max_width, 1))
        line.setStyleSheet(style_sheet)
        line.setSizePolicy(size_policy)
        return line

    def __add_single_chat_box(self, parent: QFrame, chat_id: str, chat_name: str, chat_type: str) -> dict:
        frame = QFrame(parent)
        h_layout = QHBoxLayout(frame)
        h_layout.setSpacing(10)
        h_layout.setContentsMargins(0, 0, 10, 0)

        check_box = QCheckBox(frame)
        h_layout.addWidget(check_box)

        inner_frame = QFrame(frame)
        h_layout.addWidget(inner_frame)

        inner_layout = QHBoxLayout(inner_frame)
        inner_layout.setSpacing(10)
        inner_layout.setContentsMargins(0, 0, 0, 0)

        inner_layout.addWidget(self.separator_line(frame, 'border: 1px dashed #693af5;'))

        label = QLabel(frame)
        inner_layout.addWidget(label)

        # inner_layout.addWidget(self.separator_line(frame, 'border: 1px dashed #693af5;'))

        label.setText('')
        check_box.setText(chat_name)
        check_box.setObjectName(chat_id)
        label.setObjectName(chat_id)

        inner_frame.hide()
        parent.layout().addWidget(frame)

        chat_meta = {'inner_frame': inner_frame,
                     'frame': frame,
                     'label': label,
                     'check_box': check_box,
                     'chat_id': chat_id,
                     'chat_name': chat_name,
                     'chat_type': chat_type}
        return {chat_id: chat_meta}

    def search(self) -> None:
        for name, meta in self.chats_boxes.items():
            if self.ui.search_lineEdit.text() and self.ui.search_lineEdit.text() not in meta['chat_name']:
                meta['frame'].hide()
            else:
                meta['frame'].show()
