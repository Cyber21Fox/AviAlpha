# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPlainTextEdit, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QSpinBox, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 681)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QWidget{\n"
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
        self.gridLayout_31 = QGridLayout(MainWindow)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.progressBar = QProgressBar(MainWindow)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(0)
        self.progressBar.setOrientation(Qt.Horizontal)

        self.gridLayout_31.addWidget(self.progressBar, 2, 0, 1, 1)

        self.tabWidget = QTabWidget(MainWindow)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(11)
        self.tabWidget.setFont(font1)
        self.tabWidget.setStyleSheet(u"")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.gridLayout_34 = QGridLayout(self.tab_15)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.frame_4 = QFrame(self.tab_15)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_4)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.gridLayout_35.setContentsMargins(0, 0, 0, 0)
        self.textBrowser = QTextBrowser(self.frame_4)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_35.addWidget(self.textBrowser, 0, 0, 3, 1)

        self.label_31 = QLabel(self.frame_4)
        self.label_31.setObjectName(u"label_31")
        font2 = QFont()
        font2.setFamilies([u"GUERRILLA"])
        font2.setPointSize(28)
        self.label_31.setFont(font2)

        self.gridLayout_35.addWidget(self.label_31, 0, 1, 2, 3)

        self.label_33 = QLabel(self.frame_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)

        self.gridLayout_35.addWidget(self.label_33, 1, 2, 2, 3)

        self.label_32 = QLabel(self.frame_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)

        self.gridLayout_35.addWidget(self.label_32, 2, 3, 1, 2)


        self.gridLayout_34.addWidget(self.frame_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_15, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setStyleSheet(u"")
        self.gridLayout_17 = QGridLayout(self.tab)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.frame_12 = QFrame(self.tab)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_12)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame_43 = QFrame(self.frame_12)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_43)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(15)
        self.label_30 = QLabel(self.frame_43)
        self.label_30.setObjectName(u"label_30")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setUnderline(False)
        self.label_30.setFont(font3)

        self.gridLayout_4.addWidget(self.label_30, 0, 0, 1, 3)

        self.label = QLabel(self.frame_43)
        self.label.setObjectName(u"label")

        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_43)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_4.addWidget(self.label_2, 1, 1, 1, 1)

        self.comboBox_login = QComboBox(self.frame_43)
        self.comboBox_login.setObjectName(u"comboBox_login")
        self.comboBox_login.setMinimumSize(QSize(145, 0))
        self.comboBox_login.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.comboBox_login, 2, 0, 1, 1)

        self.comboBox_proxy_browser = QComboBox(self.frame_43)
        self.comboBox_proxy_browser.setObjectName(u"comboBox_proxy_browser")
        self.comboBox_proxy_browser.setMinimumSize(QSize(145, 0))
        self.comboBox_proxy_browser.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.comboBox_proxy_browser, 2, 1, 1, 1)

        self.pushButton_start_login = QPushButton(self.frame_43)
        self.pushButton_start_login.setObjectName(u"pushButton_start_login")
        self.pushButton_start_login.setMinimumSize(QSize(100, 0))
        self.pushButton_start_login.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.pushButton_start_login, 2, 2, 1, 1)


        self.gridLayout_5.addWidget(self.frame_43, 0, 0, 1, 1)

        self.frame_45 = QFrame(self.frame_12)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_45)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_add_data = QPushButton(self.frame_45)
        self.pushButton_add_data.setObjectName(u"pushButton_add_data")
        self.pushButton_add_data.setMinimumSize(QSize(0, 0))
        self.pushButton_add_data.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_add_data, 1, 0, 1, 1)

        self.pushButton_delete_data = QPushButton(self.frame_45)
        self.pushButton_delete_data.setObjectName(u"pushButton_delete_data")
        self.pushButton_delete_data.setMinimumSize(QSize(100, 0))
        self.pushButton_delete_data.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_delete_data, 1, 1, 1, 1)

        self.pushButton_update_data = QPushButton(self.frame_45)
        self.pushButton_update_data.setObjectName(u"pushButton_update_data")
        self.pushButton_update_data.setMinimumSize(QSize(100, 0))
        self.pushButton_update_data.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_update_data, 1, 2, 1, 1)

        self.label_3 = QLabel(self.frame_45)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)


        self.gridLayout_5.addWidget(self.frame_45, 0, 1, 1, 1)

        self.tableWidget_main = QTableWidget(self.frame_12)
        self.tableWidget_main.setObjectName(u"tableWidget_main")
        self.tableWidget_main.setMinimumSize(QSize(0, 0))
        self.tableWidget_main.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(12)
        self.tableWidget_main.setFont(font4)
        self.tableWidget_main.setStyleSheet(u"QTableView {\n"
"  	\n"
"}\n"
"QHeaderView::section{\n"
"background-color:  #ffa31a;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"background-color: #ffa31a; }\n"
"\n"
"QTableView::indicator:unchecked {\n"
"   \n"
"	background-color: rgb(170, 170, 255);\n"
"}")
        self.tableWidget_main.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_main.setShowGrid(True)
        self.tableWidget_main.setGridStyle(Qt.DashLine)
        self.tableWidget_main.horizontalHeader().setVisible(True)
        self.tableWidget_main.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_main.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_main.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_main.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.tableWidget_main, 1, 0, 1, 2)


        self.gridLayout_17.addWidget(self.frame_12, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_22 = QGridLayout(self.tab_3)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.tabWidget_3 = QTabWidget(self.tab_3)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setDocumentMode(False)
        self.tabWidget_3.setTabBarAutoHide(False)
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_16 = QGridLayout(self.tab_12)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_19 = QFrame(self.tab_12)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_19)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(2, 0, 0, 0)
        self.checkBox_new_folder = QCheckBox(self.frame_19)
        self.checkBox_new_folder.setObjectName(u"checkBox_new_folder")
        self.checkBox_new_folder.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_20.addWidget(self.checkBox_new_folder, 4, 0, 1, 1)

        self.label_image = QLabel(self.frame_19)
        self.label_image.setObjectName(u"label_image")

        self.gridLayout_20.addWidget(self.label_image, 1, 0, 1, 1)

        self.label_8 = QLabel(self.frame_19)
        self.label_8.setObjectName(u"label_8")
        font5 = QFont()
        font5.setPointSize(12)
        self.label_8.setFont(font5)

        self.gridLayout_20.addWidget(self.label_8, 0, 0, 1, 1)

        self.pushButton_clear_exif = QPushButton(self.frame_19)
        self.pushButton_clear_exif.setObjectName(u"pushButton_clear_exif")
        self.pushButton_clear_exif.setStyleSheet(u"")

        self.gridLayout_20.addWidget(self.pushButton_clear_exif, 3, 0, 1, 1)

        self.tableWidget_image_analyz = QTableWidget(self.frame_19)
        self.tableWidget_image_analyz.setObjectName(u"tableWidget_image_analyz")
        self.tableWidget_image_analyz.setMaximumSize(QSize(16777215, 13212312))
        self.tableWidget_image_analyz.setStyleSheet(u"QTableView {\n"
"  	\n"
"}\n"
"QHeaderView::section{\n"
"background-color:  #ffa31a;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"background-color: #ffa31a; }\n"
"\n"
"QTableView::indicator:unchecked {\n"
"   \n"
"	background-color: rgb(170, 170, 255);\n"
"}")
        self.tableWidget_image_analyz.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_image_analyz.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_image_analyz.verticalHeader().setVisible(False)
        self.tableWidget_image_analyz.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_image_analyz.verticalHeader().setStretchLastSection(False)

        self.gridLayout_20.addWidget(self.tableWidget_image_analyz, 2, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_19, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_28 = QGridLayout(self.tab_13)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.frame_20 = QFrame(self.tab_13)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_37 = QGridLayout(self.frame_20)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.gridLayout_37.setContentsMargins(6, 0, -1, 0)
        self.frame_25 = QFrame(self.frame_20)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.WinPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_25)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_33.setVerticalSpacing(17)
        self.gridLayout_33.setContentsMargins(-1, 2, -1, 6)
        self.label_35 = QLabel(self.frame_25)
        self.label_35.setObjectName(u"label_35")

        self.gridLayout_33.addWidget(self.label_35, 2, 1, 1, 1)

        self.label_34 = QLabel(self.frame_25)
        self.label_34.setObjectName(u"label_34")

        self.gridLayout_33.addWidget(self.label_34, 0, 1, 1, 1)

        self.lineEdit_anal_region = QLineEdit(self.frame_25)
        self.lineEdit_anal_region.setObjectName(u"lineEdit_anal_region")

        self.gridLayout_33.addWidget(self.lineEdit_anal_region, 0, 2, 1, 1)

        self.lineEdit_anal_nisha = QLineEdit(self.frame_25)
        self.lineEdit_anal_nisha.setObjectName(u"lineEdit_anal_nisha")

        self.gridLayout_33.addWidget(self.lineEdit_anal_nisha, 2, 2, 1, 1)

        self.radioButton_search = QRadioButton(self.frame_25)
        self.radioButton_search.setObjectName(u"radioButton_search")
        self.radioButton_search.setChecked(True)

        self.gridLayout_33.addWidget(self.radioButton_search, 0, 0, 1, 1)


        self.gridLayout_37.addWidget(self.frame_25, 1, 0, 1, 1)

        self.label_18 = QLabel(self.frame_20)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_37.addWidget(self.label_18, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame_20)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_2)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.pushButton_analyz_con = QPushButton(self.frame_2)
        self.pushButton_analyz_con.setObjectName(u"pushButton_analyz_con")
        self.pushButton_analyz_con.setEnabled(True)
        self.pushButton_analyz_con.setStyleSheet(u"")

        self.gridLayout_21.addWidget(self.pushButton_analyz_con, 0, 3, 1, 1)

        self.pushButton_analyz = QPushButton(self.frame_2)
        self.pushButton_analyz.setObjectName(u"pushButton_analyz")
        self.pushButton_analyz.setEnabled(True)
        self.pushButton_analyz.setStyleSheet(u"")

        self.gridLayout_21.addWidget(self.pushButton_analyz, 0, 2, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(150, 16777215))

        self.gridLayout_21.addWidget(self.label_4, 0, 0, 1, 1)

        self.spinBox_anal = QSpinBox(self.frame_2)
        self.spinBox_anal.setObjectName(u"spinBox_anal")
        self.spinBox_anal.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_21.addWidget(self.spinBox_anal, 0, 1, 1, 1)


        self.gridLayout_37.addWidget(self.frame_2, 7, 0, 1, 1)

        self.frame_26 = QFrame(self.frame_20)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setEnabled(True)
        self.frame_26.setMinimumSize(QSize(747, 0))
        self.frame_26.setFrameShape(QFrame.WinPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_26)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.label_38 = QLabel(self.frame_26)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(130, 0))

        self.gridLayout_36.addWidget(self.label_38, 0, 1, 1, 1)

        self.radioButton_url = QRadioButton(self.frame_26)
        self.radioButton_url.setObjectName(u"radioButton_url")
        self.radioButton_url.setMaximumSize(QSize(16, 16777215))

        self.gridLayout_36.addWidget(self.radioButton_url, 0, 0, 1, 1)

        self.lineEdit_anal_url = QLineEdit(self.frame_26)
        self.lineEdit_anal_url.setObjectName(u"lineEdit_anal_url")
        self.lineEdit_anal_url.setEnabled(False)
        self.lineEdit_anal_url.setMinimumSize(QSize(747, 0))
        self.lineEdit_anal_url.setMaximumSize(QSize(4343543, 16777215))

        self.gridLayout_36.addWidget(self.lineEdit_anal_url, 0, 2, 1, 1)


        self.gridLayout_37.addWidget(self.frame_26, 2, 0, 1, 1)

        self.tableWidget_analyz = QTableWidget(self.frame_20)
        self.tableWidget_analyz.setObjectName(u"tableWidget_analyz")
        self.tableWidget_analyz.setMinimumSize(QSize(0, 0))
        self.tableWidget_analyz.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_analyz.setFont(font4)
        self.tableWidget_analyz.setStyleSheet(u"QTableView {\n"
"  	\n"
"}\n"
"QHeaderView::section{\n"
"background-color:  #ffa31a;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"background-color: #ffa31a; }\n"
"\n"
"QTableView::indicator:unchecked {\n"
"   \n"
"	background-color: rgb(170, 170, 255);\n"
"}")
        self.tableWidget_analyz.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_analyz.setShowGrid(True)
        self.tableWidget_analyz.setGridStyle(Qt.DashLine)
        self.tableWidget_analyz.horizontalHeader().setVisible(True)
        self.tableWidget_analyz.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_analyz.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_analyz.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_analyz.verticalHeader().setStretchLastSection(False)

        self.gridLayout_37.addWidget(self.tableWidget_analyz, 6, 0, 1, 1)


        self.gridLayout_28.addWidget(self.frame_20, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.gridLayout_32 = QGridLayout(self.tab_14)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.frame_24 = QFrame(self.tab_14)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_24)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.gridLayout_30.setContentsMargins(7, 0, 0, 0)
        self.label_29 = QLabel(self.frame_24)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_30.addWidget(self.label_29, 0, 0, 1, 1)

        self.tableWidget_image_drive = QTableWidget(self.frame_24)
        self.tableWidget_image_drive.setObjectName(u"tableWidget_image_drive")
        self.tableWidget_image_drive.setMaximumSize(QSize(16777215, 13212312))
        self.tableWidget_image_drive.setStyleSheet(u"QTableView {\n"
"  	\n"
"}\n"
"QHeaderView::section{\n"
"background-color:  #ffa31a;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"background-color: #ffa31a; }\n"
"\n"
"QTableView::indicator:unchecked {\n"
"   \n"
"	background-color: rgb(170, 170, 255);\n"
"}")
        self.tableWidget_image_drive.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_image_drive.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_image_drive.verticalHeader().setVisible(True)
        self.tableWidget_image_drive.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_image_drive.verticalHeader().setStretchLastSection(True)

        self.gridLayout_30.addWidget(self.tableWidget_image_drive, 2, 0, 1, 1)

        self.label_image_drive = QLabel(self.frame_24)
        self.label_image_drive.setObjectName(u"label_image_drive")

        self.gridLayout_30.addWidget(self.label_image_drive, 1, 0, 1, 1)

        self.textBrowser_drive = QTextBrowser(self.frame_24)
        self.textBrowser_drive.setObjectName(u"textBrowser_drive")
        self.textBrowser_drive.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_30.addWidget(self.textBrowser_drive, 2, 1, 1, 1)

        self.pushButton_add_drive_excel = QPushButton(self.frame_24)
        self.pushButton_add_drive_excel.setObjectName(u"pushButton_add_drive_excel")
        self.pushButton_add_drive_excel.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.pushButton_add_drive_excel, 3, 0, 1, 1)

        self.pushButton_add_drive = QPushButton(self.frame_24)
        self.pushButton_add_drive.setObjectName(u"pushButton_add_drive")
        self.pushButton_add_drive.setStyleSheet(u"")

        self.gridLayout_30.addWidget(self.pushButton_add_drive, 3, 1, 1, 1)


        self.gridLayout_32.addWidget(self.frame_24, 0, 0, 1, 1)

        self.tabWidget_3.addTab(self.tab_14, "")

        self.gridLayout_22.addWidget(self.tabWidget_3, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_3 = QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.tab_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableWidget_proxy = QTableWidget(self.frame)
        self.tableWidget_proxy.setObjectName(u"tableWidget_proxy")
        self.tableWidget_proxy.setMinimumSize(QSize(0, 0))
        self.tableWidget_proxy.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget_proxy.setFont(font4)
        self.tableWidget_proxy.setStyleSheet(u"QTableView {\n"
"  	\n"
"}\n"
"QHeaderView::section{\n"
"background-color:  #ffa31a;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QTableCornerButton::section {\n"
"background-color: #ffa31a; }\n"
"\n"
"QTableView::indicator:unchecked {\n"
"   \n"
"	background-color: rgb(170, 170, 255);\n"
"}")
        self.tableWidget_proxy.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_proxy.setShowGrid(True)
        self.tableWidget_proxy.setGridStyle(Qt.DashLine)
        self.tableWidget_proxy.horizontalHeader().setVisible(True)
        self.tableWidget_proxy.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_proxy.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_proxy.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_proxy.verticalHeader().setStretchLastSection(True)

        self.gridLayout_6.addWidget(self.tableWidget_proxy, 0, 0, 1, 1)

        self.frame_17 = QFrame(self.frame)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_17)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_37 = QLabel(self.frame_17)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_2.addWidget(self.label_37, 1, 4, 1, 1)

        self.comboBox_proxy = QComboBox(self.frame_17)
        self.comboBox_proxy.setObjectName(u"comboBox_proxy")
        self.comboBox_proxy.setMinimumSize(QSize(145, 0))
        self.comboBox_proxy.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.comboBox_proxy, 2, 1, 1, 1)

        self.label_24 = QLabel(self.frame_17)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_2.addWidget(self.label_24, 1, 2, 1, 1)

        self.label_21 = QLabel(self.frame_17)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_2.addWidget(self.label_21, 2, 4, 1, 1)

        self.label_23 = QLabel(self.frame_17)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_2.addWidget(self.label_23, 2, 0, 1, 1)

        self.lineEdit_data_proxy3 = QLineEdit(self.frame_17)
        self.lineEdit_data_proxy3.setObjectName(u"lineEdit_data_proxy3")

        self.gridLayout_2.addWidget(self.lineEdit_data_proxy3, 2, 3, 1, 1)

        self.label_20 = QLabel(self.frame_17)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_2.addWidget(self.label_20, 1, 0, 1, 1)

        self.lineEdit_data_proxy1 = QLineEdit(self.frame_17)
        self.lineEdit_data_proxy1.setObjectName(u"lineEdit_data_proxy1")

        self.gridLayout_2.addWidget(self.lineEdit_data_proxy1, 1, 1, 1, 1)

        self.lineEdit_data_proxy5 = QLineEdit(self.frame_17)
        self.lineEdit_data_proxy5.setObjectName(u"lineEdit_data_proxy5")

        self.gridLayout_2.addWidget(self.lineEdit_data_proxy5, 2, 5, 1, 1)

        self.pushButton_add_proxy = QPushButton(self.frame_17)
        self.pushButton_add_proxy.setObjectName(u"pushButton_add_proxy")
        self.pushButton_add_proxy.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pushButton_add_proxy, 0, 6, 2, 1)

        self.label_26 = QLabel(self.frame_17)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 2, 2, 1, 1)

        self.pushButton_remove_proxy = QPushButton(self.frame_17)
        self.pushButton_remove_proxy.setObjectName(u"pushButton_remove_proxy")
        self.pushButton_remove_proxy.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.pushButton_remove_proxy, 2, 6, 1, 1)

        self.lineEdit_data_proxy2 = QLineEdit(self.frame_17)
        self.lineEdit_data_proxy2.setObjectName(u"lineEdit_data_proxy2")

        self.gridLayout_2.addWidget(self.lineEdit_data_proxy2, 1, 3, 1, 1)

        self.lineEdit_data_proxy4 = QLineEdit(self.frame_17)
        self.lineEdit_data_proxy4.setObjectName(u"lineEdit_data_proxy4")

        self.gridLayout_2.addWidget(self.lineEdit_data_proxy4, 0, 5, 2, 1)


        self.gridLayout_6.addWidget(self.frame_17, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_13 = QGridLayout(self.tab_10)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.plainTextEdit = QPlainTextEdit(self.tab_10)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 1666))
        self.plainTextEdit.setFont(font4)
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(71, 71, 71);\n"
"color: rgb(255, 255, 255);")
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_13.addWidget(self.plainTextEdit, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_10, "")

        self.gridLayout_31.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.checkBox_browser = QCheckBox(MainWindow)
        self.checkBox_browser.setObjectName(u"checkBox_browser")
        self.checkBox_browser.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.checkBox_browser.setChecked(True)

        self.gridLayout_31.addWidget(self.checkBox_browser, 3, 0, 1, 1)


        self.retranslateUi(MainWindow)
        self.tableWidget_main.cellClicked.connect(self.tableWidget_main.selectRow)
        self.tableWidget_proxy.cellClicked.connect(self.tableWidget_proxy.selectRow)

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Avitolog228", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:28pt; font-weight:700;\">Multitool</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:12pt;\">Avito</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:12pt;\">* \u0411\u0440\u0430\u0443\u0437\u0435\u0440"
                        " - \u2705 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:12pt;\">\u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u043e\u0432.\u0417\u0430\u043f\u0443\u0441\u043a, \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435, \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0430\u043a\u043a\u0430\u0443\u043d\u0442\u043e\u0432.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:12pt;\">* \u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b - \u2705 "
                        "\u2757\ufe0f</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:12pt;\">** \u041e\u0447\u0438\u0441\u0442\u043a\u0430 \u0444\u043e\u0442\u043e \u043e\u0442 \u043c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0445\u2705</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:12pt;\">** \u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0441\u0441\u044b\u043b\u043e\u043a \u043d\u0430 Google drive + \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0438\u0445 \u0432 Excel\u2705\u2757\ufe0f</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:12pt;\">** \u0410\u043d\u0430\u043b\u0438\u0437 \u2705"
                        "\u2757\ufe0f</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:12pt;\">*** \u0410\u043d\u0430\u043b\u0438\u0437 \u043f\u043b\u0430\u0442\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433 \u2705 \u2757</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:12pt;\">*** \u0410\u043d\u0430\u043b\u0438\u0437 \u0432\u044b\u0434\u0430\u0447\u0438 \u2705  \u2757\ufe0f</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; fo"
                        "nt-size:12pt;\">* \u0411\u0430\u0437\u0430 \u0414\u0430\u043d\u043d\u044b\u0445 \u0411\u043e\u0442\u043e\u0432 - \u2705 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:12pt;\">** \u0411\u0430\u0437\u0430 \u0434\u0430\u043d\u043d\u044b\u0445 \u043f\u0440\u043e\u043a\u0441\u0438 \u2705 </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Courier New'; font-size:12pt;\">* \u041b\u043e\u0433\u0438 - \u2705 </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New'; font-size:"
                        "12pt;\"><br /></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><pre style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New';\"><br/></pre></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><pre style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New';\"><br/></pre></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><pre style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Courier New';\"><br/></pre></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0441\u0442\u0438\u0442\u044c \u0430\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u043a\u0430\u0443\u043d\u0442", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043a\u0441\u0438", None))
        self.pushButton_start_login.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442", None))
        self.pushButton_add_data.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.pushButton_delete_data.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_update_data.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.label_3.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u0411\u0440\u0430\u0443\u0437\u0435\u0440", None))
        self.checkBox_new_folder.setText(QCoreApplication.translate("MainWindow", u"\u0412 \u043d\u043e\u0432\u043e\u0439 \u043f\u0430\u043f\u043a\u0435", None))
        self.label_image.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043e \u043a\u0430\u0440\u0442\u0438\u043d\u043e\u043a : 0", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">\u041e\u0447\u0438\u0441\u0442\u043a\u0430 \u043c\u0435\u0442\u0430\u0434\u0430\u043d\u043d\u044b\u0445 </span></p></body></html>", None))
        self.pushButton_clear_exif.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0444\u043e\u0442\u043e", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u043a\u0430 \u0444\u043e\u0442\u043e", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0438\u043e\u043d", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a\u043e\u0432\u043e\u0439 \u0437\u0430\u043f\u0440\u043e\u0441", None))
        self.lineEdit_anal_region.setText("")
        self.lineEdit_anal_nisha.setText("")
        self.radioButton_search.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">\u0410\u043d\u0430\u043b\u0438\u0437 \u043d\u0438\u0448\u0438</span></p></body></html>", None))
        self.pushButton_analyz_con.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.pushButton_analyz.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437 \u043f\u043b\u0430\u0442\u043d\u044b\u0445 \u0443\u0441\u043b\u0443\u0433", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u0442\u0440\u0430\u043d\u0438\u0446", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Url \u0437\u0430\u043f\u0440\u043e\u0441", None))
        self.radioButton_url.setText("")
        self.lineEdit_anal_url.setText("")
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:700;\">\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0444\u043e\u0442\u043e \u0432 Google Drive (\u0434\u043b\u044f \u043c\u0430\u0441\u0441\u043f\u043e\u0441\u0442\u0438\u043d\u0433\u0430 XML)</span></p></body></html>", None))
        self.label_image_drive.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043e \u043a\u0430\u0440\u0442\u0438\u043d\u043e\u043a : 0", None))
        self.pushButton_add_drive_excel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u0444\u043e\u0442\u043e + Excel", None))
        self.pushButton_add_drive.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0433\u0440\u0443\u0437\u043a\u0430 \u0444\u043e\u0442\u043e", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Google Drive", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d \u0430\u0432\u0438\u0442\u043e", None))
        self.pushButton_add_proxy.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043f\u0440\u043e\u043a\u0441\u0438", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0440\u0442", None))
        self.pushButton_remove_proxy.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u043f\u0440\u043e\u043a\u0441\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043a\u0441\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438", None))
        self.checkBox_browser.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0431\u0440\u0430\u0443\u0437\u0435\u0440", None))
    # retranslateUi

