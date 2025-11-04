from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from calculatorpage import CalculatorPage
import allure
import pytest

@allure.feature("Калькулятор с задержкой")
@allure.severity(allure.severity_level.CRITICAL)
class TestSlowCalculator:
    
    @allure.title("Тест работы калькулятора с задержкой вычислений")
    @allure.description("""
    Этот тест проверяет корректность работы калькулятора 
    с установленной задержкой вычислений.
    
    Шаги теста:
    1. Открыть страницу калькулятора
    2. Установить задержку 45 секунд
    3. Выполнить операцию 7 + 8
    4. Дождаться результата
    5. Проверить, что результат равен 15
    """)
    def test_slow_calculator(self):
        driver = webdriver.Chrome()
        
        try:
            with allure.step("Инициализация страницы калькулятора"):
                calculator_page = CalculatorPage(driver)
            
            with allure.step("Выполнение операции 7 + 8 с задержкой 45 секунд"):
                calculator_page.perform_calculation(45)
        
            with allure.step("Ожидание результата вычислений"):
                calculator_page.wait_for_result("15", timeout=50)
            
            with allure.step("Получение результата с экрана"):
                result = calculator_page.get_screen_text()
            
            with allure.step("Проверка корректности результата"):
                assert result == "15", f"Ожидался результат '15', но получен '{result}'"
                
        finally:
            with allure.step("Закрытие браузера"):
                driver.quit()
