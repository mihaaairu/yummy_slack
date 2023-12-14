import sys


from PySide6.QtWidgets import QApplication
from app.controller.main_window_controller import MainWindow
from app.model.config_loader import Config
from app.service.chat_parser import Parser


if __name__ == '__main__':
    # TODO: Refactor internet errors notifications.

    config = Config()

    parser = Parser()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

