import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from demoqa_com.pages.basepage import BasePage


class TestCheckboxes(unittest.TestCase, BasePage):
    LINK = 'https://demoqa.com/checkbox'
    home_box = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/label')
    home_checkbox = (By.CSS_SELECTOR, '#tree-node > ol > li > span > label > span.rct-checkbox > svg')
    result = (By.ID, 'result')
    colapse = (By.CSS_SELECTOR, '#tree-node > div > button.rct-option.rct-option-expand-all > svg')
    items = (By.XPATH, '//*[@id="tree-node"]/ol/li')
    documents_box = (By.XPATH, '//*[@id="tree-node"]/ol/li/ol/li[2]/span/label')
    document_checkbox = (By.CSS_SELECTOR, '#tree-node > ol > li > ol > li:nth-child(2) > span > label > span.rct-checkbox > svg')
    excel_loc = (By.XPATH, '//span[text()="Excel File.doc"]')
    angular = (By.XPATH, '//span[text()="Angular"]')

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_home_checkbox(self):
        self.click(self.home_box)
        self.assertIn('rct-icon rct-icon-check', self.find(self.home_checkbox).get_attribute('class'),'Unxpected message')
        self.assertIn('You have selected :', self.get_text(self.result), 'Unexpected result!')
        self.click(self.home_box)
        self.assertIn('rct-icon rct-icon-uncheck', self.find(self.home_checkbox).get_attribute('class'), 'Unxpected message')


    def test_box_items(self):
        self.click(self.colapse)
        self.click(self.documents_box)
        self.assertIn('rct-icon rct-icon-check', self.find(self.document_checkbox).get_attribute('class'),'Unxpected message')
        time.sleep(2)
        self.assertIn('documents', self.get_text(self.result), 'Unexpected result!')

    def test_excel_angular(self):
        self.click(self.colapse)
        time.sleep(3)
        self.click(self.excel_loc)
        self.click(self.angular)
        assert 'angular' and 'excelFile' in self.get_text(self.result), 'Not expected response'
        print(self.get_text(self.result))
