from selenium.webdriver.common.by import By
from BasePage import BasePage
from InventoryPage import InventoryPage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://www.saucedemo.com/")
    
    def enter_username(self, username):
        username_field = self.find_element(*self.USERNAME_INPUT)
        username_field.clear()
        username_field.send_keys(username)
        return self
    
    def enter_password(self, password):
        password_field = self.find_element(*self.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)
        return self
    
    def click_login(self):
        self.find_clickable_element(*self.LOGIN_BUTTON).click()
        return InventoryPage(self.driver)
    
    def login_as_standard_user(self):
        return self.enter_username("standard_user")\
                   .enter_password("secret_sauce")\

