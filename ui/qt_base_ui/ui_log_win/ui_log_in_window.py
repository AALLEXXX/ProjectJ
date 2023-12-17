# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_log_in_window.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
from ui.qt_base_ui.ui_log_win import res_rc
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.bgwidget = QWidget(Dialog)
        self.bgwidget.setObjectName(u"bgwidget")
        self.bgwidget.setGeometry(QRect(0, 0, 640, 500))
        self.bgwidget.setStyleSheet(u"/* \u041e\u043a\u043d\u043e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f */\n"
"QWidget#bgwidget {\n"
"    border-image: url(:/images/log_bg.png); /* \u0417\u0430\u043c\u0435\u043d\u0438\u0442\u0435 \u043d\u0430 \u043f\u0443\u0442\u044c \u043a \u0432\u0430\u0448\u0435\u0439 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0435 */\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-attachment: fixed;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u044f \u0434\u043b\u044f \u0432\u0432\u043e\u0434\u0430 */\n"
"QLineEdit {\n"
"    background: rgba(255, 255, 255, 50); /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0431\u0435\u043b\u044b\u0439 \u0446\u0432\u0435\u0442 */\n"
"    border: 2px solid #aaa; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid lightblue; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438"
                        "\u0446\u044b \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 */\n"
"}\n"
"\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0430 */\n"
"QPushButton{\n"
"    background: rgba(0, 128, 255, 30); /* \u041f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0446\u0432\u0435\u0442 */\n"
"    border: 2px solid #aaa; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgba(0, 128, 255, 50); /* \u0426\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    border-color: #666; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    color: #eee; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u0440"
                        "\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"\n"
"/* \u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430 \u0432 \u043f\u043e\u043b\u044f\u0445 \u0432\u0432\u043e\u0434\u0430 */\n"
"QLineEdit::placeholder {\n"
"    color: #888; /* \u0426\u0432\u0435\u0442 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0438 */\n"
"}\n"
"QPushButton:pressed {\n"
"    background: rgba(0, 128, 255, 90); /* \u0426\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border-color: #666; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    color: #eee; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"/* \u0422\u0435\u043a\u0441\u0442 \u0432 \u043f\u043e\u043b\u044f\u0445 \u0432\u0432\u043e\u0434\u0430 */\n"
"QLineEdit, QLabel {\n"
"    color: white; /* \u0427\u0435\u0440\u043d\u044b"
                        "\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"")
        self.login_text = QLineEdit(self.bgwidget)
        self.login_text.setObjectName(u"login_text")
        self.login_text.setGeometry(QRect(218, 160, 211, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.login_text.sizePolicy().hasHeightForWidth())
        self.login_text.setSizePolicy(sizePolicy1)
        self.create_acc_prog_but = QPushButton(self.bgwidget)
        self.create_acc_prog_but.setObjectName(u"create_acc_prog_but")
        self.create_acc_prog_but.setGeometry(QRect(150, 400, 140, 32))
        sizePolicy1.setHeightForWidth(self.create_acc_prog_but.sizePolicy().hasHeightForWidth())
        self.create_acc_prog_but.setSizePolicy(sizePolicy1)
        self.password_text = QLineEdit(self.bgwidget)
        self.password_text.setObjectName(u"password_text")
        self.password_text.setGeometry(QRect(218, 230, 211, 31))
        sizePolicy1.setHeightForWidth(self.password_text.sizePolicy().hasHeightForWidth())
        self.password_text.setSizePolicy(sizePolicy1)
        self.label = QLabel(self.bgwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(293, 80, 65, 35))
        self.label.setMinimumSize(QSize(65, 35))
        self.label.setMaximumSize(QSize(100, 60))
        self.label.setStyleSheet(u"\n"
"font: 26pt \"Apple Symbols\";")
        self.log_in_but = QPushButton(self.bgwidget)
        self.log_in_but.setObjectName(u"log_in_but")
        self.log_in_but.setGeometry(QRect(270, 310, 113, 32))
        sizePolicy1.setHeightForWidth(self.log_in_but.sizePolicy().hasHeightForWidth())
        self.log_in_but.setSizePolicy(sizePolicy1)
        self.create_acc_lead_but = QPushButton(self.bgwidget)
        self.create_acc_lead_but.setObjectName(u"create_acc_lead_but")
        self.create_acc_lead_but.setGeometry(QRect(360, 400, 140, 32))
        sizePolicy1.setHeightForWidth(self.create_acc_lead_but.sizePolicy().hasHeightForWidth())
        self.create_acc_lead_but.setSizePolicy(sizePolicy1)
        self.label_2 = QLabel(self.bgwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(154, 372, 130, 20))
        self.label_3 = QLabel(self.bgwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(367, 374, 131, 16))
        self.warning_label = QLabel(self.bgwidget)
        self.warning_label.setObjectName(u"warning_label")
        self.warning_label.setGeometry(QRect(225, 280, 201, 16))
        self.warning_label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.login_text.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.create_acc_prog_but.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.password_text.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0412\u0445\u043e\u0434", None))
        self.log_in_but.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.create_acc_lead_but.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0414\u043b\u044f \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0441\u0442\u043e\u0432", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u043b\u044f \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u0435\u0439", None))
        self.warning_label.setText("")
    # retranslateUi

