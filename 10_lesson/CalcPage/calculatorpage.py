from selenium.webdriver.common.by import By
from basepage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class CalculatorPage(BasePage):
    """Класс для работы со страницей калькулятора"""
    
    # Локаторы элементов
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CLASS_NAME, "screen")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    
    def __init__(self, driver) -> None:
        """
        Инициализация страницы калькулятора
        
        Args:
            driver: WebDriver экземпляр
        """
        super().__init__(driver)
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    @allure.step("Установить задержку вычислений: {delay_seconds} секунд")
    def set_delay(self, delay_seconds: int) -> 'CalculatorPage':
        """
        Установка задержки вычислений
        
        Args:
            delay_seconds: количество секунд задержки
            
        Returns:
            CalculatorPage: текущий экземпляр страницы
        """
        delay_input = self.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(delay_seconds))
        return self
    
    @allure.step("Нажать кнопку '7'")
    def click_button_7(self) -> 'CalculatorPage':
        """
        Нажатие кнопки 7
        
        Returns:
            CalculatorPage: текущий экземпляр страницы
        """
        self.find_clickable_element(*self.BUTTON_7).click()
        return self
    
    @allure.step("Нажать кнопку '8'")
    def click_button_8(self) -> 'CalculatorPage':
        """
        Нажатие кнопки 8
        
        Returns:
            CalculatorPage: текущий экземпляр страницы
        """
        self.find_clickable_element(*self.BUTTON_8).click()
        return self
    
    @allure.step("Нажать кнопку '+'")
    def click_plus(self) -> 'CalculatorPage':
        """
        Нажатие кнопки +
        
        Returns:
            CalculatorPage: текущий экземпляр страницы
        """
        self.find_clickable_element(*self.BUTTON_PLUS).click()
        return self
    
    @allure.step("Нажать кнопку '='")
    def click_equals(self) -> 'CalculatorPage':
        """
        Нажатие кнопки =
        
        Returns:
            CalculatorPage: текущий экземпляр страницы
        """
        self.find_clickable_element(*self.BUTTON_EQUALS).click()
        return self
    
    @allure.step("Ожидать результат: {expected_result}")
    def wait_for_result(self, expected_result: str, timeout: int = 50) -> 'CalculatorPage':
        """
        Ожидание появления результата на экране
        
        Args:
            expected_result: ожидаемый результат
            timeout: время ожидания в секундах
            
        Returns:
            CalculatorPage: текущий экземпляр страницы
        """
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.SCREEN, str(expected_result)))
        return self
    
    @allure.step("Получить текст с экрана калькулятора")
    def get_screen_text(self) -> str:
        """
        Получение текста с экрана калькулятора
        
        Returns:
            str: текст с экрана калькулятора
        """
        screen_element = self.find_element(*self.SCREEN)
        return screen_element.text
    
    @allure.step("Выполнить операцию 7 + 8 с задержкой {delay_seconds} секунд")
    def perform_calculation(self, delay_seconds: int = 45) -> 'CalculatorPage':
        """
        Выполнение полной операции вычисления 7 + 8
        
        Args:
            delay_seconds: задержка вычислений в секундах
            
        Returns:
            CalculatorPage: текущий экземпляр страницы
        """
        return (self.set_delay(delay_seconds)
                   .click_button_7()
                   .click_plus()
                   .click_button_8()
                   .click_equals())
