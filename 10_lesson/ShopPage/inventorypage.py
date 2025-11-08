from selenium.webdriver.common.by import By
from basepage import BasePage
from cartpage import CartPage
import allure

class InventoryPage(BasePage):
    """
    Класс для работы со страницей инвентаря товаров SauceDemo.
    """
    
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART = (By.CLASS_NAME, "shopping_cart_link")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    
    def __init__(self, driver):
        """
        Инициализация страницы инвентаря.
        
        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        super().__init__(driver)
        self.find_element(*self.PRODUCTS_TITLE)
    
    def get_product_button(self, product_name):
        """
        Получение локатора кнопки добавления товара по названию.
        
        Args:
            product_name: название товара
            
        Returns:
            tuple: локатор кнопки добавления товара в корзину
        """
        return (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
    
    @allure.step("Добавить товар '{product_name}' в корзину")
    def add_product_to_cart(self, product_name):
        """
        Добавление товара в корзину по названию.
        
        Args:
            product_name: название товара для добавления
            
        Returns:
            InventoryPage: текущий экземпляр страницы для цепочки вызовов
        """
        add_button = self.find_clickable_element(*self.get_product_button(product_name))
        
        # Проверяем текст кнопки - если "Remove", значит товар уже в корзине
        button_text = add_button.text
        if button_text.upper() == "REMOVE":
            print(f"⚠️ Товар '{product_name}' уже в корзине, пропускаем добавление")
            return self
        
        # Если кнопка "Add to cart", кликаем для добавления
        add_button.click()
        print(f"✅ Товар '{product_name}' добавлен в корзину")
        return self
    
    @allure.step("Удалить товар '{product_name}' из корзины")
    def remove_product_from_cart(self, product_name):
        """
        Удаление товара из корзины по названию.
        
        Args:
            product_name: название товара для удаления
            
        Returns:
            InventoryPage: текущий экземпляр страницы для цепочки вызовов
        """
        remove_button = self.find_clickable_element(*self.get_product_button(product_name))
        
        # Проверяем текст кнопки - если "Add to cart", значит товара нет в корзине
        button_text = remove_button.text
        if button_text.upper() == "ADD TO CART":
            print(f"⚠️ Товар '{product_name}' не в корзине, пропускаем удаление")
            return self
        
        # Если кнопка "Remove", кликаем для удаления
        remove_button.click()
        print(f"✅ Товар '{product_name}' удален из корзины")
        return self
    
    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self):
        """
        Получение количества товаров в корзине из бейджа.
        
        Returns:
            int: количество товаров в корзине
        """
        try:
            badge = self.find_element(*self.SHOPPING_CART_BADGE)
            return int(badge.text)
        except:
            return 0
    
    @allure.step("Перейти в корзину")
    def go_to_cart(self):
        """
        Переход на страницу корзины.
        
        Returns:
            CartPage: экземпляр страницы корзины
        """
        self.find_clickable_element(*self.SHOPPING_CART).click()
        return CartPage(self.driver)
