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

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_windows(self):
        self.driver.get('https://omayo.blogspot.com/')

        main_window = self.driver.current_window_handle

        self.driver.find_element(By.XPATH, '//*[@id="HTML37"]/div[1]/p/a').click()

        all_windows = self.driver.window_handles

        for w in all_windows:
            self.driver.switch_to.window(w)
            if self.driver.title.__eq__('New Window'):
                para = self.driver.find_element(By.XPATH, "//h3").text
                print(para)
                self.driver.close()
                break

        self.driver.switch_to.window(main_window)
        self.driver.find_element(By.XPATH, '//*[@id="ta1"]').send_keys('laaaaaaaaaaaa')
        time.sleep(3)
