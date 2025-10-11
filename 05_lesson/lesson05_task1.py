from selenium import webdriver
from selenium.webdriver.common.by import By 
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("http://uitestingplayground.com/classattr")

button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()


sleep(60)

