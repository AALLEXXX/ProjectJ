# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_text_window.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QGroupBox,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
from ui.qt_base_ui.ui_text_widget import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(758, 478)
        Form.setStyleSheet(u"QWidget#Form{border-image: url(:/imgaes/macos-monterey-1920x1080-23425.png);\n"
"background-size: cover;\n"
"}\n"
"\n"
"QPlainTextEdit {\n"
"    background-color: rgba(255, 255, 255, 50); /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c \u0444\u043e\u043d\u0430 \u043f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 */\n"
"    border: 1px solid #ccc; /* \u041e\u0431\u0432\u043e\u0434\u043a\u0430 \u043f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 */\n"
"    border-radius: 5px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u043f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 */\n"
"    padding: 5px; /* \u041e\u0442\u0441\u0442\u0443\u043f \u0432\u043d\u0443\u0442\u0440\u0438 \u043f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 */\n"
"color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPlainTextEdit:hover {\n"
"    background-color: rgba(255, 255, 255, 100); /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c"
                        " \u0444\u043e\u043d\u0430 \u043f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPlainTextEdit:focus {\n"
"    background-color: rgba(255, 255, 255, 100); /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c \u0444\u043e\u043d\u0430 \u043f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 \u043f\u0440\u0438 \u0444\u043e\u043a\u0443\u0441\u0435 */\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: rgba(100, 100, 255, 100); /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c \u0444\u043e\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border: 1px solid #555; /* \u041e\u0431\u0432\u043e\u0434\u043a\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    border-radius: 5px; /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0435\u043d\u0438\u0435 \u0443\u0433\u043b\u043e\u0432 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"    padding: 5px 10px; /* \u041e\u0442\u0441\u0442"
                        "\u0443\u043f\u044b \u0432\u043d\u0443\u0442\u0440\u0438 \u043a\u043d\u043e\u043f\u043a\u0438 */\n"
"	color:rgb(255, 255, 255)\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(100, 100, 255, 150); /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c \u0444\u043e\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgba(100, 100, 255, 200); /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u043e\u0441\u0442\u044c \u0444\u043e\u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0438 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}")
        self.create_case_but = QPushButton(Form)
        self.create_case_but.setObjectName(u"create_case_but")
        self.create_case_but.setGeometry(QRect(340, 360, 113, 32))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create_case_but.sizePolicy().hasHeightForWidth())
        self.create_case_but.setSizePolicy(sizePolicy)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(530, 140, 169, 161))
        self.groupBox.setStyleSheet(u"color:white;")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.blocker_checkBox = QCheckBox(self.groupBox)
        self.buttonGroup = QButtonGroup(Form)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.blocker_checkBox)
        self.blocker_checkBox.setObjectName(u"blocker_checkBox")
        font = QFont()
        font.setPointSize(16)
        self.blocker_checkBox.setFont(font)
        self.blocker_checkBox.setStyleSheet(u"color:white;")

        self.verticalLayout.addWidget(self.blocker_checkBox)

        self.critical_checkBox = QCheckBox(self.groupBox)
        self.buttonGroup.addButton(self.critical_checkBox)
        self.critical_checkBox.setObjectName(u"critical_checkBox")
        self.critical_checkBox.setFont(font)
        self.critical_checkBox.setStyleSheet(u"color:white;")

        self.verticalLayout.addWidget(self.critical_checkBox)

        self.major_checkBox = QCheckBox(self.groupBox)
        self.buttonGroup.addButton(self.major_checkBox)
        self.major_checkBox.setObjectName(u"major_checkBox")
        self.major_checkBox.setFont(font)
        self.major_checkBox.setStyleSheet(u"color:white;")

        self.verticalLayout.addWidget(self.major_checkBox)

        self.minor_checkBox = QCheckBox(self.groupBox)
        self.buttonGroup.addButton(self.minor_checkBox)
        self.minor_checkBox.setObjectName(u"minor_checkBox")
        self.minor_checkBox.setFont(font)
        self.minor_checkBox.setStyleSheet(u"color:white;")

        self.verticalLayout.addWidget(self.minor_checkBox)

        self.trivial_checkBox = QCheckBox(self.groupBox)
        self.buttonGroup.addButton(self.trivial_checkBox)
        self.trivial_checkBox.setObjectName(u"trivial_checkBox")
        self.trivial_checkBox.setFont(font)
        self.trivial_checkBox.setStyleSheet(u"color:white;")

        self.verticalLayout.addWidget(self.trivial_checkBox)

        self.descr_TextEdit = QPlainTextEdit(Form)
        self.descr_TextEdit.setObjectName(u"descr_TextEdit")
        self.descr_TextEdit.setGeometry(QRect(50, 140, 381, 151))
        self.target_TextEdit = QPlainTextEdit(Form)
        self.target_TextEdit.setObjectName(u"target_TextEdit")
        self.target_TextEdit.setGeometry(QRect(100, 88, 271, 31))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.create_case_but.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.groupBox.setTitle("")
        self.blocker_checkBox.setText(QCoreApplication.translate("Form", u"\u0411\u043b\u043e\u043a\u0438\u0440\u0443\u044e\u0449\u0430\u044f", None))
        self.critical_checkBox.setText(QCoreApplication.translate("Form", u"\u041a\u0440\u0438\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f ", None))
        self.major_checkBox.setText(QCoreApplication.translate("Form", u"\u0421\u0443\u0449\u0435\u0441\u0442\u0432\u0435\u043d\u043d\u0430\u044f", None))
        self.minor_checkBox.setText(QCoreApplication.translate("Form", u"\u041d\u0435\u0437\u043d\u0430\u0447\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f", None))
        self.trivial_checkBox.setText(QCoreApplication.translate("Form", u"\u041c\u0435\u043b\u043e\u0447\u044c", None))
        self.descr_TextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.target_TextEdit.setPlainText("")
        self.target_TextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u0426\u0435\u043b\u044c", None))
    # retranslateUi

