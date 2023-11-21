import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from herokuapp_testing_OOP.pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class TestJQueryUI(unittest.TestCase, BasePage):
    LINK = "https://the-internet.herokuapp.com/jqueryui/menu"
    expected_back_to_JQueryUI_link = "https://the-internet.herokuapp.com/jqueryui"
    title_header_locator = (By.XPATH, "//div/h3")
    widget_number_of_windows_locator = (By.CLASS_NAME, "ui-menu-item")
    back_to_JQueryUI_menu_locator = (By.XPATH, "//li[@id='ui-id-8']")
    expected_title_text = "JQueryUI - Men"
    enabled_window_locator = (By.XPATH, "//*[@id='ui-id-3']/a")
    downloads_locator = (By.XPATH, "//li[@id='ui-id-4']")
    pdf_locator = (By.XPATH, "//li[@id='ui-id-5']")
    csv_locator = (By.XPATH, "//li[@id='ui-id-6']")
    excel_locator = (By.XPATH, "//li[@id='ui-id-7']")

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)
        self.wait = WebDriverWait(self.driver, 5)

    def tearDown(self):
        self.driver.quit()

    def test_number_of_widgets_8(self):
        self.assertEqual(8, self.get_number_of_elements(self.widget_number_of_windows_locator),
                         "Error not correct number of widgets")
        print(self.get_number_of_elements(self.widget_number_of_windows_locator))

    def test_back_to_JQueryUI(self):
        self.click(self.enabled_window_locator)
        self.wait.until(EC.element_to_be_clickable(self.find(self.back_to_JQueryUI_menu_locator)),
                        "Element not clickable yet.")
        self.move_to_element(self.back_to_JQueryUI_menu_locator)
        self.assertEqual(self.expected_back_to_JQueryUI_link, self.get_current_url(), "Unexpected URL!")
        time.sleep(3)

    def test_downloads_pdf(self):
        self.click(self.enabled_window_locator)
        self.wait.until(EC.element_to_be_clickable(self.find(self.downloads_locator)), "Element not clickable yet.")
        self.move_to_element(self.downloads_locator)
        self.wait.until(EC.element_to_be_clickable(self.find(self.pdf_locator)), "Element not clickable yet.")
        self.move_to_element(self.pdf_locator)
        assert self.is_displayed(self.pdf_locator), " Not displayed"
        assert "PDF" == self.get_text(self.pdf_locator),  "Not expected text!"
        time.sleep(1)

    def test_downloads_CSV(self):
        assert self.is_displayed(self.enabled_window_locator)
        self.click(self.enabled_window_locator)
        self.wait.until(EC.element_to_be_clickable(self.find(self.downloads_locator)), "Element not clickable yet.")
        self.move_to_element(self.downloads_locator)
        self.wait.until(EC.element_to_be_clickable(self.find(self.csv_locator)), "Element not clickable yet.")
        self.assertTrue(self.is_displayed(self.csv_locator),"Not displayed")
        self.assertEqual("CSV", self.get_text(self.csv_locator), "Unexpected text")
        self.move_to_element(self.csv_locator)
        time.sleep(1)

    def test_downloads_excel(self):
        #without action chains and EC
        assert self.is_displayed(self.enabled_window_locator)
        self.click(self.enabled_window_locator)
        time.sleep(1)
        self.click(self.downloads_locator)
        time.sleep(1)
        self.assertTrue(self.is_displayed(self.excel_locator), "Not Displayed")
        self.assertEqual("Excel", self.get_text(self.excel_locator), "Unexpected text!")
        self.click(self.excel_locator)
        time.sleep(1)

