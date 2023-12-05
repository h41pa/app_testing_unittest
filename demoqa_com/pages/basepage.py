from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_url(self, url: str):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def get_title_page(self):
        return self.driver.title

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def wait_for_visible_element(self, locator: tuple, time: int = 5):
        wait = WebDriverWait(self.driver, time)
        wait.until(EC.visibility_of_element_located(locator), 'Element not visible!')

    def type(self, locator: tuple, message: str, time: int = 5):
        self.wait_for_visible_element(locator, time)
        self.find(locator).send_keys(message)

    def click(self, locator: tuple, time: int = 5):
        self.wait_for_visible_element(locator, time)
        self.find(locator).click()

    def get_text(self, locator: tuple, time: int = 5):
        self.wait_for_visible_element(locator, time)
        return self.find(locator).text

    def is_displayed(self, locator: tuple, time: int = 5):
        try:
            self.wait_for_visible_element(locator, time)
            return self.find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def is_selected(self, locator: tuple, time: int=5):
        self.wait_for_visible_element(locator, time)
        return self.find(locator).is_selected()