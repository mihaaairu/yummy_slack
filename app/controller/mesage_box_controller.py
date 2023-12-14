from PySide6.QtWidgets import QMessageBox, QLabel, QDialogButtonBox, QApplication, QPushButton
from PySide6.QtCore import Qt
from typing import Callable

from app.resources.additional_stylesheets import push_button_style, q_message_box_stylesheet_ss
from app.model.static_globals import MSG_WARNING, MSG_INFO


class MessageBox(QMessageBox):
    def __init__(self, text: str,  msg_type: str, button_text: str = 'Ok', parent=None, show_button: bool = True):
        super().__init__(parent)
        self.setStyleSheet(q_message_box_stylesheet_ss)
        if msg_type == MSG_WARNING:
            self.setIcon(QMessageBox.Warning)
            self.setWindowTitle('Warning !')
        elif msg_type == MSG_INFO:
            self.setIcon(QMessageBox.Information)
            self.setWindowTitle('Info')

        self.setText(text)
        self.layout().update()

        grid_layout = self.layout()

        icon = self.findChild(QLabel, "qt_msgboxex_icon_label")
        grid_layout.removeWidget(icon)
        grid_layout.addWidget(icon, 0, 0, alignment=Qt.AlignCenter)

        label = self.findChild(QLabel, "qt_msgbox_label")
        grid_layout.removeWidget(label)
        grid_layout.addWidget(label, 0, 1, alignment=Qt.AlignCenter)

        grid_layout.removeWidget(self.findChild(QDialogButtonBox, "qt_msgbox_buttonbox"))
        if show_button:
            button = QPushButton(button_text)
            button.pressed.connect(self.close)
            grid_layout.addWidget(button, 1, 0, 1, 2, alignment=Qt.AlignCenter)
            button.setStyleSheet(push_button_style)
        self.exec_()
