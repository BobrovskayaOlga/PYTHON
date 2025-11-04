from selenium.webdriver.common.by import By
from basepage import BasePage
from inventorypage import InventoryPage
import allure

class LoginPage(BasePage):
    """
    Класс для работы со страницей авторизации SauceDemo.
    """
    
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        """
        Инициализация страницы авторизации.
        
        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com/")
    
    @allure.step("Ввести имя пользователя: '{username}'")
    def enter_username(self, username):
        """
        Ввод имени пользователя в поле ввода.
        
        Args:
            username: имя пользователя для ввода
            
        Returns:
            LoginPage: текущий экземпляр страницы для цепочки вызовов
        """
        username_field = self.find_element(*self.USERNAME_INPUT)
        username_field.clear()
        username_field.send_keys(username)
        return self
    
    @allure.step("Ввести пароль")
    def enter_password(self, password):
        """
        Ввод пароля в поле ввода.
        
        Args:
            password: пароль для ввода
            
        Returns:
            LoginPage: текущий экземпляр страницы для цепочки вызовов
        """
        password_field = self.find_element(*self.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)
        return self
    
    @allure.step("Нажать кнопку входа")
    def click_login(self):
        """
        Нажатие кнопки входа в систему.
        
        Returns:
            InventoryPage: экземпляр страницы инвентаря после успешного входа
        """
        self.find_clickable_element(*self.LOGIN_BUTTON).click()
        return InventoryPage(self.driver)
    
    @allure.step("Авторизоваться как стандартный пользователь")
    def login_as_standard_user(self):
        """
        Полная авторизация под стандартным пользователем.
        
        Returns:
            InventoryPage: экземпляр страницы инвентаря после успешного входа
        """
        return (self.enter_username("standard_user")
                   .enter_password("secret_sauce")
                   .click_login())
    
    @allure.step("Получить текст сообщения об ошибке")
    def get_error_message(self):
        """
        Получение текста сообщения об ошибке авторизации.
        
        Returns:
            str: текст сообщения об ошибке
        """
        error_element = self.find_element(*self.ERROR_MESSAGE)
        return error_element.text
