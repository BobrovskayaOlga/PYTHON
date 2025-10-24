from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firefox_options = Options()
driver = webdriver.Firefox(options=firefox_options)

try:
    driver.get("https://www.saucedemo.com/")
    
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "user-name"))
    )
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")
    
    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()
    
    backpack_add = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    backpack_add.click()
    
    tshirt_add = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    tshirt_add.click()
    
    onesie_add = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    onesie_add.click()
    
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()
    
    checkout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout_button.click()
    
    first_name_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    first_name_field.send_keys("Ольга")
    
    last_name_field = driver.find_element(By.ID, "last-name")
    last_name_field.send_keys("Бобровская")
    
    postal_code_field = driver.find_element(By.ID, "postal-code")
    postal_code_field.send_keys("309501")
    
    continue_button = driver.find_element(By.ID, "continue")
    continue_button.click()
    
    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text
    total_value = total_text.replace("Total: $", "")
    
    expected_total = "$58.29"
    actual_total = f"${total_value}"
    
    if actual_total == expected_total:
        print(f"✓ ТЕСТ ПРОЙДЕН: Итоговая сумма корректна - {actual_total}")
    else:
        print(f"✗ ТЕСТ НЕ ПРОЙДЕН: Ожидалось {expected_total}, получено {actual_total}")
    
finally:
    driver.quit()
