import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from demoqa_com.pages.basepage import BasePage

class TestFrames(unittest.TestCase, BasePage):
    URL = 'https://demoqa.com/frames'
    header_locator = (By.ID, 'sampleHeading')


    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.URL)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()


    def test_frames(self):
        self.driver.switch_to.frame('frame1')
        print(self.get_text(self.header_locator))
        self.assertEqual('This is a sample page', self.get_text(self.header_locator), "Unexpected text!")
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame('frame2')
        self.assertEqual('This is a sample page', self.get_text(self.header_locator), "Unexpected text!")
        print(self.get_text(self.header_locator))


