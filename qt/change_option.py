# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'change_option.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(481, 238)
        Widget.setStyleSheet(u"QWidget{\n"
"	background: #292929;\n"
"}\n"
"\n"
"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #ffa31a;\n"
"    border-width: 2px;\n"
"    border-radius: 7px;\n"
"    border-color:  #ffa31a;\n"
" 	padding: 6px;}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: #FF801A;\n"
"	border-color: #D17B37;\n"
"    border-style: inset;\n"
"}\n"
"QComboBox {\n"
"    border: 1px solid #ffa31a;\n"
"	border-width: 1.5px;\n"
"    border-radius: 5px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"	height: 27px;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: white;\n"
"\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 15px;\n"
"\n"
"    border-left-width: 2px;\n"
"    border-left-color: #ffa31a;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow"
                        " {\n"
"   color: black;\n"
"\n"
"}\n"
"\n"
"QComboBox:!editable, QComboBox::drop-down:editable {\n"
"\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:on {\n"
"\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 5)

        self.verticalSpacer = QSpacerItem(20, 89, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 2, 1)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(300, 0))
        font = QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)

        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 3)

        self.verticalSpacer_2 = QSpacerItem(20, 89, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 4, 2, 1)

        self.horizontalSpacer_4 = QSpacerItem(103, 29, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 2, 1, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 25))

        self.gridLayout_2.addWidget(self.pushButton, 2, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(102, 29, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 3, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText(QCoreApplication.translate("Widget", u"<html><head/><body><p><span style=\" font-size:12pt;\">\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u0438\u0437 \u043f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u043d\u043e\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"\u0422\u0430\u043a \u0442\u043e\u0447\u043d\u043e!", None))
    # retranslateUi

