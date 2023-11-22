import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from herokuapp_testing_OOP.pages.base_page import BasePage


class TestDynamicContent(unittest.TestCase, BasePage):
    LINK_Static_content = "https://the-internet.herokuapp.com/dynamic_content?with_content=static"
    avatar_3_locator = (By.XPATH, '//*[@id="content"]/div[3]/div[1]/img')
    text_3_locator = (By.XPATH, '//*[@id="content"]/div[3]/div[2]')
    LINK_DYNAMIC_CONTENT = "https://the-internet.herokuapp.com/dynamic_content"
    text_1_locator = (By.XPATH, '//*[@id="content"]/div[1]/div[2]')
    text_2_locator = (By.XPATH, '//*[@id="content"]/div[2]/div[2]')

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_content_static(self):
        # sometimes  test fails cause webpage refresh same avatar.
        self.driver.get(self.LINK_Static_content)
        before_refresh_avatar_3 = self.find(self.avatar_3_locator).get_attribute('src')
        before_refresh_text_3 = self.get_text(self.text_3_locator)
        print(before_refresh_avatar_3)
        print(before_refresh_text_3)
        self.driver.refresh()
        after_refresh_avatar_3 = self.find(self.avatar_3_locator).get_attribute('src')
        after_refresh_text_3 = self.get_text(self.text_3_locator)
        print(after_refresh_avatar_3)
        print(after_refresh_text_3)
        self.assertNotEqual(before_refresh_avatar_3, after_refresh_avatar_3, "Same avatar")
        self.assertNotEqual(before_refresh_text_3, after_refresh_text_3, "Same text")

    def test_dynamic_content(self):
        self.driver.get(self.LINK_DYNAMIC_CONTENT)
        before_refresh_text_1 = self.get_text(self.text_1_locator)
        before_refresh_text_2 = self.get_text(self.text_2_locator)
        before_refresh_text_3 = self.get_text(self.text_3_locator)
        self.driver.refresh()
        after_refresh_text_1 = self.get_text(self.text_1_locator)
        after_refresh_text_2 = self.get_text(self.text_2_locator)
        after_refresh_text_3 = self.get_text(self.text_3_locator)
        self.assertNotEqual(before_refresh_text_1, after_refresh_text_1, 'Seems same text!')
        self.assertNotEqual(before_refresh_text_2, after_refresh_text_2, 'Seems same text!')
        self.assertNotEqual(before_refresh_text_3, after_refresh_text_3, 'Seems same text!')



