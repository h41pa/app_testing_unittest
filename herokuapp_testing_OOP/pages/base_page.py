from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys, ActionChains


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

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def decline_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def type_alert_keys(self, message: str):
        alert = self.driver.switch_to.alert
        alert.send_keys(message)
        alert.accept()

    def get_number_of_elements(self, locator: tuple):
        return len(self.driver.find_elements(*locator))

    # def is_element_present(self, locator):
    #     return len(self.driver.find_elements(*locator)) > 0 # daca nu gaseste nimic returneaza o lista goala

    def check_checkbox(self, locator: tuple):
        checkbox_element = self.find(locator)
        if not checkbox_element.is_selected():
            self.click(locator)

    def uncheck_checkbox(self, locator: tuple):
        checkbox_element = self.find(locator)
        if checkbox_element.is_selected():
            self.click(locator)

    def is_selected(self, locator: tuple):
        return self.find(locator).is_selected()

    def select_option_by_text(self, locator: tuple, text: str):
        select = Select(self.find(locator))
        select.select_by_visible_text(text)

    def select_option_by_value(self, locator: tuple, value):
        Select(self.find(locator)).select_by_value(value)

    def move_to_element(self, locator):
        action_chains = ActionChains(self.driver)
        action_chains.move_to_element(self.find(locator)).click().perform()
        action_chains.context_click()
