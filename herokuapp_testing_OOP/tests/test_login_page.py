import time
import unittest
from herokuapp_testing_OOP.pages.login_page import Login
from herokuapp_testing_OOP.pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from herokuapp_testing_OOP.pages.secure_page import SecurePage


class TestLoginPage(unittest.TestCase, BasePage):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_successful_login(self):
        login = Login(self.driver)
        login.open()
        login.execute_valid_login()
        secure = SecurePage(self.driver)
        assert secure.get_expected_url() == self.get_current_url(), "Actual URL is not the same as expected"
        assert secure.expected_header_text == secure.get_header_text(), "Header message not as expected"
        assert secure.is_logout_button_displayed()

    def test_invalid_username(self):
        login = Login(self.driver)
        login.open()
        login.execute_invalid_username_login()
        time.sleep(2)
        assert login.expected_invalid_text_username in login.get_error_message(), "Username is not as expected"

    def test_invalid_password(self):
        login = Login(self.driver)
        login.open()
        login.execute_invalid_password_login()
        assert login.expected_invalid_text_password in login.get_error_message(), "Password is not as expected"