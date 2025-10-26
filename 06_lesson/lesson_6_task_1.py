from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


brauser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

brauser.get("http://uitestingplayground.com/ajax")

wait = WebDriverWait(brauser, 10)
button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary")))
button.click()
wait = WebDriverWait(brauser, 20)
success_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'bg-success' )))

print(success_message.text)

