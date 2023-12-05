import time
import unittest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from demoqa_com.pages.basepage import BasePage


class TestDatepicker(unittest.TestCase, BasePage):
    LINK = 'https://demoqa.com/date-picker'
    select_date_locator = (By.XPATH, '//*[@id="datePickerMonthYearInput"]')
    day_select = (By.XPATH, '//div[@aria-label="Choose Tuesday, January 19th, 2010"]')
    month_select = (By.XPATH, '//select[@class="react-datepicker__month-select"]')
    year_select = (By.XPATH, '//select[@class="react-datepicker__year-select"]')

    date_and_time_locator = (By.ID, 'dateAndTimePickerInput')
    year_second_selec = (By.CLASS_NAME, 'react-datepicker__month-read-view--selected-month')

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
        self.click(self.select_date_locator)
        time.sleep(1)
        Select(self.find(self.year_select)).select_by_value('2010')
        Select(self.find(self.month_select)).select_by_value('0')
        self.click(self.day_select)
        self.assertEqual('01/19/2010', self.find(self.select_date_locator).get_attribute('value'))
        time.sleep(2)

    def test_date_and_time_with_send_keys(self):
        self.find(self.date_and_time_locator).send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        self.type(self.date_and_time_locator, 'December 1, 2023 8:00 AM')
        time.sleep(2)
        self.assertEqual('December 1, 2023 8:00 AM', self.find(self.date_and_time_locator).get_attribute('value'),
                         'Not Expected Response !')
        print(self.find(self.date_and_time_locator).get_attribute('value'))

