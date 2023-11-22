import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from herokuapp_testing_OOP.pages.base_page import BasePage


class TestDataTables(unittest.TestCase, BasePage):
    LINK = "https://the-internet.herokuapp.com/tables"
    title_locator = (By.XPATH, "//h3")
    expected_title_text = "Data Tables"
    table_1_lastname_locator = (By.XPATH, "//table[@id='table1']/thead/tr/th[1]")
    table_1_firstname_locator = (By.XPATH, "//table[@id='table1']/thead/tr/th[2]")
    table1_rows_locator = (By.XPATH, "//table[@id='table1']/tbody/tr")
    table2_rows_locator = (By.XPATH, "//*[@id='table2']/tbody/tr")
    table_2_lastname_locator = (By.XPATH, "//*[@id='table2']/thead/tr/th[1]")

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_title(self):
        self.assertEqual(self.expected_title_text, self.get_text(self.title_locator), "Unexpected title!")

    def get_column_values_table_1(self, column_index):
        # functie pentru a colecta valorile dintr-o coloana
        column_values = []
        rows = self.driver.find_elements(*self.table1_rows_locator)
        for row in rows:
            column_values.append(row.find_element(By.XPATH, f"td[{column_index}]").text)
        return column_values

    def test_table_1_sorting_by_lastname(self):
        self.click(self.table_1_lastname_locator)
        sort_list = self.get_column_values_table_1(1)
        self.assertEqual(sort_list, sorted(sort_list))

    def test_table_1_sorting_by_firstname(self):
        self.click(self.table_1_firstname_locator)
        sort_list = self.get_column_values_table_1(2)
        self.assertEqual(sort_list, sorted(sort_list))

    def get_column_values_table_2(self, column_index):
        columns_values = []
        rows = self.driver.find_elements(*self.table2_rows_locator)
        for row in rows:
            columns_values.append(row.find_element(By.XPATH, f"td[{column_index}]").text)

        return columns_values

    def test_table_2_sorting_by_lastname(self):
        self.click(self.table_2_lastname_locator)
        list_values = self.get_column_values_table_2(1)
        self.assertEqual(list_values, sorted(list_values))
        print(list_values)

