import pytest
import allure
import sys
import os

# Добавляем текущую директорию в путь Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from selenium import webdriver
from formpage import FormPage

@allure.feature("Валидация формы")
class TestFormValidation:
    
    @allure.title("Тест валидации формы с пустым ZIP-кодом")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка, что при пустом ZIP-коде поле подсвечивается красным, а остальные - зеленым")
    def test_form_validation_empty_zip(self):
        """Тест валидации формы с пустым ZIP-кодом"""
        driver = webdriver.Chrome()
        
        try:
            with allure.step("Инициализация страницы формы"):
                form_page = FormPage(driver)
                allure.attach(driver.get_screenshot_as_png(), name="page_loaded", 
                            attachment_type=allure.attachment_type.PNG)
            
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
            
            with allure.step("Заполнение формы тестовыми данными"):
                form_page.fill_all_fields(form_data)
                allure.attach(driver.get_screenshot_as_png(), name="form_filled", 
                            attachment_type=allure.attachment_type.PNG)
            
            with allure.step("Отправка формы"):
                form_page.submit_form()
            
            with allure.step("Проверка валидации полей"):
                with allure.step("Проверить, что поле ZIP-code подсвечено красным"):
                    form_page.verify_zip_code_error()
                
                with allure.step("Проверить, что все остальные поля подсвечены зеленым"):
                    form_page.verify_valid_fields_success()
                
                allure.attach(driver.get_screenshot_as_png(), name="validation_result", 
                            attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), name="error_screenshot", 
                        attachment_type=allure.attachment_type.PNG)
            raise
        finally:
            driver.quit()
    
    @allure.title("Тест валидации формы с валидным ZIP-кодом")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка, что при валидном ZIP-коде все поля подсвечиваются зеленым")
    def test_form_validation_valid_zip(self):
        """Тест с валидным ZIP-кодом"""
        driver = webdriver.Chrome()
        
        try:
            with allure.step("Инициализация страницы формы"):
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
            
            with allure.step("Заполнение формы с валидным ZIP-кодом"):
                form_page.fill_all_fields(form_data).submit_form()
            
            with allure.step("Проверка, что все поля подсвечены зеленым"):
                form_page.verify_valid_fields_success(exclude_fields=[])
                
            allure.attach(driver.get_screenshot_as_png(), name="all_green_validation", 
                        attachment_type=allure.attachment_type.PNG)
            
        except Exception as e:
            allure.attach(driver.get_screenshot_as_png(), name="error_valid_zip", 
                        attachment_type=allure.attachment_type.PNG)
            raise
        finally:
            driver.quit()

@allure.feature("Базовые проверки")
class TestBasicFunctionality:
    
    @allure.title("Проверка открытия страницы")
    @allure.severity(allure.severity_level.MINOR)
    def test_page_opens(self):
        """Проверка что страница открывается"""
        driver = webdriver.Chrome()
        try:
            with allure.step("Открытие страницы формы"):
                form_page = FormPage(driver)
            
            with allure.step("Проверка заголовка страницы"):
                # Проверяем что страница загрузилась (любой заголовок)
                assert driver.title != "", "Заголовок страницы пустой"
                print(f"Заголовок страницы: {driver.title}")
                
            allure.attach(driver.get_screenshot_as_png(), name="page_opened", 
                        attachment_type=allure.attachment_type.PNG)
            
        finally:
            driver.quit()

if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
