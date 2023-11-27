import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from jqueryui_com.pages.basepage import BasePage


class TestResizableElement(unittest.TestCase, BasePage):
    URL = 'https://jqueryui.com/droppable/'
    draggable_element = (By.XPATH, "//div[@id='draggable']")
    drop_area = (By.XPATH, "//div[@id='droppable']")

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_drop(self):
        time.sleep(2)
        frame = self.driver.find_element(By.CLASS_NAME, 'demo-frame')
        self.driver.switch_to.frame(frame)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(self.find(self.draggable_element), self.find(self.drop_area)).perform()
        self.assertEqual('Dropped!', self.get_text(self.drop_area), 'Not Expected text!')
        time.sleep(2)
