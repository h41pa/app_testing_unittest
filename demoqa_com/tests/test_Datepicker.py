import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from demoqa_com.pages.basepage import BasePage


class TestDatepicker(unittest.TestCase, BasePage):
    LINK = 'https://demoqa.com/date-picker'
    select_date_locator = (By.XPATH, '//*[@id="datePickerMonthYearInput"]')

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_select_date_with_sned_keys(self):
        self.find(self.select_date_locator).send_keys(Keys.CONTROL, 'a')
        self.find(self.select_date_locator).send_keys(Keys.BACKSPACE)
        time.sleep(1)
        self.type(self.select_date_locator, '12/12/2023')
        self.assertEqual('12/12/2023', self.find(self.select_date_locator).get_attribute('value'),
                         'Not expected result')
        print(self.find(self.select_date_locator).get_attribute('value'))
        time.sleep(1)

    def test_select_date_using_select(self):

