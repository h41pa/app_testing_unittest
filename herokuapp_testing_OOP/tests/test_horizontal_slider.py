import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from herokuapp_testing_OOP.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class TestHorizontalSlider(unittest.TestCase, BasePage):
    LINK = "https://the-internet.herokuapp.com/horizontal_slider"
    header_title = (By.XPATH, "h3")
    slider_locator = (By.CSS_SELECTOR, "input[type='range']")
    range_locator = (By.XPATH, "//span[@id='range']")

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_slider_with_right_left_arrows(self):
        self.type(self.slider_locator, Keys.ARROW_RIGHT * 5)
        self.assertEqual(self.get_text(self.range_locator), "2.5", "Error, slider didn t move forward 5x")
        time.sleep(2)
        self.type(self.slider_locator, Keys.ARROW_LEFT * 2)
        self.assertEqual(self.get_text(self.range_locator), "1.5", "Error, slider didn t back 2x")
        time.sleep(2)


