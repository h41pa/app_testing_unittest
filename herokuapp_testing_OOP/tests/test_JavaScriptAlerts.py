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

    def test_Js_simple(self):
        javalerts = JavaScriptAlertsPage(self.driver)
        javalerts.load_page()
        javalerts.click_simple_alert_and_accept()
        assert javalerts.expected_text_js_alert_simple == javalerts.get_text_js_alert_simple(), "Error, not same text!"
