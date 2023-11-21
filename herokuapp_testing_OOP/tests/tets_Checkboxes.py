import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from herokuapp_testing_OOP.pages.base_page import BasePage


class TestCheckBoxes(unittest.TestCase, BasePage):
    # locators
    LINK = "https://the-internet.herokuapp.com/checkboxes"
    header_locator = (By.XPATH, "//*[@id='content']/div/h3")
    check_box_1_locator = (By.XPATH, "//*[@id='checkboxes']/input[1]")
    check_box_2_locator = (By.XPATH, "//*[@id='checkboxes']/input[2]")

    # text
    expected_header_text = "Checkboxes"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_header_text(self):
        assert self.expected_header_text == self.get_text(self.header_locator), "Not same header text"

    def test_checkbox_1(self):
        self.check_checkbox(self.check_box_1_locator)
        self.assertTrue(self.is_selected(self.check_box_1_locator), "Checkbox not checked")
        self.uncheck_checkbox(self.check_box_1_locator)
        self.assertFalse(self.is_selected(self.check_box_1_locator), "Checkbox still checked")

    def test_checkbox_2(self):
        self.uncheck_checkbox(self.check_box_2_locator)
        self.assertFalse(self.is_selected(self.check_box_2_locator),"Checkbox still checked")
        self.check_checkbox(self.check_box_2_locator)
        self.assertTrue(self.is_selected(self.check_box_2_locator), "Checkbox not checked")