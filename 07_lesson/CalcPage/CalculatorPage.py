from selenium.webdriver.common.by import By
from BasePage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage(BasePage):
    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CLASS_NAME, "screen")
    
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    def set_delay(self, delay_seconds):
        """Установка задержки вычислений"""
        delay_input = self.find_element(*self.DELAY_INPUT)
        delay_input.clear()
        delay_input.send_keys(str(delay_seconds))
        return self
    
    def click_button_7(self):
        """Нажатие кнопки 7"""
        self.find_clickable_element(*self.BUTTON_7).click()
        return self
    
    def click_button_8(self):
        """Нажатие кнопки 8"""
        self.find_clickable_element(*self.BUTTON_8).click()
        return self
    
    def click_plus(self):
        """Нажатие кнопки +"""
        self.find_clickable_element(*self.BUTTON_PLUS).click()
        return self
    
    def click_equals(self):
        """Нажатие кнопки ="""
        self.find_clickable_element(*self.BUTTON_EQUALS).click()
        return self
    
    def wait_for_result(self, expected_result, timeout=50):
        """Ожидание появления результата на экране"""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.text_to_be_present_in_element(self.SCREEN, str(expected_result)))
        return self
    
    def get_screen_text(self):
        """Получение текста с экрана калькулятора"""
        screen_element = self.find_element(*self.SCREEN)
        return screen_element.text
    
    def perform_calculation(self, delay_seconds=45):
        """Выполнение полной операции вычисления 7 + 8"""
        return (self.set_delay(delay_seconds)
                   .click_button_7()
                   .click_plus()
                   .click_button_8()
                   .click_equals())
