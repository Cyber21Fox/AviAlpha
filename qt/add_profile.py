# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_profile.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setWindowModality(Qt.WindowModal)
        Widget.resize(412, 426)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setStyleSheet(u"QWidget{\n"
"	background: #292929;\n"
"}\n"
"\n"
"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QLineEdit{\n"
"    color: rgb(255, 255, 255);\n"
" 	border: 1px solid #ffa31a;\n"
"    border-width: 1.5px;\n"
"    border-radius: 5px;\n"
"    border-color: #ffa31a;\n"
" 	padding: 6px;\n"
"	height: 20px;\n"
" }\n"
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
"    width: 1"
                        "5px;\n"
"\n"
"    border-left-width: 2px;\n"
"    border-left-color: #ffa31a;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
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
"\n"
"\n"
"\n"
"\n"
"\n"
"QProgressBar {\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"	text-align: center;\n"
"	color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #ffa31a;\n"
"    width: 20px;\n"
"	margin: 0.5px;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane {\n"
"    border-top: 1px solid  #808080;\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 10px; \n"
"}\n"
"\n"
"QTabBar::tab {\n"
"	border-color:  #ffa31a;\n"
""
                        "	background-color: #ffa31a;\n"
"    border: 2px solid #292929;\n"
"    border-bottom-color: #292929;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 15ex;\n"
"    padding: 2px;\n"
"}\n"
"\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    background:qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0)) ;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    border-color: #292929;\n"
"    border-bottom-color: #292929; \n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    margin-top: 2px; \n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    margin-left: -4px;\n"
"    margin-right: -4px;\n"
"}\n"
"\n"
"QTabBar::tab:first:selected {\n"
"    margin-left: 0; \n"
"}\n"
"\n"
"QTabBar::tab:last:selected {\n"
"    margin-right: 0; \n"
"}\n"
"\n"
"QTabBar::tab:only-one {\n"
"    margin: 0; \n"
"}\n"
"\n"
"QSpinBox {\n"
"    padding-right: 15px;\n"
"	\n"
"	\n"
"	\n"
"	c"
                        "olor: rgb(255, 255, 255);\n"
"    border-width: 3;\n"
"}\n"
"")
        self.gridLayout_2 = QGridLayout(Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 2, -1, 2)
        self.frame = QFrame(Widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 4, -1, -1)
        self.comboBox_webgl = QComboBox(self.frame)
        self.comboBox_webgl.setObjectName(u"comboBox_webgl")
        self.comboBox_webgl.setMinimumSize(QSize(145, 0))
        self.comboBox_webgl.setMaximumSize(QSize(200, 16777215))
        self.comboBox_webgl.setStyleSheet(u"")

        self.gridLayout.addWidget(self.comboBox_webgl, 5, 1, 1, 1)

        self.lineEdit_profile_pass = QLineEdit(self.frame)
        self.lineEdit_profile_pass.setObjectName(u"lineEdit_profile_pass")
        self.lineEdit_profile_pass.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.lineEdit_profile_pass, 3, 1, 1, 1)

        self.comboBox_os = QComboBox(self.frame)
        self.comboBox_os.setObjectName(u"comboBox_os")
        self.comboBox_os.setMinimumSize(QSize(145, 0))
        self.comboBox_os.setMaximumSize(QSize(200, 16777215))
        self.comboBox_os.setStyleSheet(u"")

        self.gridLayout.addWidget(self.comboBox_os, 4, 1, 1, 1)

        self.comboBox_render = QComboBox(self.frame)
        self.comboBox_render.setObjectName(u"comboBox_render")
        self.comboBox_render.setMinimumSize(QSize(145, 0))
        self.comboBox_render.setMaximumSize(QSize(200, 16777215))
        self.comboBox_render.setStyleSheet(u"")

        self.gridLayout.addWidget(self.comboBox_render, 6, 1, 1, 1)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.lineEdit_profile_login = QLineEdit(self.frame)
        self.lineEdit_profile_login.setObjectName(u"lineEdit_profile_login")
        self.lineEdit_profile_login.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.lineEdit_profile_login, 2, 1, 1, 1)

        self.pushButton_add_profile = QPushButton(self.frame)
        self.pushButton_add_profile.setObjectName(u"pushButton_add_profile")
        self.pushButton_add_profile.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_add_profile, 7, 0, 1, 2)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label_72 = QLabel(self.frame)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_72.setFont(font)

        self.gridLayout.addWidget(self.label_72, 0, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.lineEdit_profile_name = QLineEdit(self.frame)
        self.lineEdit_profile_name.setObjectName(u"lineEdit_profile_name")
        self.lineEdit_profile_name.setMaximumSize(QSize(200, 16777215))

        self.gridLayout.addWidget(self.lineEdit_profile_name, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u0430", None))
        self.lineEdit_profile_pass.setText("")
        self.label_5.setText(QCoreApplication.translate("Widget", u"Webgl_Vendor", None))
        self.lineEdit_profile_login.setText("")
        self.pushButton_add_profile.setText(QCoreApplication.translate("Widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0411\u0414", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Render", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"\u041e\u043f\u0435\u0440\u0430\u0446\u0438\u043e\u043d\u043a\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_72.setText(QCoreApplication.translate("Widget", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442 \u0432 \u0431\u0430\u0437\u0443 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.label.setText(QCoreApplication.translate("Widget", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lineEdit_profile_name.setText("")
        self.label_4.setText(QCoreApplication.translate("Widget", u"\u0418\u043c\u044f", None))
    # retranslateUi

