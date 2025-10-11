from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

driver.get("http://the-internet.herokuapp.com/login")

wait = WebDriverWait(driver, 10)

username_input = wait.until(
    EC.presence_of_element_located((By.ID, 'username'))
)
username_input.send_keys('tomsmith')
time.sleep(5)

password_input = wait.until(
    EC.presence_of_element_located((By.ID, 'password'))
)
password_input.send_keys('SuperSecretPassword!')
time.sleep(5)

login_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
)
login_button.click()

success_message = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'flash.success'))
)
print(success_message.text.strip())

try:
    pass
except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()
   