import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from demoqa_com.pages.basepage import BasePage


class TestResizableBox(unittest.TestCase, BasePage):
    URL = 'https://demoqa.com/resizable'
    first_box_locator = (By.XPATH, '//*[@id="resizableBoxWithRestriction"]')
    first_resizer = (By.XPATH, '//*[@id="resizableBoxWithRestriction"]/span')

    second_box_locator = (By.XPATH, '//*[@id="resizable"]')
    second_resizer = (By.XPATH, "//div[@id='resizable']//span[@class='react-resizable-handle react-resizable-handle-se']")

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_resizable_box_1(self):
        initial_width = self.find(self.first_box_locator).size['width']
        initial_height = self.find(self.first_box_locator).size['height']
        print(initial_width, initial_height)
        actions = ActionChains(self.driver)
        actions.click_and_hold(self.find(self.first_resizer)).move_by_offset(40, 40).perform()
        time.sleep(2)
        actual_width = self.find(self.first_box_locator).size['width']
        actual_height = self.find(self.first_box_locator).size['height']
        print(actual_width, actual_height)
        self.assertTrue(actual_width > initial_width and actual_height > initial_height, "Error")

    def test_resizable_box_2(self):
        initial_width = self.find(self.second_box_locator).size['width']
        initial_height = self.find(self.second_box_locator).size['height']
        print(initial_width, initial_height)
        actions = ActionChains(self.driver)
        time.sleep(2)
        actions.send_keys(Keys.END).perform()
        time.sleep(2)
        actions.click_and_hold(self.find(self.second_resizer)).move_by_offset(68, 48).perform()
        time.sleep(5)
        actual_width = self.find(self.second_box_locator).size['width']
        actual_height = self.find(self.second_box_locator).size['height']
        self.assertTrue(actual_width > initial_width and actual_height > initial_height, "Error")
        print(actual_width, actual_height)
