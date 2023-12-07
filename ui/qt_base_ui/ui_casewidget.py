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
    QLineEdit, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_CaseWidget(object):
    def setupUi(self, CaseWidget):
        if not CaseWidget.objectName():
            CaseWidget.setObjectName(u"CaseWidget")
        CaseWidget.resize(319, 307)
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
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.targetEdit = QLineEdit(self.groupBox_2)
        self.targetEdit.setObjectName(u"targetEdit")
        self.targetEdit.setFont(font)
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
        self.descriptionEdit = QTextEdit(self.groupBox)
        self.descriptionEdit.setObjectName(u"descriptionEdit")
        self.descriptionEdit.setFont(font)
        self.descriptionEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.verticalLayout.addWidget(self.descriptionEdit)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.verticalLayout_3.addWidget(self.groupBox_2)


        self.retranslateUi(CaseWidget)

        QMetaObject.connectSlotsByName(CaseWidget)
    # setupUi

    def retranslateUi(self, CaseWidget):
        CaseWidget.setWindowTitle(QCoreApplication.translate("CaseWidget", u"Form", None))
        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("CaseWidget", u"\u0426\u0435\u043b\u044c", None))
        self.groupBox.setTitle(QCoreApplication.translate("CaseWidget", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.descriptionEdit.setHtml(QCoreApplication.translate("CaseWidget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

