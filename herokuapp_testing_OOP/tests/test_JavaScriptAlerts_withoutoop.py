import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class JavaScriptAlerts(unittest.TestCase):
    LINK = "https://the-internet.herokuapp.com/javascript_alerts"
    BUTTON_JS_ALERT_SIMPLE = (By.XPATH, "//button[@onclick='jsAlert()']")
    BUTTON_JS_ALERT_CONFIRM = (By.XPATH, "//button[@onclick='jsConfirm()']")
    BUTTON_JS_PROMPT = (By.XPATH, "//button[@onclick='jsPrompt()']")
    RESULT = (By.ID, "result")

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        sleep(2)
        self.driver.quit()

    def test_accept_simple_JsAlert(self):
        self.driver.find_element(*self.BUTTON_JS_ALERT_SIMPLE).click()
        sleep(2)
        alert = self.driver.switch_to.alert
        alert.accept()
        expected_text = "You successfully clicked an alert"
        actual_text = self.driver.find_element(*self.RESULT).text
        assert expected_text == actual_text, "Error, text are not matching."
        # self.assertEqual(expected_text, actual_text, "Error, text are not matching.")

    def test_accept_Js_Confirm(self):
        self.driver.find_element(*self.BUTTON_JS_ALERT_CONFIRM).click()
        sleep(2)
        self.driver.switch_to.alert.accept()
        expected_text = "You clicked: Ok"
        actual_text = self.driver.find_element(*self.RESULT).text
        assert expected_text == actual_text, "Error, text are not matching."

    def test_decline_Js_Confirm(self):
        self.driver.find_element(*self.BUTTON_JS_ALERT_CONFIRM).click()
        sleep(2)
        self.driver.switch_to.alert.dismiss()
        expected_text = "You clicked: Cancel"
        actual = self.driver.find_element(*self.RESULT).text
        assert expected_text == actual, "Error, text are not matching"

    def test_accept_Js_Prompt_with_text(self):
        self.driver.find_element(*self.BUTTON_JS_PROMPT).click()
        alert = self.driver.switch_to.alert
        alert.send_keys("Text")
        alert.accept()
        sleep(2)
        expected_text = "You entered: Text"
        actual_text = self.driver.find_element(*self.RESULT).text
        self.assertEqual(expected_text, actual_text, "Error text not matching")

    def test_decline_Js_Prompt(self):
        self.driver.find_element(*self.BUTTON_JS_PROMPT).click()
        alert = self.driver.switch_to.alert
        alert.dismiss()
        expected_text = "You entered: null"
        actual_text = self.driver.find_element(*self.RESULT).text
        self.assertEqual(expected_text, actual_text, "Text Not macthing")
