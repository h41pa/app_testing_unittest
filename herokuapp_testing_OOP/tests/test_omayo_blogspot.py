import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from herokuapp_testing_OOP.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class TestSelected(unittest.TestCase, BasePage):

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

    def test_select_option(self):
        self.driver.get('https://omayo.blogspot.com/')
        select_menu = self.driver.find_element(By.ID, 'drop1')
        select = Select(select_menu)
        select.select_by_index(3)
        time.sleep(2)
        assert 'doc 3' == select.first_selected_option.text, "Error"
        print(select.first_selected_option.text)

    def test_select_multiple(self):
        self.driver.get('https://omayo.blogspot.com/')
        select_menu = self.driver.find_element(By.ID, 'multiselect1')
        select = Select(select_menu)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL)
        actions.click(select.select_by_visible_text('Volvo'))
        actions.click(select.select_by_visible_text('Swift'))
        actions.key_up(Keys.CONTROL)
        actions.perform()
        time.sleep(3)
        # selected_options = [option.text for option in select.all_selected_options]
        selected_options = []
        for option in select.all_selected_options:
            selected_options.append(option.text)

        assert 'Volvo' in selected_options
        assert 'Swift' in selected_options


    def test_disabled(self):
        self.driver.get('https://omayo.blogspot.com/')
        box = self.driver.find_element(By.XPATH, '//*[@id="tb2"]')
        self.assertFalse(box.is_enabled())


    def test_text_box(self):
        self.driver.get('https://omayo.blogspot.com/')
        trt = self.driver.find_element(By.ID, 'textbox1')
        trt.clear()
        time.sleep(2)
        trt.send_keys('helooooo')
        trt.send_keys(Keys.CONTROL, 'A')
        time.sleep(2)
        trt.send_keys(Keys.CONTROL, 'c')
        trt.clear()
        time.sleep(2)
        trt.send_keys(Keys.CONTROL, 'V')
        time.sleep(2)

    def test_Multi_Selection_box(self):
        self.driver.get('https://omayo.blogspot.com/')
        select_menu = self.driver.find_element(By.ID, 'multiselect1')
        select = Select(select_menu)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.CONTROL)
        actions.click(select.select_by_visible_text('Volvo'))
        actions.click(select.select_by_visible_text('Swift'))
        time.sleep(2)
        assert 2 == len(select.all_selected_options), 'Not same'
        actions.click(select.select_by_visible_text('Audi'))
        assert 3 == len(select.all_selected_options), 'Not same'
        actions.click(select.deselect_all())
        assert len(select.all_selected_options) == 0, 'Not same'
        actions.perform()
        time.sleep(2)



