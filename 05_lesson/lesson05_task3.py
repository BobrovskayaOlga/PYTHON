from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


driver.get("http://the-internet.herokuapp.com/inputs")

try:
 
    wait = WebDriverWait(driver, 10)

    input_field = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="number"]'))
    )
    
  
    input_field.send_keys('Sky')
    
    time.sleep(5)
    
    input_field.clear()
    
    time.sleep(5)
   
    input_field.send_keys('Pro')


finally:
    
    driver.quit()