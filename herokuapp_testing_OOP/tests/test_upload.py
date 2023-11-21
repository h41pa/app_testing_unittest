import time
import os
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from herokuapp_testing_OOP.pages.base_page import BasePage
from selenium.webdriver import Keys, ActionChains


class TestUpload(unittest.TestCase, BasePage):
    LINK = "https://the-internet.herokuapp.com/upload"
    header_title_locator = (By.CSS_SELECTOR, "#content > div.example > h3")
    select_file_locator = (By.ID, "file-upload")
    upload_locator = (By.ID, "file-submit")
    failed_upload_header_locator = (By.CSS_SELECTOR, "body > h1")
    upload_successful_header_locator = (By.CSS_SELECTOR, "#content > div > h3")
    upload_successful_filename_locator = (By.XPATH, "//div[@id='uploaded-files']")
    # text
    expected_title = "File Uploader"
    expected_successful_upload_header_text = "File Uploaded!"
    expected_successful_upload_filename_text = "proba.txt"
    expected_unsuccessful_upload_text = "Internal Server Error"

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_title(self):
        self.assertEqual(self.expected_title, self.get_text(self.header_title_locator), "Unexpected title")

    def test_successful_upload(self):
        file_path = os.path.abspath('proba.txt')
        self.type(self.select_file_locator, file_path)
        self.click(self.upload_locator)
        time.sleep(3)
        self.assertEqual(self.expected_successful_upload_header_text, self.get_text(self.upload_successful_header_locator), "Error, file not uploaded")
        self.assertEqual(self.expected_successful_upload_filename_text, self.get_text(self.upload_successful_filename_locator),"Error, seems to upload different file." )

    def test_unsuccessful_upload(self):
        self.click(self.upload_locator)
        time.sleep(3)
        self.assertEqual(self.expected_unsuccessful_upload_text, self.get_text(self.failed_upload_header_locator), "Error, file seems to not failed")




