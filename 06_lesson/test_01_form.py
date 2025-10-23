from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    wait = WebDriverWait(driver, 10)

    elements = [
        ("first-name", "Иван"),
        ("last-name", "Петров"),
        ("address", "Москва"),
        ("zip-code", ""),
        ("city", "Москва"),
        ("country", "Россия"),
        ("e-mail", "ivan@test.ru"),
        ("phone", "+79991234567"),
        ("job-position", "QA"),
        ("company", "SkyPro")
    ]

    for name, value in elements:
        input_field = wait.until(EC.presence_of_element_located((By.NAME, name)))
        input_field.clear()
        input_field.send_keys(value)

    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code.alert-danger")))

    zip_code_field = driver.find_element(By.ID, "zip-code")
    zip_code_classes = zip_code_field.get_attribute("class")
    
    assert "alert-danger" in zip_code_classes

    field_ids = ["first-name", "last-name", "address", "city", "country", 
                "e-mail", "phone", "job-position", "company"]
    
    for field_id in field_ids:
        field = driver.find_element(By.ID, field_id)
        field_classes = field.get_attribute("class")
        
        assert "alert-success" in field_classes

    print("Тест пройден успешно: все цвета границ установлены корректно!")

except Exception as e:
    print(f"Произошла ошибка: {e}")
    raise
    
finally:
    driver.quit()
