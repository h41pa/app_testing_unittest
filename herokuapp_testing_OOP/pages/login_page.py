from herokuapp_testing_OOP.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPageObjects:
    login_link = "https://the-internet.herokuapp.com/login"
    username_locator = (By.XPATH, "//input[@name='username']")
    password_locator = (By.XPATH, "//input[@name='password']")
    login_button_locator = (By.XPATH, "//i[@class='fa fa-2x fa-sign-in']")
    flash_error = (By.ID, "flash")

    valid_username = "tomsmith"
    valid_password = "SuperSecretPassword!"
    invalid_username = "tomsmith1"
    invalid_password = "SuperSecretPassword111"
    expected_invalid_text_password = "Your password is invalid!"
    expected_invalid_text_username = "Your username is invalid!"


class Login(BasePage, LoginPageObjects):

    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        return self.open_url(self.login_link)

    def execute_valid_login(self):
        self.type(self.username_locator, self.valid_username)
        self.type(self.password_locator, self.valid_password)
        self.click(self.login_button_locator)

    def execute_invalid_username_login(self):
        self.type(self.username_locator, self.invalid_username)
        self.type(self.password_locator, self.valid_password)
        self.click(self.login_button_locator)

    def execute_invalid_password_login(self):
        self.type(self.username_locator, self.valid_username)
        self.type(self.password_locator, self.invalid_password)
        self.click(self.login_button_locator)

    def get_error_message(self):
        return self.get_text(self.flash_error)