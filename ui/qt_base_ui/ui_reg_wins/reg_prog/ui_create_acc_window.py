# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_create_acc_window.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QDialog,
    QGroupBox, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
from ui.qt_base_ui.ui_reg_wins.reg_prog import res_rc
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(916, 570)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(910, 560))
        Dialog.setMaximumSize(QSize(1280, 720))
        Dialog.setMouseTracking(False)
        Dialog.setStyleSheet(u"")
        self.bgwidget = QWidget(Dialog)
        self.bgwidget.setObjectName(u"bgwidget")
        self.bgwidget.setEnabled(True)
        self.bgwidget.setGeometry(QRect(0, -20, 920, 600))
        self.bgwidget.setMaximumSize(QSize(1280, 720))
        self.bgwidget.setStyleSheet(u"/* \u041e\u043a\u043d\u043e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u044f */\n"
"QWidget#bgwidget {\n"
"    border-image: url(:/images/mini_gori.png); /* \u0417\u0430\u043c\u0435\u043d\u0438\u0442\u0435 \u043d\u0430 \u043f\u0443\u0442\u044c \u043a \u0432\u0430\u0448\u0435\u0439 \u043a\u0430\u0440\u0442\u0438\u043d\u043a\u0435 */\n"
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
"/* \u041a\u043d\u043e\u043f\u043a\u0430 */\n"
"QPushButton{\n"
"    background: rgba(0, 128, 255, 30); /* \u041f\u0440"
                        "\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0433\u043e\u043b\u0443\u0431\u043e\u0439 \u0446\u0432\u0435\u0442 */\n"
"    border: 2px solid #aaa; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b */\n"
"    border-radius: 10px;\n"
"    padding: 5px 10px;\n"
"	color: white;\n"
"}\n"
"\n"
"/* \u041f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0430 \u0432 \u043f\u043e\u043b\u044f\u0445 \u0432\u0432\u043e\u0434\u0430 */\n"
"QLineEdit::placeholder {\n"
"    color: #888; /* \u0426\u0432\u0435\u0442 \u043f\u043e\u0434\u0441\u043a\u0430\u0437\u043a\u0438 */\n"
"}\n"
"QPushButton:hover {\n"
"    background: rgba(0, 128, 255, 50); /* \u0426\u0432\u0435\u0442 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    border-color: #666; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    color: #eee; /* \u0426\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u043f"
                        "\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
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
"    color: white; /* \u0427\u0435\u0440\u043d"
                        "\u044b\u0439 \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"    border: 2px solid lightblue; /* \u0426\u0432\u0435\u0442 \u0433\u0440\u0430\u043d\u0438\u0446\u044b \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 \u043a\u0443\u0440\u0441\u043e\u0440\u0430 */\n"
"}")
        self.name_line = QLineEdit(self.bgwidget)
        self.name_line.setObjectName(u"name_line")
        self.name_line.setEnabled(True)
        self.name_line.setGeometry(QRect(120, 330, 230, 40))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name_line.sizePolicy().hasHeightForWidth())
        self.name_line.setSizePolicy(sizePolicy1)
        self.create_acc_but = QPushButton(self.bgwidget)
        self.create_acc_but.setObjectName(u"create_acc_but")
        self.create_acc_but.setEnabled(True)
        self.create_acc_but.setGeometry(QRect(410, 450, 113, 32))
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.create_acc_but.sizePolicy().hasHeightForWidth())
        self.create_acc_but.setSizePolicy(sizePolicy2)
        self.create_acc_but.setMouseTracking(False)
        self.create_acc_but.setAcceptDrops(False)
        self.create_acc_but.setStyleSheet(u"")
        self.login_line = QLineEdit(self.bgwidget)
        self.login_line.setObjectName(u"login_line")
        self.login_line.setEnabled(True)
        self.login_line.setGeometry(QRect(120, 210, 230, 40))
        sizePolicy1.setHeightForWidth(self.login_line.sizePolicy().hasHeightForWidth())
        self.login_line.setSizePolicy(sizePolicy1)
        self.label = QLabel(self.bgwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(350, 80, 231, 50))
        self.label.setMinimumSize(QSize(201, 50))
        self.label.setMaximumSize(QSize(250, 70))
        font = QFont()
        font.setFamilies([u"Tahoma"])
        font.setPointSize(22)
        self.label.setFont(font)
        self.password_line = QLineEdit(self.bgwidget)
        self.password_line.setObjectName(u"password_line")
        self.password_line.setEnabled(True)
        self.password_line.setGeometry(QRect(120, 270, 230, 40))
        sizePolicy1.setHeightForWidth(self.password_line.sizePolicy().hasHeightForWidth())
        self.password_line.setSizePolicy(sizePolicy1)
        self.password_line.setMouseTracking(False)
        self.groupBox = QGroupBox(self.bgwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(610, 190, 201, 211))
        font1 = QFont()
        font1.setPointSize(17)
        self.groupBox.setFont(font1)
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setCheckable(False)
        self.groupBox.setChecked(False)
        self.junior_checkBox = QCheckBox(self.groupBox)
        self.buttonGroup = QButtonGroup(Dialog)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.setExclusive(True)
        self.buttonGroup.addButton(self.junior_checkBox)
        self.junior_checkBox.setObjectName(u"junior_checkBox")
        self.junior_checkBox.setGeometry(QRect(0, 60, 91, 22))
        font2 = QFont()
        font2.setPointSize(15)
        self.junior_checkBox.setFont(font2)
        self.middl_checkBox = QCheckBox(self.groupBox)
        self.buttonGroup.addButton(self.middl_checkBox)
        self.middl_checkBox.setObjectName(u"middl_checkBox")
        self.middl_checkBox.setGeometry(QRect(3, 106, 65, 22))
        self.middl_checkBox.setFont(font2)
        self.senior_checkBox = QCheckBox(self.groupBox)
        self.buttonGroup.addButton(self.senior_checkBox)
        self.senior_checkBox.setObjectName(u"senior_checkBox")
        self.senior_checkBox.setGeometry(QRect(3, 154, 79, 22))
        self.senior_checkBox.setFont(font2)
        self.code_line = QLineEdit(self.bgwidget)
        self.code_line.setObjectName(u"code_line")
        self.code_line.setEnabled(True)
        self.code_line.setGeometry(QRect(120, 390, 230, 40))
        sizePolicy1.setHeightForWidth(self.code_line.sizePolicy().hasHeightForWidth())
        self.code_line.setSizePolicy(sizePolicy1)
        self.warning_label = QLabel(self.bgwidget)
        self.warning_label.setObjectName(u"warning_label")
        self.warning_label.setGeometry(QRect(126, 130, 221, 71))
        self.warning_label.setTextFormat(Qt.AutoText)
        self.warning_label.setScaledContents(False)
        self.warning_label.setWordWrap(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.name_line.setText("")
        self.name_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f ", None))
        self.create_acc_but.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.login_line.setText("")
        self.login_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.password_line.setText("")
        self.password_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0431\u0435\u0440\u0438 \u0441\u0432\u043e\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.junior_checkBox.setText(QCoreApplication.translate("Dialog", u"\u0414\u0436\u0443\u043d\u0438\u043e\u0440", None))
        self.middl_checkBox.setText(QCoreApplication.translate("Dialog", u"\u041c\u0438\u0434\u043b", None))
        self.senior_checkBox.setText(QCoreApplication.translate("Dialog", u"\u0421\u0435\u043d\u044c\u043e\u0440", None))
        self.code_line.setText("")
        self.code_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u0434 \u043a\u043e\u043c\u0430\u043d\u0434\u044b", None))
        self.warning_label.setText("")
    # retranslateUi

