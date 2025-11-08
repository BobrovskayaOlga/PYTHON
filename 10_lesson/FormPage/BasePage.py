from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    @allure.step("Найти элемент с локатором {by} = '{value}'")
    def find_element(self, by, value):
        return self.wait.until(EC.presence_of_element_located((by, value)))
    
    @allure.step("Найти кликабельный элемент с локатором {by} = '{value}'")
    def find_clickable_element(self, by, value):
        return self.wait.until(EC.element_to_be_clickable((by, value)))
