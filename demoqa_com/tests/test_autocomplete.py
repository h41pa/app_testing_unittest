import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from demoqa_com.pages.basepage import BasePage


class TestAutoComplete(unittest.TestCase, BasePage):
    URL = 'https://demoqa.com/auto-complete'
    multiple_colors_locator = (By.XPATH, '//*[@id="autoCompleteMultipleInput"]')
    multi_text_box = (By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div/div[1]')
    delete_text_multi_box = (By.XPATH, '//*[@id="autoCompleteMultipleContainer"]/div/div[2]/div')

    single_color_locator = (By.XPATH, '//*[@id="autoCompleteSingleInput"]')
    single_text_box = (By.XPATH, '//*[@id="autoCompleteSingleContainer"]/div/div[1]')


    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.URL)
        self.driver.implicitly_wait(2)

    def tearDown(self):
        self.driver.quit()

    def test_multiple_colors_autocomplete_box(self):
        self.find(self.multiple_colors_locator).send_keys('Red')
        self.find(self.multiple_colors_locator).send_keys(Keys.ENTER)
        self.find(self.multiple_colors_locator).send_keys('Blue')
        self.find(self.multiple_colors_locator).send_keys(Keys.ENTER)
        self.assertIn('Red', self.get_text(self.multi_text_box))
        self.assertIn('Blue', self.get_text(self.multi_text_box))
        self.assertIn('', self.get_text(self.multi_text_box))
        print(self.get_text(self.multi_text_box))
        self.click(self.delete_text_multi_box)  #clean text box
        self.assertNotIn('Red', self.get_text(self.multi_text_box))
        self.assertNotIn('Blue', self.get_text(self.multi_text_box))

    def test_single_color_autocomplete_box(self):
        self.find(self.single_color_locator).send_keys('Green')
        self.find(self.single_color_locator).send_keys(Keys.ENTER)
        self.assertIn('Green', self.get_text(self.single_text_box))


