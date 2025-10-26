from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    browser.get("http://uitestingplayground.com/textinput")
    
    input_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]'))
    )
    
    input_field.send_keys('SkyPro')
    
    button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
    button.click()
    
    updated_button_text = button.text
    print(updated_button_text)
finally:
    
    browser.quit()
