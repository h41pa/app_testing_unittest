from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://webflow.com/made-in-webflow/links')
driver.implicitly_wait(5)
links = driver.find_elements(By.XPATH, "//a[@class='--pick-UQdGt --styled-drnMLX wf-1etior2']")
for i in links:
    print(i.get_attribute('href'))
