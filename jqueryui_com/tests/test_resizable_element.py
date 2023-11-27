import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from jqueryui_com.pages.basepage import BasePage


class TestResizableElement(unittest.TestCase, BasePage):
    URL = 'https://jqueryui.com/resizable/'
    resizer_width_locator_ = (By.XPATH, '//*[@id="resizable"]/div[1]')
    resizer_height_locator_ = (By.XPATH, '//*[@id="resizable"]/div[2]')
    widget_locator = (By.XPATH, '//*[@id="resizable"]')

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_resizable_element_bigger(self):
        frame = self.driver.find_element(By.CLASS_NAME, 'demo-frame')
        self.driver.switch_to.frame(frame)
        time.sleep(2)
        actions = ActionChains(self.driver)
        # self.click(self.resizer_locator)
        initial_element_width = self.find(self.widget_locator).size['width']
        initial_element_height = self.find(self.widget_locator).size['height']
        print(initial_element_width, initial_element_height)
        actions.click_and_hold(self.find(self.resizer_width_locator_)).move_by_offset(40, 0).release().perform()
        actions.click_and_hold(self.find(self.resizer_height_locator_)).move_by_offset(0, 50).release().perform()
        resized_element_width = self.find(self.widget_locator).size['width']
        resized_element_height = self.find(self.widget_locator).size['height']
        print(resized_element_width, resized_element_height)
        self.assertTrue(resized_element_width > initial_element_width, "Error")
        self.assertTrue(resized_element_height > initial_element_height, "Error")
        time.sleep(2)

    def test_resizable_element_smaller(self):
        frame = self.driver.find_element(By.CLASS_NAME, 'demo-frame')
        self.driver.switch_to.frame(frame)
        initial_element_width = self.find(self.widget_locator).size['width']
        initial_element_height = self.find(self.widget_locator).size['height']
        print(initial_element_width, initial_element_height)
        acions = ActionChains(self.driver)
        acions.click_and_hold(self.find(self.resizer_width_locator_)).move_by_offset(-20, 0).release().perform()
        acions.click_and_hold(self.find(self.resizer_height_locator_)).move_by_offset(0, -30).release().perform()
        resized_element_width = self.find(self.widget_locator).size['width']
        resized_element_height = self.find(self.widget_locator).size['height']
        print(resized_element_width, resized_element_height)
        self.assertTrue(resized_element_height < initial_element_height, 'Error!')
        self.assertTrue(resized_element_width < initial_element_width, 'Error!')
