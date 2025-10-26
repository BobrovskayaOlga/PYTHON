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
            
            assert result == "15"
        finally:
            driver.quit()
    