from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from CalculatorPage import CalculatorPage
class TestSlowCalculator:
    def test_slow_calculator(self):
        """Тест проверяет работу калькулятора с задержкой"""
        driver = webdriver.Chrome()
        
        try:

            calculator_page = CalculatorPage(driver)
            
            calculator_page.perform_calculation(45)
        
            calculator_page.wait_for_result("15", timeout=50)
            
            result = calculator_page.get_screen_text()
            
            assert result == "15", f"Ожидался результат '15', но получено '{result}'"
            print(f"✅ Тест пройден! Результат: {result}")
            
        except Exception as e:
            print(f"❌ Ошибка в тесте: {e}")
            driver.save_screenshot("calculator_error.png")
            raise
        finally:
            driver.quit()
    
    def test_slow_calculator_with_different_delay(self):
        """Тест с другой задержкой для демонстрации гибкости"""
        driver = webdriver.Chrome()
        
        try:
            calculator_page = CalculatorPage(driver)
            
            calculator_page.perform_calculation(5)
            
            calculator_page.wait_for_result("15", timeout=10)
            
            result = calculator_page.get_screen_text()
            
            assert result == "15", f"Ожидался результат '15', но получено '{result}'"
            print(f"✅ Тест с задержкой 5с пройден! Результат: {result}")
            
        finally:
            driver.quit()
