import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from herokuapp_testing_OOP.pages.JavaScriptAlerts_page import JavaScriptAlertsPage


class TestJavaScriptAlerts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_js_simple(self):
        java_alerts = JavaScriptAlertsPage(self.driver)
        java_alerts.load_page()
        java_alerts.click_simple_alert_and_accept()
        assert java_alerts.expected_text_js_alert_simple == java_alerts.get_text_for_js_result(), "Error, not same text!"

    def test_js_confirm_and_accept(self):
        java_alerts = JavaScriptAlertsPage(self.driver)
        java_alerts.load_page()
        java_alerts.click_js_confirm_and_accept()
        assert java_alerts.expected_text_js_alert_confirm_accept == java_alerts.get_text_for_js_result()

    def test_js_confirm_and_decline(self):
        java_alerts = JavaScriptAlertsPage(self.driver)
        java_alerts.load_page()
        java_alerts.click_js_confirm_and_decline()
        assert java_alerts.expected_text_js_alert_confirm_decline == java_alerts.get_text_for_js_result()
