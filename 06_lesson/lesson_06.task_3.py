from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = ChromeService(executable_path=ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 30)

try:
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
    
    wait.until(EC.invisibility_of_element_located((By.ID, 'spinner')))
    
    images = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '#image-container img'))
    )
    
    wait.until(lambda driver: images[2].get_attribute('src') and 
               images[2].get_attribute('src') != '')
    
    third_image_src = images[2].get_attribute('src')
    print(f'Значение атрибута src у третьей картинки: {third_image_src}')
        
finally:
    driver.quit()