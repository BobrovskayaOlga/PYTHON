import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LoginPage import LoginPage

class TestSauceDemo:
    def test_complete_purchase_flow(self):
        driver = webdriver.Chrome()
        
        try:
            login_page = LoginPage(driver)
            inventory_page = login_page.login_as_standard_user()
            
            inventory_page.add_product_to_cart("Sauce Labs Backpack")
            inventory_page.add_product_to_cart("Sauce Labs Bolt T-Shirt")
            inventory_page.add_product_to_cart("Sauce Labs Onesie")
            
            assert inventory_page.get_cart_items_count() == 3
            
            cart_page = inventory_page.go_to_cart()
            
            checkout_page = cart_page.click_checkout()
            
            checkout_page.fill_checkout_info("John", "Doe", "12345")
            
            total_amount = checkout_page.get_total_amount()
            assert total_amount == "58.29", f"Expected $58.29, but got ${total_amount}"
            
            print(f"Тест пройден! Итоговая сумма: ${total_amount}")
        finally:
            driver.quit()
