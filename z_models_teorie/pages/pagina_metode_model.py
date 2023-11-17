from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class PaginaMetode:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def deschide_pagina(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def introdu_username(self, username: str):
        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys(username)

    def introdu_parola(self, password: str):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys(password)

    def apasa_autentificare(self):
        login_button = self.driver.find_element(By.CSS_SELECTOR, "#login > button")
        login_button.click()
