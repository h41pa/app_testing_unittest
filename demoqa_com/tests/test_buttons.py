import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from demoqa_com.pages.basepage import BasePage


class TestButtons(unittest.TestCase, BasePage):
    LINK = 'https://demoqa.com/buttons'
    double_click_me_locator = (By.ID, 'doubleClickBtn')
    right_click_me_locator = (By.ID, 'rightClickBtn')
    click_me_locator = (By.XPATH, '//button[text()="Click Me"]')
    double_click_response = (By.ID, 'doubleClickMessage')
    right_click_response = (By.ID, 'rightClickMessage')
    click_me_reponse = (By.XPATH, '//p[@id="dynamicClickMessage"]')

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_buttons_actions(self):
        actions = ActionChains(self.driver)
        # double click test
        actions.double_click(self.find(self.double_click_me_locator)).perform()
        self.assertTrue(self.is_displayed(self.double_click_me_locator), 'Not displayed')
        self.assertEqual('You have done a double click', self.get_text(self.double_click_response),
                         'Not expected response!')
        # test right click
        actions.context_click(self.find(self.right_click_me_locator)).perform()
        self.assertTrue(self.is_displayed(self.right_click_me_locator),'Not displayed')
        self.assertEqual('You have done a right click', self.get_text(self.right_click_response), 'Not expected response!')
        # test click me
        self.click(self.click_me_locator)
        self.assertTrue(self.is_displayed(self.click_me_locator), 'Not displayed')
        self.assertEqual('You have done a dynamic click',self.get_text(self.click_me_reponse),'Not expected response!')
