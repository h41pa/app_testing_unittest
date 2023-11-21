import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from herokuapp_testing_OOP.pages.base_page import BasePage
from selenium.webdriver import Keys


class TestKeyPress(unittest.TestCase, BasePage):
    # locators
    LINK = "https://the-internet.herokuapp.com/key_presses?"
    header_locator = (By.CSS_SELECTOR, "#content > div > h3")
    field_locator = (By.CLASS_NAME, "no-js")
    empty_field_locator = (By.ID, "target")

    result_locator = (By.ID, "result")

    # text
    expected_header_text = "Key Presses"
    expected_press_enter_result = "You entered: ENTER"
    expected_press_ctrl_result = "You entered: CONTROL"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_page_header_text(self):
        self.assertEqual(self.expected_header_text, self.get_text(self.header_locator), "Not same header text!")

    def test_field_keypress(self):
        self.type(self.field_locator, Keys.ENTER)
        self.assertEqual(self.expected_press_enter_result, self.get_text(self.result_locator),
                         "result not,You entered: ENTER")
        print(self.get_text(self.result_locator))
        self.type(self.field_locator, Keys.CONTROL)
        self.assertEqual(self.expected_press_ctrl_result, self.get_text(self.result_locator),
                         "Result not ,You entered: CONTROL")
        print(self.get_text(self.result_locator))

    def test_empty_field(self):
        self.type(self.empty_field_locator, Keys.SPACE)
        time.sleep(2)
        self.assertEqual("You entered: SPACE", self.get_text(self.result_locator),"result not,You entered: SPACE")
        self.type(self.empty_field_locator, Keys.CONTROL)
        time.sleep(2)
        self.assertEqual(self.expected_press_ctrl_result, self.get_text(self.result_locator), "Result not ,You entered: CONTROL")


    # def test_enter_empty_filed(self):
    #     # seems that pressing enter on empty fields makes result  You entered: ENTER" insta vanish
    #     self.type(self.empty_field_locator, Keys.ENTER)
    #     self.assertEqual(self.expected_press_enter_result, self.get_text(self.result_locator),
    #                      "result not,You entered: ENTER")
    #     print(self.get_text(self.result_locator))
    #     self.type(self.empty_field_locator, Keys.CONTROL)
    #     self.assertEqual(self.expected_press_ctrl_result, self.get_text(self.result_locator),
    #                      "Result not ,You entered: CONTROL")
    #     print(self.get_text(self.result_locator))
