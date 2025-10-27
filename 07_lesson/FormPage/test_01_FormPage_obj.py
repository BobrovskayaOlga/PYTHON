from selenium import webdriver
from FormPage import FormPage

class TestFormValidation:
    def test_form_validation(self):
        """Тест валидации формы с пустым ZIP-кодом"""
        driver = webdriver.Edge()
        
        try:
            form_page = FormPage(driver)
            
            form_data = {
                'first_name': 'Иван',
                'last_name': 'Петров', 
                'address': 'Ленина, 55-3',
                'email': 'test@skypro.com',
                'phone': '+7985899998787',
                'zip_code': '',
                'city': 'Москва',
                'country': 'Россия',
                'job_position': 'QA',
                'company': 'SkyPro'
            }
            
            print("1. Заполнение формы данными...")
            form_page.fill_all_fields(form_data)
            
            print("2. Отправка формы...")
            form_page.submit_form()
            
            print("3. Проверка валидации полей...")
            
            form_page.verify_zip_code_error()
            print("   ✅ Поле ZIP-code подсвечено красным (ошибка валидации)")
            
            form_page.verify_valid_fields_success()
            print("   ✅ Все остальные поля подсвечены зеленым (валидация пройдена)")
            
            print("✅ Тест пройден успешно!")
            
        except Exception as e:
            print(f"❌ Ошибка в тесте: {e}")
            driver.save_screenshot("form_validation_error.png")
            raise
        finally:
            driver.quit()
    
    def test_form_with_valid_zip_code(self):
        """Тест с валидным ZIP-кодом"""
        driver = webdriver.Edge()
        
        try:
            form_page = FormPage(driver)
            
            form_data = {
                'first_name': 'Иван',
                'last_name': 'Петров',
                'address': 'Ленина, 55-3',
                'email': 'test@skypro.com', 
                'phone': '+7985899998787',
                'zip_code': '123456',
                'city': 'Москва',
                'country': 'Россия',
                'job_position': 'QA',
                'company': 'SkyPro'
            }
            
            form_page.fill_all_fields(form_data).submit_form()
            
            form_page.verify_valid_fields_success(exclude_fields=[])
            print("✅ Тест с валидным ZIP-кодом пройден!")
            
        finally:
            driver.quit()

