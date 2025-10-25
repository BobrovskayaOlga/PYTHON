from selenium.webdriver.common.by import By
from BasePage import BasePage
from CartPage import CartPage

class InventoryPage(BasePage):
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    
    def get_product_button(self, product_name):
        return (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.find_element(*self.PRODUCTS_TITLE)
    
    def add_product_to_cart(self, product_name):
        add_button = self.find_clickable_element(*self.get_product_button(product_name))
        add_button.click()
        return self
    
    def get_cart_items_count(self):
        try:
            badge = self.find_element(*self.SHOPPING_CART_BADGE)
            return int(badge.text)
        except:
            return 0
    
    def go_to_cart(self):
        self.find_clickable_element(*self.SHOPPING_CART).click()
        return CartPage(self.driver)
