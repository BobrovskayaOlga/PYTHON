from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    """
    Базовый класс для всех страниц, содержащий общие методы работы с веб-элементами.
    """
    
    def __init__(self, driver):
        """
        Инициализация базовой страницы.
        
        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Найти элемент с локатором {by} = '{value}'")
    def find_element(self, by, value):
        """
        Поиск элемента с ожиданием его появления на странице.
        
        Args:
            by: метод поиска (By.ID, By.XPATH, By.CSS_SELECTOR, etc.)
            value: значение локатора для поиска элемента
            
        Returns:
            WebElement: найденный веб-элемент
        """
        return self.wait.until(EC.presence_of_element_located((by, value)))
    
    @allure.step("Найти кликабельный элемент с локатором {by} = '{value}'")
    def find_clickable_element(self, by, value):
        """
        Поиск кликабельного элемента с ожиданием возможности взаимодействия.
        
        Args:
            by: метод поиска (By.ID, By.XPATH, By.CSS_SELECTOR, etc.)
            value: значение локатора для поиска элемента
            
        Returns:
            WebElement: найденный кликабельный веб-элемент
        """
        return self.wait.until(EC.element_to_be_clickable((by, value)))
