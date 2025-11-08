from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver: webdriver.Chrome) -> None:
        """
        Базовый класс для всех страниц
        
        Args:
            driver: WebDriver экземпляр
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Найти элемент с локатором {by} = {value}")
    def find_element(self, by: By, value: str) -> WebDriverWait:
        """
        Поиск элемента с ожиданием его появления
        
        Args:
            by: метод поиска (By.ID, By.XPATH, etc.)
            value: значение локатора
            
        Returns:
            WebElement: найденный элемент
        """
        return self.wait.until(EC.presence_of_element_located((by, value)))
    
    @allure.step("Найти кликабельный элемент с локатором {by} = {value}")
    def find_clickable_element(self, by: By, value: str) -> WebDriverWait:
        """
        Поиск кликабельного элемента с ожиданием
        
        Args:
            by: метод поиска (By.ID, By.XPATH, etc.)
            value: значение локатора
            
        Returns:
            WebElement: найденный кликабельный элемент
        """
        return self.wait.until(EC.element_to_be_clickable((by, value)))
