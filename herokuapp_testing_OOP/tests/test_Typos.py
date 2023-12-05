import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from herokuapp_testing_OOP.pages.base_page import BasePage


class TestTypos(unittest.TestCase, BasePage):
    LINK = "https://the-internet.herokuapp.com/typos"
    html_full = (By.CLASS_NAME, "no-js")
    text_locator = (By.XPATH, "//*/div/p[2]")
    correct_text = "Sometimes you'll see a typo, other times you won't."

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_no_typos(self):
        if self.get_text(self.text_locator) != self.correct_text:
            time.sleep(2)
            self.driver.refresh()
        else:
            self.assertEqual(self.correct_text, self.get_text(self.text_locator), "Error, a typo is present")
        print(self.get_text(self.text_locator))

    def test_typos(self):
        if self.get_text(self.text_locator) == self.correct_text:
            time.sleep(2)
            self.driver.refresh()
        else:
            self.assertNotEqual(self.correct_text, self.get_text(self.text_locator), "Error, no typo visible")
        print(self.get_text(self.text_locator))
