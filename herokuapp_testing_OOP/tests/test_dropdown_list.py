import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from herokuapp_testing_OOP.pages.base_page import BasePage


class TestCheckBoxes(unittest.TestCase, BasePage):
    # locators
    LINK = "https://the-internet.herokuapp.com/dropdown"
    header_locator = (By.CSS_SELECTOR, "#content > div > h3")
    dropdown_locator = (By.ID, "dropdown")
    # text
    option_1 = (By.CSS_SELECTOR, "#dropdown [value='1']")
    option_2 = (By.CSS_SELECTOR, "#dropdown [value='2']")
    expected_header_text = "Dropdown List"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_header_text(self):
        assert self.expected_header_text == self.get_text(self.header_locator), "Not same header text"

    def test_dropdown_list_is_displayed(self):
        self.assertTrue(self.is_displayed(self.dropdown_locator), "Locator not available")

    def test_option_1(self):
        self.select_option_by_value(self.dropdown_locator, "1")
        self.assertTrue(self.is_selected(self.option_1))
        time.sleep(2)

    def test_option_2(self):
        self.select_option_by_value(self.dropdown_locator, "2")
        self.assertTrue(self.is_selected(self.option_2))

    # def test_extra(self):
    #     self.click(self.option_1)
    #     assert "Option 1" in self.get_text(self.option_1)



