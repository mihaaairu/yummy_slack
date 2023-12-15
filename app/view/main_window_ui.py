# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTabWidget, QVBoxLayout,
    QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(550, 650)
        MainWindow.setMinimumSize(QSize(550, 650))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/candy.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"\n"
"*{\n"
"	margin: 0px;\n"
"	padding: 0px;\n"
"	background: transparent;\n"
"	color: #693af5;\n"
"	border: none;\n"
"	font-family:'Segoe UI'; \n"
"	font-size: 14px;\n"
"}\n"
"/*414043*/\n"
"\n"
"#centralwidget{\n"
"	background: #ecedef;\n"
"}\n"
"\n"
"\n"
"\n"
"/* ======= TEMP ======= */\n"
"#label {\n"
"	border-radius: 6px;\n"
"	background: #f1effc;\n"
"	padding: 5px;\n"
"}\n"
"#line_4, #line_5 {\n"
"	border: 1px dashed #693af5;\n"
"}\n"
"\n"
"\n"
"\n"
"/* ======= QPushButton ======= */\n"
"QPushButton{\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"	background: #906ef7;\n"
"	color: #fbfbfb;\n"
"	border-radius: 16px;\n"
"	padding: 13px;\n"
"	padding-top: 7px;\n"
"	padding-bottom: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: #8d52fc;   \n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: #693af5;\n"
"}\n"
"QPushButton:disabled {\n"
"	background-color: #dbcffc; \n"
"}\n"
"\n"
"\n"
"\n"
"/* ======= QTabWidget ======= */\n"
"QTabWidget::pane { \n"
"    border-top: transparent;\n"
"}\n"
"QTabW"
                        "idget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"QTabBar::tab {\n"
"	font-size: 14px;\n"
"	font-weight: bold;\n"
"    background: #906ef7;\n"
"	color: #fbfbfb;\n"
"	border-radius: 16px;\n"
"	padding: 13px;\n"
"	padding-top: 7px;\n"
"	padding-bottom: 7px;\n"
"	margin-bottom: 10px;\n"
"	margin-right: 10px;\n"
"}\n"
"QTabBar::tab:hover{\n"
"	background-color: #8d52fc;   \n"
"}\n"
"QTabBar::tab:selected{\n"
"    background: #693af5;\n"
"}\n"
"\n"
"\n"
"\n"
"/*===== QFrame =====*/\n"
"#header_frame, #body_frame,  #info_frame, #search_frame{\n"
"	background: #fbfbfb;\n"
"	border-radius: 7px;\n"
"}\n"
"#search_frame {\n"
"	border: 1px solid #dbcffc;\n"
"}\n"
"\n"
"\n"
"\n"
"/*===== QScrollArea =====*/\n"
"#direct_scrollArea, #private_scrollArea, #public_scrollArea{\n"
"	border: 1px solid #dbcffc;\n"
"	background: #fbfbfb;\n"
"	border-radius: 7px;\n"
"}\n"
"QScrollArea::corner { \n"
"	background-color: transparent; \n"
"}\n"
"\n"
"\n"
"\n"
"/* ======= QCheckBox ======= */\n"
"QCheckBox {\n"
"	padding-left:10px;\n"
""
                        "}\n"
"QCheckBox::indicator {\n"
"	background: #f1effc;\n"
"	border-radius : 5px;\n"
"	border-top-right-radius: 2px;\n"
"	border : 1px solid #693af5;\n"
"}\n"
"QCheckBox::indicator::checked{\n"
"	background-color: #8d52fc; \n"
"	border : 1px solid #693af5 \n"
"}\n"
"/*dbcffc*/\n"
"QCheckBox:disabled {\n"
"	color: #693af5;\n"
"}\n"
"QCheckBox::indicator:disabled {\n"
"	border: 1px solid #693af5;\n"
"}\n"
"QCheckBox::indicator:checked:disabled {\n"
"	background: #8d52fc;\n"
"}\n"
"\n"
"\n"
"\n"
"/* ======= Line ======= */\n"
"#line, #line_2, #line_3{\n"
"	background: #dbcffc;\n"
"}\n"
"\n"
"\n"
"\n"
"/* ======= QScrollBar ======= */\n"
" QScrollBar:vertical{\n"
"	width: 17px;\n"
"	margin: 3px 3px 3px  3px;\n"
"	border:  transparent;\n"
"	border-radius: 5px;\n"
"	background-color: #f1effc; \n"
"}\n"
" QScrollBar:horizontal{\n"
"	height: 17px;\n"
"	margin: 3px 3px 3px  3px;\n"
"	border:  transparent;\n"
"	border-radius: 5px;\n"
"	background-color: #f1effc; \n"
"}/*f1effc*/\n"
"\n"
"QScrollBar::handle:vertical{\n"
""
                        "	background-color: #906ef7;      \n"
"	min-height: 50px;\n"
"	border-radius: 5px;\n"
"}\n"
"QScrollBar::handle:horizontal{\n"
"	background-color: #906ef7;      \n"
"	min-width: 50px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"	background: #8d52fc;\n"
"}\n"
"QScrollBar::handle:horizontal:hover {\n"
"	background: #8d52fc;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:pressed {\n"
"	background: #693af5;\n"
"}\n"
"QScrollBar::handle:horizontal:pressed {\n"
"	background: #693af5;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"	width: 0px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"	width: 0px;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"	height: 0px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{\n"
"	background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{\n"
"	background: none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(485, 0))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.main_work_frame = QFrame(self.centralwidget)
        self.main_work_frame.setObjectName(u"main_work_frame")
        self.main_work_frame.setMinimumSize(QSize(485, 0))
        self.main_work_frame.setFrameShape(QFrame.StyledPanel)
        self.main_work_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_work_frame)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_work_frame)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(485, 0))
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.header_info_frame = QFrame(self.header_frame)
        self.header_info_frame.setObjectName(u"header_info_frame")
        self.header_info_frame.setFrameShape(QFrame.StyledPanel)
        self.header_info_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_info_frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header_info_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self._user_name_label = QLabel(self.frame)
        self._user_name_label.setObjectName(u"_user_name_label")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(False)
        self._user_name_label.setFont(font)

        self.verticalLayout.addWidget(self._user_name_label, 0, Qt.AlignRight)

        self._workspace_label = QLabel(self.frame)
        self._workspace_label.setObjectName(u"_workspace_label")
        self._workspace_label.setFont(font)

        self.verticalLayout.addWidget(self._workspace_label, 0, Qt.AlignRight)


        self.horizontalLayout.addWidget(self.frame)

        self.line_3 = QFrame(self.header_info_frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setMinimumSize(QSize(1, 0))
        self.line_3.setMaximumSize(QSize(1, 16777215))
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_3)

        self.user_labels_frame = QFrame(self.header_info_frame)
        self.user_labels_frame.setObjectName(u"user_labels_frame")
        self.user_labels_frame.setFrameShape(QFrame.StyledPanel)
        self.user_labels_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.user_labels_frame)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.user_name_label = QLabel(self.user_labels_frame)
        self.user_name_label.setObjectName(u"user_name_label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setWeight(QFont.DemiBold)
        self.user_name_label.setFont(font1)

        self.verticalLayout_3.addWidget(self.user_name_label)

        self.workspace_name_label = QLabel(self.user_labels_frame)
        self.workspace_name_label.setObjectName(u"workspace_name_label")
        self.workspace_name_label.setFont(font1)

        self.verticalLayout_3.addWidget(self.workspace_name_label)


        self.horizontalLayout.addWidget(self.user_labels_frame)


        self.horizontalLayout_2.addWidget(self.header_info_frame, 0, Qt.AlignLeft)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.header_buttons_frame = QFrame(self.header_frame)
        self.header_buttons_frame.setObjectName(u"header_buttons_frame")
        self.header_buttons_frame.setMinimumSize(QSize(221, 0))
        self.header_buttons_frame.setMaximumSize(QSize(221, 16777215))
        self.header_buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.header_buttons_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_buttons_frame)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.header_buttons_frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(1, 0))
        self.line_2.setMaximumSize(QSize(1, 16777215))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)

        self.log_out_pushButton = QPushButton(self.header_buttons_frame)
        self.log_out_pushButton.setObjectName(u"log_out_pushButton")
        self.log_out_pushButton.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.log_out_pushButton.sizePolicy().hasHeightForWidth())
        self.log_out_pushButton.setSizePolicy(sizePolicy)
        self.log_out_pushButton.setMinimumSize(QSize(78, 0))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(True)
        self.log_out_pushButton.setFont(font2)

        self.horizontalLayout_4.addWidget(self.log_out_pushButton)

        self.line = QFrame(self.header_buttons_frame)
        self.line.setObjectName(u"line")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy1)
        self.line.setMinimumSize(QSize(1, 0))
        self.line.setMaximumSize(QSize(1, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        self.line.setFont(font3)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.backup_pushButton = QPushButton(self.header_buttons_frame)
        self.backup_pushButton.setObjectName(u"backup_pushButton")
        self.backup_pushButton.setEnabled(True)
        self.backup_pushButton.setMinimumSize(QSize(111, 0))
        self.backup_pushButton.setFont(font2)

        self.horizontalLayout_4.addWidget(self.backup_pushButton)


        self.horizontalLayout_2.addWidget(self.header_buttons_frame, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.body_frame = QFrame(self.main_work_frame)
        self.body_frame.setObjectName(u"body_frame")
        sizePolicy1.setHeightForWidth(self.body_frame.sizePolicy().hasHeightForWidth())
        self.body_frame.setSizePolicy(sizePolicy1)
        self.body_frame.setFrameShape(QFrame.StyledPanel)
        self.body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.body_frame)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.search_frame = QFrame(self.body_frame)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.search_frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(10, 10, 10, 10)
        self.search_lineEdit = QLineEdit(self.search_frame)
        self.search_lineEdit.setObjectName(u"search_lineEdit")

        self.verticalLayout_9.addWidget(self.search_lineEdit)


        self.verticalLayout_4.addWidget(self.search_frame)

        self.tabWidget = QTabWidget(self.body_frame)
        self.tabWidget.setObjectName(u"tabWidget")
        self.public_tab = QWidget()
        self.public_tab.setObjectName(u"public_tab")
        self.verticalLayout_10 = QVBoxLayout(self.public_tab)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.public_scroll_frame = QFrame(self.public_tab)
        self.public_scroll_frame.setObjectName(u"public_scroll_frame")
        self.public_scroll_frame.setEnabled(True)
        self.public_scroll_frame.setFrameShape(QFrame.StyledPanel)
        self.public_scroll_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.public_scroll_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.public_scrollArea = QScrollArea(self.public_scroll_frame)
        self.public_scrollArea.setObjectName(u"public_scrollArea")
        self.public_scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.public_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.public_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.public_scrollArea.setWidgetResizable(True)
        self.public_scrollAreaWidgetContents = QWidget()
        self.public_scrollAreaWidgetContents.setObjectName(u"public_scrollAreaWidgetContents")
        self.public_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 508, 342))
        self.verticalLayout_6 = QVBoxLayout(self.public_scrollAreaWidgetContents)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.public_chats_frame = QFrame(self.public_scrollAreaWidgetContents)
        self.public_chats_frame.setObjectName(u"public_chats_frame")
        self.public_chats_frame.setEnabled(True)
        self.public_chats_frame.setFrameShape(QFrame.StyledPanel)
        self.public_chats_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.public_chats_frame)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 6, 0, 6)

        self.verticalLayout_6.addWidget(self.public_chats_frame, 0, Qt.AlignTop)

        self.public_scrollArea.setWidget(self.public_scrollAreaWidgetContents)

        self.horizontalLayout_5.addWidget(self.public_scrollArea)


        self.verticalLayout_10.addWidget(self.public_scroll_frame)

        self.tabWidget.addTab(self.public_tab, "")
        self.private_tab = QWidget()
        self.private_tab.setObjectName(u"private_tab")
        self.verticalLayout_14 = QVBoxLayout(self.private_tab)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.private_scroll_frame = QFrame(self.private_tab)
        self.private_scroll_frame.setObjectName(u"private_scroll_frame")
        self.private_scroll_frame.setEnabled(True)
        self.private_scroll_frame.setFrameShape(QFrame.StyledPanel)
        self.private_scroll_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.private_scroll_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.private_scrollArea = QScrollArea(self.private_scroll_frame)
        self.private_scrollArea.setObjectName(u"private_scrollArea")
        self.private_scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.private_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.private_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.private_scrollArea.setWidgetResizable(True)
        self.private_scrollAreaWidgetContents = QWidget()
        self.private_scrollAreaWidgetContents.setObjectName(u"private_scrollAreaWidgetContents")
        self.private_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 508, 342))
        self.verticalLayout_11 = QVBoxLayout(self.private_scrollAreaWidgetContents)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.private_chats_frame = QFrame(self.private_scrollAreaWidgetContents)
        self.private_chats_frame.setObjectName(u"private_chats_frame")
        self.private_chats_frame.setEnabled(True)
        self.private_chats_frame.setFrameShape(QFrame.StyledPanel)
        self.private_chats_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.private_chats_frame)
        self.verticalLayout_12.setSpacing(10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 6, 0, 6)

        self.verticalLayout_11.addWidget(self.private_chats_frame, 0, Qt.AlignTop)

        self.private_scrollArea.setWidget(self.private_scrollAreaWidgetContents)

        self.horizontalLayout_7.addWidget(self.private_scrollArea)


        self.verticalLayout_14.addWidget(self.private_scroll_frame)

        self.tabWidget.addTab(self.private_tab, "")
        self.direct_tab = QWidget()
        self.direct_tab.setObjectName(u"direct_tab")
        self.verticalLayout_18 = QVBoxLayout(self.direct_tab)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.direct_scroll_frame = QFrame(self.direct_tab)
        self.direct_scroll_frame.setObjectName(u"direct_scroll_frame")
        self.direct_scroll_frame.setEnabled(True)
        self.direct_scroll_frame.setFrameShape(QFrame.StyledPanel)
        self.direct_scroll_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.direct_scroll_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.direct_scrollArea = QScrollArea(self.direct_scroll_frame)
        self.direct_scrollArea.setObjectName(u"direct_scrollArea")
        self.direct_scrollArea.setMaximumSize(QSize(16777215, 16777215))
        self.direct_scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.direct_scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.direct_scrollArea.setWidgetResizable(True)
        self.direct_scrollAreaWidgetContents = QWidget()
        self.direct_scrollAreaWidgetContents.setObjectName(u"direct_scrollAreaWidgetContents")
        self.direct_scrollAreaWidgetContents.setGeometry(QRect(0, 0, 508, 342))
        self.verticalLayout_15 = QVBoxLayout(self.direct_scrollAreaWidgetContents)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.direct_chats_frame = QFrame(self.direct_scrollAreaWidgetContents)
        self.direct_chats_frame.setObjectName(u"direct_chats_frame")
        self.direct_chats_frame.setEnabled(True)
        self.direct_chats_frame.setFrameShape(QFrame.StyledPanel)
        self.direct_chats_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.direct_chats_frame)
        self.verticalLayout_16.setSpacing(10)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 6, 0, 6)

        self.verticalLayout_15.addWidget(self.direct_chats_frame, 0, Qt.AlignTop)

        self.direct_scrollArea.setWidget(self.direct_scrollAreaWidgetContents)

        self.horizontalLayout_6.addWidget(self.direct_scrollArea)


        self.verticalLayout_18.addWidget(self.direct_scroll_frame)

        self.tabWidget.addTab(self.direct_tab, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.verticalLayout_5.addWidget(self.body_frame)


        self.verticalLayout_2.addWidget(self.main_work_frame)

        self.info_frame = QFrame(self.centralwidget)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMinimumSize(QSize(485, 0))
        self.info_frame.setMaximumSize(QSize(16777215, 16777215))
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.info_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.frame_3 = QFrame(self.info_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.info_label = QLabel(self.frame_3)
        self.info_label.setObjectName(u"info_label")

        self.verticalLayout_8.addWidget(self.info_label, 0, Qt.AlignHCenter)

        self.auth_pushButton = QPushButton(self.frame_3)
        self.auth_pushButton.setObjectName(u"auth_pushButton")
        self.auth_pushButton.setMinimumSize(QSize(0, 0))

        self.verticalLayout_8.addWidget(self.auth_pushButton, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.frame_3, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_2.addWidget(self.info_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Yummy Slack", None))
        self._user_name_label.setText(QCoreApplication.translate("MainWindow", u"User name", None))
        self._workspace_label.setText(QCoreApplication.translate("MainWindow", u"Workspace", None))
        self.user_name_label.setText(QCoreApplication.translate("MainWindow", u"some user-name", None))
        self.workspace_name_label.setText(QCoreApplication.translate("MainWindow", u"some team-name", None))
        self.log_out_pushButton.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.backup_pushButton.setText(QCoreApplication.translate("MainWindow", u"Start Backup", None))
        self.search_lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.public_tab), QCoreApplication.translate("MainWindow", u"Public channels", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.private_tab), QCoreApplication.translate("MainWindow", u"Private channels", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.direct_tab), QCoreApplication.translate("MainWindow", u"Direct messages", None))
        self.info_label.setText(QCoreApplication.translate("MainWindow", u"Some info", None))
        self.auth_pushButton.setText(QCoreApplication.translate("MainWindow", u"Loading...", None))
    # retranslateUi

