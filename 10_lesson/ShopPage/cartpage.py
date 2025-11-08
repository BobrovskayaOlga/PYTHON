from selenium.webdriver.common.by import By
from basepage import BasePage
from checkoutpage import CheckoutPage
import allure

class CartPage(BasePage):
    """
    Класс для работы со страницей корзины SauceDemo.
    """
    
    CART_TITLE = (By.CLASS_NAME, "title")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    
    def __init__(self, driver):
        """
        Инициализация страницы корзины.
        
        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        super().__init__(driver)
        self.find_element(*self.CART_TITLE)
    
    @allure.step("Нажать кнопку оформления заказа")
    def click_checkout(self):
        """
        Нажатие кнопки оформления заказа.
        
        Returns:
            CheckoutPage: экземпляр страницы оформления заказа
        """
        self.find_clickable_element(*self.CHECKOUT_BUTTON).click()
        return CheckoutPage(self.driver)
    
    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self):
        """
        Получение количества товаров в корзине.
        
        Returns:
            int: количество товаров в корзине
        """
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
    
    @allure.step("Продолжить покупки")
    def continue_shopping(self):
        """
        Нажатие кнопки продолжения покупок.
        
        Returns:
            CartPage: текущий экземпляр страницы для цепочки вызовов
        """
        self.find_clickable_element(*self.CONTINUE_SHOPPING_BUTTON).click()
        return self
