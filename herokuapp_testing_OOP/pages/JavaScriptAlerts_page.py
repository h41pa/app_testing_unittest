from selenium.webdriver.common.by import By

from herokuapp_testing_OOP.pages.base_page import BasePage


class JavaScriptAlertsPage(BasePage):
    # locators
    LINK = "https://the-internet.herokuapp.com/javascript_alerts"
    BUTTON_JS_ALERT_SIMPLE = (By.XPATH, "//button[@onclick='jsAlert()']")
    BUTTON_JS_ALERT_CONFIRM = (By.XPATH, "//button[@onclick='jsConfirm()']")
    BUTTON_JS_PROMPT = (By.XPATH, "//button[@onclick='jsPrompt()']")
    RESULT_LOCATOR = (By.ID, "result")
    # text
    expected_text_js_alert_simple = "You successfully clicked an alert"
    expected_text_js_alert_confirm_accept = "You clicked: Ok"
    expected_text_js_alert_confirm_decline = "You clicked: Cancel"

    def __init__(self, driver):
        super().__init__(driver)

    def load_page(self):
        self.open_url(self.LINK)

    def click_simple_alert_and_accept(self):
        self.click(self.BUTTON_JS_ALERT_SIMPLE)
        self.accept_alert()

    def get_text_js_alert_simple(self):
        return self.get_text(self.RESULT_LOCATOR)

