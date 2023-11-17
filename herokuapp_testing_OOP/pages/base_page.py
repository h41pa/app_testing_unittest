from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_url(self, url: str):
        self.driver.get(url)

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def type(self, locator: tuple, message: str):
        self.find(locator).send_keys(message)

    def get_text(self, locator: tuple):
        return self.find(locator).text

    def click(self, locator: tuple):
        self.find(locator).click()

    def is_displayed(self, locator: tuple):
        try:
            return self.find(locator).is_displayed()
        except NoSuchElementException:
            return False

    def get_current_url(self):
        return self.driver.current_url
