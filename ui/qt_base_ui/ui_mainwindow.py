# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1600, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setMinimumSize(QSize(1280, 720))
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget\n"
"{background-color: rgb(102, 102, 102);}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(1280, 80))
        self.frame.setMaximumSize(QSize(1920, 80))
        self.frame.setLayoutDirection(Qt.LeftToRight)
        self.frame.setStyleSheet(u"background-color: rgb(76, 76, 76);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, 16, 12, 12)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(10, 40))
        self.pushButton.setMaximumSize(QSize(200, 40))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #4c4c4c; /* \u0421\u0435\u0440\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 2px solid #333333; /* \u0422\u0435\u043c\u043d\u0435\u0435 \u0433\u0440\u0430\u043d\u0438\u0446\u0430 */\n"
"    border-radius: 10px; /* \u0420\u0430\u0434\u0438\u0443\u0441 \u0437\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u044f \u0443\u0433\u043b\u043e\u0432 */\n"
"    padding: 5px 10px; /* \u041e\u0442\u0441\u0442\u0443\u043f \u0432\u043d\u0443\u0442\u0440\u044c \u043e\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u0434\u043b\u044f \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    color: #ffffff; /* \u0411\u0435\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #606060; /* \u0421\u0432\u0435\u0442\u043b\u0435\u0435 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #404040; /* "
                        "\u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border: 2px solid #282828; /* \u0415\u0449\u0435 \u0442\u0435\u043c\u043d\u0435\u0435 \u0433\u0440\u0430\u043d\u0438\u0446\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)

        self.todoListLayout = QHBoxLayout()
        self.todoListLayout.setObjectName(u"todoListLayout")

        self.verticalLayout.addLayout(self.todoListLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1600, 24))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Name", None))
    # retranslateUi

