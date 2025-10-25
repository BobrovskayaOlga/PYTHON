from selenium.webdriver.common.by import By
from BasePage import BasePage
from CheckoutPage import CheckoutPage
class CartPage(BasePage):
    CART_TITLE = (By.CLASS_NAME, "title")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.find_element(*self.CART_TITLE)
    
    def click_checkout(self):
        self.find_clickable_element(*self.CHECKOUT_BUTTON).click()
        return CheckoutPage(self.driver)
    
    def get_cart_items_count(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
