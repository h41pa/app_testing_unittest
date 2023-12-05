import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from demoqa_com.pages.basepage import BasePage


class TestSelectable(unittest.TestCase, BasePage):
    URL = 'https://demoqa.com/selectable'
    selectable_list_locator = (By.ID, 'demo-tab-list')
    first_list = (By.XPATH, '//*[@id="verticalListContainer"]/li[1]')
    second_list = (By.XPATH, '//*[@id="verticalListContainer"]/li[2]')
    third_list = (By.XPATH, '//*[@id="verticalListContainer"]/li[3]')

    selectable_grid_locator = (By.ID, 'demo-tab-grid')
    one_selector = (By.XPATH, '//*[@id="row1"]/li[1]')
    five_selector = (By.XPATH, '//*[@id="row2"]/li[2]')
    seven_selector = (By.XPATH, '//*[@id="row3"]/li[1]')

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_selectable_grid_with_asctions(self):
        actions = ActionChains(self.driver)
        actions.click(self.find(self.selectable_grid_locator)).perform()
        actions.click(self.find(self.one_selector)).perform()
        self.assertIn('active', self.find(self.one_selector).get_attribute('class'), "Not active")
        actions.click(self.find(self.five_selector)).perform()
        self.assertIn('active', self.find(self.five_selector).get_attribute('class'), "Not active")
        actions.click(self.find(self.seven_selector)).perform()
        self.assertIn('active', self.find(self.seven_selector).get_attribute('class'), "Not active")
        time.sleep(4)

    def test_selectable_grid_with_click(self):
        self.click(self.selectable_grid_locator)
        time.sleep(1)
        self.click(self.one_selector)
        self.assertIn('active', self.find(self.one_selector).get_attribute('class'), "Not active")
        self.click(self.five_selector)
        self.assertIn('active', self.find(self.five_selector).get_attribute('class'), "Not active")
        self.click(self.seven_selector)
        self.assertIn('active', self.find(self.seven_selector).get_attribute('class'), "Not active")
        time.sleep(4)

    def test_selectable_list(self):
        self.click(self.selectable_list_locator)
        self.click(self.first_list)
        self.assertIn('active', self.find(self.first_list).get_attribute('class'), 'Not selected')
        self.click(self.second_list)
        self.assertIn('active', self.find(self.second_list).get_attribute('class'), "Not selected")
        self.click(self.third_list)
        self.assertIn('active', self.find(self.third_list).get_attribute('class'), "Not selected")
        time.sleep(2)
