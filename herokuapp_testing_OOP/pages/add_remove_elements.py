from selenium.webdriver.common.by import By

from herokuapp_testing_OOP.pages.base_page import BasePage


class AddRemoveElementsPage(BasePage):
    # Link
    URL = "https://the-internet.herokuapp.com/add_remove_elements/"

    # Locators
    ADD_ELEMENT = (By.XPATH, "//button[@onclick='addElement()']")
    DELETE_ELEMENT = (By.XPATH, "//button[@onclick='deleteElement()']")
    HEADER_TEXT_LOCATOR = (By.XPATH, "//h3")

    # text
    EXPECTED_HEADER_TEXT = "Add/Remove Elements"

    def __init__(self, driver):
        super().__init__(driver)

    def load_page(self):
        self.open_url(self.URL)

    def get_header_text(self):
        return self.get_text(self.HEADER_TEXT_LOCATOR)

    def add_element(self, nr: int):
        for i in range(0, nr):
            self.click(self.ADD_ELEMENT)

    def delete_button(self):
        self.click(self.DELETE_ELEMENT)

    def is_delete_button_displayed(self):
        return self.is_displayed(self.DELETE_ELEMENT)

    def get_number_of_delete_buttons(self):
        return len(self.driver.find_elements(*self.DELETE_ELEMENT))