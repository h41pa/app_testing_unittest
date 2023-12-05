import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from demoqa_com.pages.basepage import BasePage


class TestDroppableQA(unittest.TestCase, BasePage):
    URL = 'https://demoqa.com/droppable'
    simple_tab_locator = (By.ID, 'droppableExample-tab-simple')
    drag_me_locator = (By.XPATH, '//*[@id="draggable"]')
    drop_area = (By.XPATH, '//*[@id="droppable"]')

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.URL)
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def test_simple_tab_drag_and_drop(self):
        self.click(self.simple_tab_locator)
        actions = ActionChains(self.driver)
        actions.click_and_hold(self.find(self.drag_me_locator)).move_to_element(
            self.find(self.drop_area)).release().perform()
        self.assertEqual('Dropped!', self.get_text(self.drop_area), 'Error')
        rgb = self.find(self.drop_area).value_of_css_property('background-color')
        color = Color.from_string(rgb).hex
        self.assertEqual('#4682b4', color, 'Not expected background color')
        print(color)
