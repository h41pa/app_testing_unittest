import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.color import Color
from webdriver_manager.chrome import ChromeDriverManager

from herokuapp_testing_OOP.pages.base_page import BasePage


class TestNotificationMessage(unittest.TestCase, BasePage):
    LINK = 'https://the-internet.herokuapp.com/notification_message_rendered'
    flash_locator = (By.ID, 'flash')
    click_locator = (By.LINK_TEXT, 'Click here')
    expected_messages = ['Action unsuccessful', 'Action unsuccessful', 'please try again']

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.close()

    def test_get_message_Action_successful(self):
        #same test can be used for the others 2 messages.
        time.sleep(2)
        self.click(self.click_locator)
        if self.get_text(self.flash_locator) != 'Action successful':
            self.click(self.click_locator)
            time.sleep(2)

        else:
            self.assertEqual('Action successful', self.get_text(self.flash_locator), "Error")

    def test_get_notification_message_after_refresh(self):
        #checking with 3 clickes what texts we get
        time.sleep(1)
        for i in range(3):
            self.click(self.click_locator)
            print(self.get_text(self.flash_locator))

        self.assertTrue(self.expected_messages, self.get_text(self.flash_locator))

    def test_get_colour_of_flash_bar(self):
        self.click(self.click_locator)
        time.sleep(2)
        color = self.find(self.flash_locator).value_of_css_property('background-color')
        rgb = Color.from_string(color).hex
        print(rgb)
        self.assertEqual('#2ba6cb', rgb, 'Not color u wanted!')
