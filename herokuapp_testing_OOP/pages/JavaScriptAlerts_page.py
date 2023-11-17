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
    expected_text_js_propmpt_input = "Test"
    expected_text_js_propmpt_when_decline = "You entered: null"

    def __init__(self, driver):
        super().__init__(driver)

    def load_page(self):
        self.open_url(self.LINK)

    def click_simple_alert_and_accept(self):
        self.click(self.BUTTON_JS_ALERT_SIMPLE)
        self.accept_alert()

    def get_text_for_js_result(self):
        return self.get_text(self.RESULT_LOCATOR)

    def click_js_confirm_and_accept(self):
        self.click(self.BUTTON_JS_ALERT_CONFIRM)
        self.accept_alert()

    def click_js_confirm_and_decline(self):
        self.click(self.BUTTON_JS_ALERT_CONFIRM)
        self.decline_alert()

    def click_js_prompt_and_accept(self):
        self.click(self.BUTTON_JS_PROMPT)
        self.type_alert_keys(self.expected_text_js_propmpt_input)
        self.accept_alert()

    def click_js_prompt_and_decline(self):
        self.click(self.BUTTON_JS_PROMPT)
        self.decline_alert()