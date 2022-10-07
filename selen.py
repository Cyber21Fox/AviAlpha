import time
import config
import sqlite3
import random
import threading
import traceback
import datetime
import logging as log

from selenium import webdriver
from user_agent import generate_navigator
from selenium_stealth import stealth
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem, QTabWidget, QFileDialog
from multiprocessing.dummy import Pool as ThreadPool
import chromedriver_autoinstaller as chromedriver
import chromedriver_binary
#chromedriver.install()
path_driver = "driver\chromedriver.exe"
import undetected_chromedriver as uc

class Browser():
    def __init__(self, parent):
        self.ui = parent
        self.locker = threading.Lock()
        self.connection = sqlite3.connect('sqlite_python.db', check_same_thread=False)
        self.cursor = self.connection.cursor()

    def start_browser(self, login):
        try:
            self.ui.tabWidget.setCurrentIndex(1)
            chrome_options = webdriver.ChromeOptions()
            if not self.ui.checkBox_browser.isChecked():
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--blink-settings=imagesEnabled=false')
            """
            if not self.ui.checkBox_gpu.isChecked():
                chrome_options.add_argument("--disable-gpu")
            if not self.ui.checkBox_js.isChecked():
                chrome_options.add_argument("--disable-javascript")
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--dns-prefetch-disable")
            chrome_options.add_argument("--disable-bundled-ppapi-flash")
            chrome_options.add_argument("--disable-plugins-discovery")
            chrome_options.add_argument("--disable-javascript")
            chrome_options.add_argument('--lang=ru-RU')
            chrome_options.add_extension(f"web.crx")
            chrome_options.add_extension(f"ghost.crx")"""
            #chrome_options.add_extension(f"extensions/adb.crx")
            log.info("Запуск браузера")
            # если логин есть
            if login is not None:
                if self.ui.comboBox_proxy_browser.currentText() != "Без прокси":
                    proxy = self.cursor.execute(f"SELECT * FROM  db_proxy WHERE ip = '{self.ui.comboBox_proxy_browser.currentText()}'").fetchone()
                    chrome_options.add_argument(f"--proxy-server={proxy[1]}://{proxy[2]}:{proxy[3]}")
                infor = self.cursor.execute(f"SELECT * FROM  db_info_os WHERE login_avito = '{login}'").fetchone()
                #width, height = infor[6].split(':')
                chrome_options.add_argument(f"--user-agent={infor[5]}")
                #chrome_options.add_argument(f"--window-size={width},{height}")
                #chrome_options.add_argument(f'--platformName={infor[2]}')
                driver = uc.Chrome(options=chrome_options)
                stealth(driver,
                        languages=["ru-RU"],
                        vendor=infor[1],
                        platform=infor[2],
                        webgl_vendor=infor[3],
                        renderer=infor[4],
                        fix_hairline=True,
                        run_on_insecure_origins=True
                        )
            else:
                # width, height = random.choice(config.width_height).split(':')
                # chrome_options.add_argument(f"--window-size={width}x{height}")
                chrome_options.add_experimental_option('useAutomationExtension', False)
                info_navigator = generate_navigator(navigator='chrome', device_type= "desktop")
                chrome_options.add_argument(f"user-agent={info_navigator['user_agent']}")
                chrome_options.add_argument(f'--platformName={info_navigator["platform"]}')
                driver = webdriver.Chrome(options=chrome_options)
                stealth(driver,
                        languages=["ru-RU"],
                        vendor=info_navigator['vendor'],
                        platform=info_navigator["platform"],
                        webgl_vendor=random.choice(config.vendor),
                        renderer=random.choice(config.renderer_NVIDIA),
                        fix_hairline=True,
                        )
            driver.implicitly_wait(5)
            #driver.get("http://f.vision/")
            #time.sleep(5342)
            return driver
        except Exception as exe:
            log.info(f'Произошла ошибка: {exe}', traceback.format_exc())
            QMessageBox.critical(self, "Ошибка ", "Проблема при подключении бразера", QMessageBox.Ok)
            driver.close()
            driver.quit()

    # запуск браузера для регистрации
    def update_test_cookies(self, login, driver):
        try:
            log.info("Получение тестовых cookies")
            driver.get('https://avito.ru/')
            time.sleep(random.randint(2, 5))
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='#login?authsrc=h']")))
            self.cursor.execute("""INSERT INTO db_cookies(login_avito, cookies, created) VALUES(?,?,?)""",
                                [f"{login}-test", str(driver.get_cookies()), datetime.datetime.now().date()])
            self.connection.commit()
            log.info("Тестовые cookies сохранены")
        except Exception as exe:
            print(f'Произошла ошибка: {exe}', traceback.format_exc())
            QMessageBox.critical(self, "Ошибка ", "Проблема при получении cookies", QMessageBox.Ok)

    # авторизация в акке
    def authorization(self, login, passw):
        try:
            self.ui.tabWidget.setCurrentIndex(1)
            log.info("Загрузка тестовых cookies")
            driver = self.start_browser(login)
            driver.delete_all_cookies()
            # загрузить куки с аккаунта если есть
            log.info("Получение cookies")
            records = self.cursor.execute(f"SELECT * FROM  db_cookies WHERE login_avito = {login} ORDER BY created DESC LIMIT 1").fetchone()
            # если нет то сделать тестовые , войти в акк и записать новые
            #date_cookies = datetime.date(day=int(records[2][-2:]), month=int(records[2][5:-3]), year=int(records[2][:4]))
            #date2_cookies = str(datetime.datetime.now().date() - date_cookies)
            #if records is None or (int(str(datetime.datetime.now().date() - (datetime.date(day=int(records[2][-2:]), month=int(records[2][5:-3]), year=int(records[2][:4]))))[:2]) >= 14):
            if records is None:
                self.cursor.execute(f"""DELETE FROM db_cookies WHERE login_avito = '{login}'""")
                self.connection.commit()
                log.info(f"Cookies для {login} нет, создаются новые")
                test_cookies = self.cursor.execute(f"SELECT * FROM  db_cookies WHERE login_avito = '{login}-test'").fetchone()
                if test_cookies is None:
                    self.update_test_cookies(login, driver)
                    test_cookies = self.cursor.execute(f"SELECT * FROM  db_cookies WHERE login_avito = '{login}-test'").fetchone()
                for cookie in eval(test_cookies[1]):
                    driver.add_cookie(cookie)
                time.sleep(random.randint(1, 2))
                driver.get('https://avito.ru/')
                time.sleep(random.randint(2, 3))
                driver.get('https://avito.ru/#login?authsrc=h')
                time.sleep(random.randint(2, 3))
                log.info(f"Вход в аккаунт {login}")
                login_find = driver.find_element(By.NAME, "login")
                login_find.send_keys(login)
                passw_find = driver.find_element(By.NAME, "password")
                passw_find.send_keys(passw)
                action = ActionChains(driver)
                action.move_to_element(driver.find_element(By.XPATH, "//button[@class='button-button-GQPRe button-size-m-DEqBY button-primary-cF3Rr width-width-12-he_88']")).click().perform()
                time.sleep(25)
            else:
                log.info(f"Cookies для {login} есть")
                driver.get('https://avito.ru/')
                for cookie in eval(records[1]):
                    driver.add_cookie(cookie)
                #if (int(str(datetime.datetime.now().date() - (datetime.date(day=int(records[2][-2:]), month=int(records[2][5:-3]), year=int(records[2][:4]))))[:2]) >= 4):
                #self.cursor.execute(f"""DELETE FROM db_cookies WHERE cookies = '{records[2]}'""")
                time.sleep(random.randint(1, 2))
                driver.refresh()
            time.sleep(random.randint(4, 6))
            self.cursor.execute("""INSERT INTO db_cookies(login_avito, cookies, created) VALUES(?,?,?)""",
                                [login, str(driver.get_cookies()), datetime.datetime.now().date()])
            self.connection.commit()
            return driver
        except Exception as exe:
            print(f'Произошла ошибка: {exe}', traceback.format_exc())
            QMessageBox.critical(self, "Ошибка ", "Проблема при входе в аккаунт", QMessageBox.Ok)

    def get_info_profile(self, login, password, driver):
        try:
            time.sleep(3)
            WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, f'js-profile-sidebar-navigation')))
            data_profile = eval(driver.find_element(By.CLASS_NAME, f'js-profile-sidebar-navigation').get_attribute("data-props"))
            print(data_profile)
            name = data_profile.get("user").get('name')
            email = data_profile.get("user").get('email')
            balance = data_profile.get("userAccount").get('balance').get('real')
            status = True
            self.cursor.execute("""INSERT INTO db_profile(name, email, number, pass, balance, status) VALUES(?,?,?,?,?,?)""",
                                    [name, email, login, password, balance, status])
            self.connection.commit()
            time.sleep(500)
            log.info(f'Профиль {login} успешно добавлен')
            # получить значениякол объявлений
        except:
            pass

    def create_ad_for_profile(self):
        data = self.cursor.execute(f"SELECT * FROM db_profile_bot WHERE number = '{self.ui.comboBox_bot.currentText()}'").fetchall()
        print(list(data))
        driver = self.authorization(data[0][2], data[0][3])
        # number_acc in range(self.ui.spinBox.value()):
