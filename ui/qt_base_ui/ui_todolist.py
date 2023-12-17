# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_todolist.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ToDoListWidget(object):
    def setupUi(self, ToDoListWidget):
        if not ToDoListWidget.objectName():
            ToDoListWidget.setObjectName(u"ToDoListWidget")
        ToDoListWidget.resize(400, 524)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        ToDoListWidget.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(ToDoListWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(ToDoListWidget)
        self.groupBox.setObjectName(u"groupBox")
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addButton = QPushButton(self.groupBox)
        self.addButton.setObjectName(u"addButton")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(False)
        self.addButton.setFont(font2)

        self.verticalLayout.addWidget(self.addButton)

        self.todoListLayout = QVBoxLayout()
        self.todoListLayout.setObjectName(u"todoListLayout")

        self.verticalLayout.addLayout(self.todoListLayout)

        self.clearButton = QPushButton(self.groupBox)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setFont(font2)

        self.verticalLayout.addWidget(self.clearButton)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.retranslateUi(ToDoListWidget)

        QMetaObject.connectSlotsByName(ToDoListWidget)
    # setupUi

    def retranslateUi(self, ToDoListWidget):
        ToDoListWidget.setWindowTitle(QCoreApplication.translate("ToDoListWidget", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("ToDoListWidget", u"GroupBox", None))
        self.addButton.setText(QCoreApplication.translate("ToDoListWidget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.clearButton.setText(QCoreApplication.translate("ToDoListWidget", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
    # retranslateUi

