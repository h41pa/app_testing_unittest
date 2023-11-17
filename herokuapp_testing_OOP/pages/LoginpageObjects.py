from selenium.webdriver.common.by import By


class LoginPageObjects:
    # login url and locators
    login_link = "https://the-internet.herokuapp.com/login"
    username_locator = (By.XPATH, "//input[@name='username']")
    password_locator = (By.XPATH, "//input[@name='password']")
    login_button_locator = (By.XPATH, "//i[@class='fa fa-2x fa-sign-in']")
    flash_error = (By.ID, "flash")
    # text for logging
    valid_username = "tomsmith"
    valid_password = "SuperSecretPassword!"
    invalid_username = "tomsmith1"
    invalid_password = "SuperSecretPassword111"
    expected_invalid_text_password = "Your password is invalid!"
    expected_invalid_text_username = "Your username is invalid!"
    # secure page url and locators
    secure_page_url = "https://the-internet.herokuapp.com/secure"
    logout_button = (By.CLASS_NAME, "icon-signout")
    secure_are_locator = (By.CSS_SELECTOR, "#content h2")
    expected_header_text = "Secure Area"
