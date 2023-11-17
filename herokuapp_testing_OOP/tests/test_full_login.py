import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from herokuapp_testing_OOP.pages.LoginpageObjects import LoginPageObjects
from herokuapp_testing_OOP.pages.base_page import BasePage


class TestLogin(unittest.TestCase, BasePage, LoginPageObjects):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.login_link)
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 5)

    def tearDown(self):
        self.driver.quit()

    def test_valid_login(self):
        self.type(self.username_locator, self.valid_username)
        self.type(self.password_locator, self.valid_password)
        self.click(self.login_button_locator)
        assert self.secure_page_url == self.get_current_url(), "Error unxpected url"
        self.wait.until(EC.visibility_of_element_located(self.logout_button), "Element Not visible")
        assert self.is_displayed(self.logout_button), "logout button missing"
        assert self.expected_header_text == self.get_text(self.secure_are_locator)

    def test_invalid_username(self):
        self.type(self.username_locator, self.invalid_username)
        self.type(self.password_locator, self.valid_password)
        self.click(self.login_button_locator)
        assert self.expected_invalid_text_username in self.get_text(self.flash_error), "error , not expected result"

    def test_invalid_password(self):
        self.type(self.username_locator, self.valid_username)
        self.type(self.password_locator, self.invalid_password)
        self.click(self.login_button_locator)
        assert self.expected_invalid_text_password in self.get_text(self.flash_error)
