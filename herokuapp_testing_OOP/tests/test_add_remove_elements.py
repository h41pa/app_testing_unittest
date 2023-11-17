import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from herokuapp_testing_OOP.pages.add_remove_elements import AddRemoveElementsPage


class TestAddRemovePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_add_elements(self):
        add_remove = AddRemoveElementsPage(self.driver)
        add_remove.load_page()
        add_remove.add_element(1)
        assert add_remove.is_delete_button_displayed(), "Error Delete Button not avaible"
        time.sleep(2)

    def test_delete_button(self):
        add_remove = AddRemoveElementsPage(self.driver)
        add_remove.load_page()
        add_remove.add_element(2)
        add_remove.delete_button()
        time.sleep(2)
        assert add_remove.get_number_of_delete_buttons() == 1, "Delete button not working"

    def test_button_x10(self):
        add_remove = AddRemoveElementsPage(self.driver)
        add_remove.load_page()
        add_remove.add_element(10)
        assert add_remove.get_number_of_delete_buttons() == 10, "There are less or more than 10 buttons"

    def test_title(self):
        add_remove = AddRemoveElementsPage(self.driver)
        add_remove.load_page()
        print(add_remove.get_header_text() )
        assert add_remove.get_header_text() == add_remove.EXPECTED_HEADER_TEXT, "Not same title"
