import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from herokuapp_testing_OOP.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class TestDragandDrop(unittest.TestCase, BasePage):
    LINK = "https://the-internet.herokuapp.com/drag_and_drop"
    header_locator = (By.CSS_SELECTOR, '#content > div > h3')
    expected_header_text = "Drag and Drop"
    table_A_locator = (By.ID, "column-a")
    table_B_locator = (By.ID, "column-b")

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_title(self):
        self.assertEqual(self.expected_header_text, self.get_text(self.header_locator), "Unexpected title!")

    def test_drag_and_drop(self):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(self.find(self.table_A_locator), self.find(self.table_B_locator)).perform()
        time.sleep(3)
        self.assertEqual(self.get_text(self.table_A_locator), "B", "Error, element A not dragged successful")
        self.assertEqual(self.get_text(self.table_B_locator), "A", "Error, element B not dragged successful")


