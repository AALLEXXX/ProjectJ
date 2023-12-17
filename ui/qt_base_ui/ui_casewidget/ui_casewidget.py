# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_casewidget.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPlainTextEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
from ui.qt_base_ui.ui_casewidget  import res_rc
class Ui_CaseWidget(object):
    def setupUi(self, CaseWidget):
        if not CaseWidget.objectName():
            CaseWidget.setObjectName(u"CaseWidget")
        CaseWidget.resize(319, 365)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CaseWidget.sizePolicy().hasHeightForWidth())
        CaseWidget.setSizePolicy(sizePolicy)
        CaseWidget.setMinimumSize(QSize(180, 0))
        CaseWidget.setStyleSheet(u"\n"
"background-color: rgb(103, 200, 99);\n"
"border-radius: 5px;")
        self.verticalLayout_3 = QVBoxLayout(CaseWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_2 = QGroupBox(CaseWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setCursor(QCursor(Qt.OpenHandCursor))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.targetEdit = QLineEdit(self.groupBox_2)
        self.targetEdit.setObjectName(u"targetEdit")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.targetEdit.setFont(font1)
        self.targetEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.targetEdit)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(71, 145, 255);")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.descriptionEdit = QPlainTextEdit(self.groupBox)
        self.descriptionEdit.setObjectName(u"descriptionEdit")
        self.descriptionEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color:black;")

        self.verticalLayout.addWidget(self.descriptionEdit)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.clear_but = QPushButton(self.groupBox_2)
        self.clear_but.setObjectName(u"clear_but")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.clear_but.sizePolicy().hasHeightForWidth())
        self.clear_but.setSizePolicy(sizePolicy1)
        self.clear_but.setMinimumSize(QSize(34, 34))
        self.clear_but.setMaximumSize(QSize(44, 44))
        self.clear_but.setStyleSheet(u"QPushButton {\n"
"border-image: url(:/icons/icons8-\u043c\u0443\u0441\u043e\u0440-64.png);\n"
"    min-width: 10px;\n"
"    max-width: 20px;\n"
"    min-height: 10px;\n"
"    max-height: 20px;\n"
"    background-color: white;\n"
"    border: 2px solid #dddddd;\n"
"    border-radius: 5px; /* \u041f\u043e\u043b\u043e\u0432\u0438\u043d\u0430 \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u043e\u0433\u043e \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f (min(\u0448\u0438\u0440\u0438\u043d\u0430, \u0432\u044b\u0441\u043e\u0442\u0430) / 2) */\n"
"    padding: 10px;\n"
"color:black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #f8f8f8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #dcdcdc;\n"
"    border: 2px solid #aaaaaa;\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.clear_but)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.status_case = QLabel(self.groupBox_2)
        self.status_case.setObjectName(u"status_case")
        font2 = QFont()
        font2.setPointSize(16)
        self.status_case.setFont(font2)

        self.verticalLayout_4.addWidget(self.status_case)

        self.author_case = QLabel(self.groupBox_2)
        self.author_case.setObjectName(u"author_case")
        self.author_case.setFont(font2)

        self.verticalLayout_4.addWidget(self.author_case)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.retranslateUi(CaseWidget)

        QMetaObject.connectSlotsByName(CaseWidget)
    # setupUi

    def retranslateUi(self, CaseWidget):
        CaseWidget.setWindowTitle(QCoreApplication.translate("CaseWidget", u"Form", None))
        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("CaseWidget", u"\u0426\u0435\u043b\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("CaseWidget", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.clear_but.setText("")
        self.status_case.setText(QCoreApplication.translate("CaseWidget", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c: ", None))
        self.author_case.setText(QCoreApplication.translate("CaseWidget", u"\u0410\u0432\u0442\u043e\u0440: ", None))
    # retranslateUi

