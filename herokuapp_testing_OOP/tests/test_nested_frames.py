import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from herokuapp_testing_OOP.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class TestNestedFrames(unittest.TestCase, BasePage):
    LINK = "https://the-internet.herokuapp.com/nested_frames"
    body_locator_for_all = (By.TAG_NAME, "body")
    frame_top = 'frame-top'
    frame_left = 'frame-left'
    frame_middle = 'frame-middle'
    frame_right = 'frame-right'
    frame_bottom = 'frame-bottom'

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(self.LINK)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def test_nested_frames_moving_to_top_left_middle_right(self):
        # moving to top frame then to left then back to parent(top) and doing same for middle and right
        self.driver.switch_to.frame(self.frame_top)
        self.driver.switch_to.frame(self.frame_left)
        self.assertEqual("LEFT", self.get_text(self.body_locator_for_all))
        print(self.get_text(self.body_locator_for_all))
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(self.frame_middle)
        self.assertEqual("MIDDLE", self.get_text(self.body_locator_for_all))
        print(self.get_text(self.body_locator_for_all))
        self.driver.switch_to.parent_frame()
        self.driver.switch_to.frame(self.frame_right)
        self.assertEqual("RIGHT", self.get_text(self.body_locator_for_all))
        print(self.get_text(self.body_locator_for_all))
        time.sleep(5)

    def test_nested_frames_moving_top_bottom(self):
        self.driver.switch_to.frame(self.frame_bottom)
        print(self.get_text(self.body_locator_for_all))

