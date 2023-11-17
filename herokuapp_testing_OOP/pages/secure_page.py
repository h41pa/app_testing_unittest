from herokuapp_testing_OOP.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class SecurePage(BasePage):
    secure_page_url = "https://the-internet.herokuapp.com/secure"
    logout_button = (By.CLASS_NAME, "icon-signout")
    secure_are_locator = (By.CSS_SELECTOR, "#content h2")
    expected_header_text = "Secure Area"

    def __init__(self, driver):
        super().__init__(driver)

    def get_expected_url(self):
        return self.secure_page_url

    def get_header_text(self):
        return self.get_text(self.secure_are_locator)

    def is_logout_button_displayed(self):
        return self.is_displayed(self.logout_button)
