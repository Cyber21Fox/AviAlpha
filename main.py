import os
import selen
import sys
import time
import math
import config
import sqlite3
import random
import traceback
import tools
from qt.add_profile import Ui_Widget
from exif import Image
import logging as log
from qt.form import Ui_MainWindow
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem, QTabWidget, QFileDialog ,QHeaderView
from PySide6.QtCore import QObject, QRunnable, Qt, QThreadPool
from PySide6 import QtGui, QtCore
from multiprocessing.dummy import Pool as ThreadPool
from PySide6.QtCore import QObject, QThread, Signal, Slot
from user_agent import generate_navigator
from PIL import Image

# хэндлер логер
class Logger(log.Handler):
    def __init__(self, parent):
        super().__init__()
        self.widget = parent.plainTextEdit
        self.widget.setReadOnly(True)

    def emit(self, record):
        msg = self.format(record)
        self.widget.appendPlainText(msg)


class AddProfile(QWidget):
    def __init__(self):
        super(AddProfile, self).__init__()
        self.ad = Ui_Widget()
        self.ad.setupUi(self)
        try:
            self.connection = sqlite3.connect('sqlite_python.db', check_same_thread=False)
            self.cursor = self.connection.cursor()
            log.info(f"База данных успешно подключена!")
        except:
            log.error(f"Не удалось подключится к БД!")
        self.ad.comboBox_os.addItems([*config.os])
        self.change_os()
        self.change_vendor()
        self.ad.comboBox_os.currentTextChanged.connect(self.change_os)
        self.ad.comboBox_webgl.currentTextChanged.connect(self.change_vendor)
        self.ad.pushButton_add_profile.clicked.connect(self.add_profile)

    def change_os(self):
        self.ad.comboBox_webgl.clear()
        if self.ad.comboBox_os.currentText() == 'MacOS':
            self.ad.comboBox_webgl.addItems(["Apple"])
        else:
            self.ad.comboBox_webgl.addItems(config.vendor)

    def change_vendor(self):
        vendor = self.ad.comboBox_webgl.currentText()
        self.ad.comboBox_render.clear()
        if vendor == "Apple":
            self.ad.comboBox_render.addItems(config.renderer_Apple)
        if vendor == "Intel Inc.":
            self.ad.comboBox_render.addItems(config.renderer_Intel)
        if vendor == "AMD":
            self.ad.comboBox_render.addItems(config.renderer_AMD)
        if vendor == "NVIDIA Corporation":
            self.ad.comboBox_render.addItems(config.renderer_NVIDIA)
        if vendor == "ATI Technologies Inc":
            self.ad.comboBox_render.addItems(config.renderer_ATI)

    def add_profile(self):
        os = self.ad.comboBox_os.currentText()
        login = self.ad.lineEdit_profile_login.text()
        password = self.ad.lineEdit_profile_pass.text()

        self.cursor.execute("""INSERT INTO db_profile(name, number, pass) VALUES(?,?,?)""",
                          [self.ad.lineEdit_profile_name.text(), login, password])
        self.connection.commit()

        info_navigator = generate_navigator(navigator='chrome', device_type="desktop", os=config.os[os])
        self.cursor.execute(
            """INSERT INTO db_info_os(login_avito, vendor, platform, webgl_vendor, renderer, user_agent, width_height)
            VALUES(?,?,?,?,?,?,?)""",
            [login, info_navigator['vendor'], os, self.ad.comboBox_webgl.currentText(),
             self.ad.comboBox_render.currentText(), info_navigator['user_agent'], random.choice(config.width_height)])
        self.connection.commit()
        log.info(f'Профиль {login} успешно добавлен')
        self.close()


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # логи
        logTextBox = Logger(self.ui)
        logTextBox.setFormatter(log.Formatter('[%(asctime)s] [%(levelname)s]: %(message)s'))
        log.getLogger().addHandler(logTextBox)
        log.getLogger().setLevel(log.INFO)

        # подключение БД
        self.connection = sqlite3.connect('sqlite_python.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        log.info(f"База данных успешно подключена!")

        # создание потоков
        self.browser = selen.Browser(self.ui)
        self.buildform = BuildForm(self.ui, self.connection, self.cursor)
        self.tool = tools.Tools(self.ui)

        self.profile = Profile(self.ui, self.connection, self.cursor)
        self.proxy = Proxy(self.ui, self.connection, self.cursor)
        #log.info(f'Старт {threading.current_thread().name}')

        # заполнение форм
        self.buildform.path_combo_browser_with_login()
        self.ui.comboBox_proxy.addItems(config.type_proxy)
        self.profile.write_tablewidget()
        self.proxy.write_tableproxy()

        # анализ
        self.ui.pushButton_clear_exif.clicked.connect(self.clear_metadata)
        self.ui.pushButton_analyz_con.clicked.connect(self.tool.analysis_competitor)
        self.ui.pushButton_add_drive.clicked.connect(self.tool.add_image_drive)
        self.ui.pushButton_analyz.clicked.connect(self.tool.analysis)
        self.ui.pushButton_add_drive_excel.clicked.connect(self.tool.dir_imageTo_exel_google)

        # браузер
        self.ui.pushButton_start_login.clicked.connect(self.start_browser_with_login)
        self.ui.pushButton_add_data.clicked.connect(self.profile.add_profile)
        self.ui.pushButton_delete_data.clicked.connect(self.profile.remove_profile)
        self.ui.pushButton_update_data.clicked.connect(self.profile.write_tablewidget)

        # прокси
        self.ui.pushButton_add_proxy.clicked.connect(self.proxy.add_proxy)
        self.ui.pushButton_remove_proxy.clicked.connect(self.proxy.remove_proxy)

        # галочки
        self.ui.radioButton_search.clicked.connect(self.clicked_search)
        self.ui.radioButton_url.clicked.connect(self.clicked_url)

    def clicked_search(self):
        self.ui.radioButton_url.toggle()
        if self.ui.radioButton_search.isChecked():
            self.ui.lineEdit_anal_url.setDisabled(1)
            self.ui.lineEdit_anal_nisha.setEnabled(1)
            self.ui.lineEdit_anal_region.setEnabled(1)

    def clicked_url(self):
        self.ui.radioButton_search.toggle()
        if self.ui.radioButton_url.isChecked():
            self.ui.lineEdit_anal_url.setEnabled(1)
            self.ui.lineEdit_anal_nisha.setDisabled(1)
            self.ui.lineEdit_anal_region.setDisabled(1)

    def clear_metadata(self):
        file, _ = QFileDialog.getOpenFileNames(self, 'Open File', './', "Image (*.png *.jpg *jpeg)")  # file путь до файла
        self.ui.tableWidget_image_analyz.setColumnCount(10)
        self.ui.tableWidget_image_analyz.setRowCount(math.ceil(len(file)/10))
        self.ui.tableWidget_image_analyz.setIconSize(QtCore.QSize(100, 100))
        column = 0
        self.ui.label_image.setText(f"Выбрано картинок : {len(file)}")
        log.info(f"Для очистки выбрано картинок : {len(file)}")
        if self.ui.checkBox_new_folder.isChecked():
            i = 0
            for image_path in file:
                i += 1
                image_path_before = image_path[:image_path.rfind("/") + 1]
                new_path = f'{image_path_before}new_image'
                if not os.path.exists(new_path):
                    os.makedirs(new_path)
                image = Image.open(image_path)
                rgb_im = image.convert('RGB')
                #data = list(image.getdata())
                #image_without_exif = Image.new(image.mode, image.size)
                #image_without_exif.putdata(data)
                rgb_im.save(f'{new_path}/{i}.jpg')
                item = QTableWidgetItem()
                self.ui.tableWidget_image_analyz.setItem(0, column, item)
                item.setIcon(QtGui.QIcon(image_path))
                column += 1
        else:
            for image_path in file:
                image = Image.open(image_path)
                rgb_im = image.convert('RGB')
                data = list(image.getdata())
                rgb_im.save(image_path)
                item = QTableWidgetItem()
                self.ui.tableWidget_image_analyz.setItem(0, column, item)
                item.setIcon(QtGui.QIcon(image_path))
                column += 1
        log.info(f"Метаданые успешно очищены!")
        self.ui.progressBar.setValue(100)
        QMessageBox.information(self, "Успешно ",
                                "Очистка метаданных выполнена",
                                QMessageBox.Ok)
        self.ui.tableWidget_image_analyz.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget_image_analyz.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget_image_analyz.horizontalHeader().setMinimumSectionSize(0)


    def start_browser_with_login(self):
        login = self.ui.comboBox_login.currentText()
        passw = self.cursor.execute(f"SELECT * FROM  db_profile WHERE number = '{login}'").fetchone()[3]
        self.browser.authorization(login, passw)
        time.sleep(True)



class BuildForm():
    def __init__(self, parent, connection, cursor):
        self.ui = parent
        self.connection = connection
        self.cursor = cursor

    # при изменении комбобокса
    def path_combo_browser_with_login(self):

        name_list = []
        proxy_list = ["Без прокси"]
        self.ui.comboBox_login.clear()
        self.ui.comboBox_proxy_browser.clear()
        infor = self.cursor.execute(f"SELECT * FROM db_profile").fetchall()
        for i in infor:
            name_list.append(i[2])
        self.ui.comboBox_login.addItems([*name_list])

        infor = self.cursor.execute(f"SELECT * FROM db_proxy").fetchall()
        for i in infor:
            proxy_list.append(i[2])
            print(i[2])
        self.ui.comboBox_proxy_browser.addItems([*proxy_list])

class Profile():
    def __init__(self, parent, connection, cursor):
        self.ui = parent
        self.connection = connection
        self.cursor = cursor
        self.buildform = BuildForm(self.ui, self.connection, self.cursor)

    def add_profile(self):
        self.ada = AddProfile()
        self.ada.show()
        #Задержка в потоках
        time.sleep(10)
        self.write_tablewidget()
        self.buildform.path_combo_browser_with_login()

    def remove_profile(self):
        self.cursor.execute(f"""DELETE FROM db_profile WHERE name = '{self.ui.tableWidget_main.currentItem().text()}'""")
        self.connection.commit()
        self.write_tablewidget()

    def write_tablewidget(self):
        self.ui.tableWidget_main.setColumnCount(7)
        self.ui.tableWidget_main.setHorizontalHeaderLabels(
            ['Имя', 'Email', 'Номер', 'Пароль', 'Баланс', 'Объявления', 'Статус'])
        self.cursor.execute("SELECT * FROM  db_profile")
        records = self.cursor.fetchall()
        self.ui.tableWidget_main.setRowCount(len(records))
        rowPosition = self.ui.tableWidget_main.rowCount()
        colPosition = self.ui.tableWidget_main.columnCount()
        for row in range(rowPosition):
            for column in range(colPosition):
                self.ui.tableWidget_main.setItem(row, column, QTableWidgetItem(records[row][column]))
        self.ui.tableWidget_main.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget_main.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget_main.horizontalHeader().setMinimumSectionSize(0)

# доделать
class Proxy:
    def __init__(self, parent, connection, cursor):
        self.ui = parent
        self.connection = connection
        self.cursor = cursor

    def add_proxy(self):
        self.cursor.execute(
            """INSERT INTO db_proxy(login_avito, type, ip, port, login, password) VALUES(?,?,?,?,?,?)""",
            [self.ui.lineEdit_data_proxy1.text(), self.ui.comboBox_proxy.currentText(),
                self.ui.lineEdit_data_proxy2.text(), self.ui.lineEdit_data_proxy3.text(),
                self.ui.lineEdit_data_proxy4.text(), self.ui.lineEdit_data_proxy5.text()])
        self.connection.commit()
        log.info(f'Прокси для {self.ui.lineEdit_data_proxy1.text()} успешно добавлен')
        self.write_tableproxy()

    def remove_proxy(self):
        self.cursor.execute(f"""DELETE FROM db_proxy WHERE login_avito = '{self.ui.tableWidget_proxy.currentItem().text()}'""")
        self.connection.commit()
        self.write_tableproxy()

    def write_tableproxy(self):
        self.ui.tableWidget_proxy.setColumnCount(6)
        self.ui.tableWidget_proxy.setHorizontalHeaderLabels(
                ['Логин авито', 'Тип', 'IP', 'Порт', 'Логин прокси', 'Пароль'])
        self.cursor.execute("SELECT * FROM  db_proxy")
        records = self.cursor.fetchall()
        self.ui.tableWidget_proxy.setRowCount(len(records))
        rowPosition = self.ui.tableWidget_proxy.rowCount()
        colPosition = self.ui.tableWidget_proxy.columnCount()
        for row in range(rowPosition):
            for column in range(colPosition):
                self.ui.tableWidget_proxy.setItem(row, column, QTableWidgetItem(records[row][column]))
        self.ui.tableWidget_proxy.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget_proxy.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.tableWidget_proxy.horizontalHeader().setMinimumSectionSize(0)


if __name__ == "__main__":
    # app = QApplication([])
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())