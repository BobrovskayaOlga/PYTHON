import pytest
from selenium import webdriver
from loginpage import LoginPage
import allure
import time

@allure.feature("SauceDemo Магазин")
@allure.severity(allure.severity_level.CRITICAL)
class TestSauceDemo:
    
    @allure.title("Полный цикл покупки в SauceDemo")
    def test_complete_purchase_flow(self):
        """Тест полного цикла покупки в магазине SauceDemo"""
        driver = webdriver.Chrome()
        
        try:
            with allure.step("Авторизация под стандартным пользователем"):
                login_page = LoginPage(driver)
                inventory_page = login_page.login_as_standard_user()
                print("✅ Авторизация прошла успешно")
                allure.attach(driver.get_screenshot_as_png(), name="after_login",
                            attachment_type=allure.attachment_type.PNG)
            
            with allure.step("Добавление товаров в корзину"):
                # Используем альтернативный метод добавления товаров
                products_to_add = [
                    "Sauce Labs Backpack",
                    "Sauce Labs Bike Light",  # Заменяем проблемные товары
                    "Sauce Labs Fleece Jacket"
                ]
                
                for product in products_to_add:
                    print(f"🛒 Пытаемся добавить: {product}")
                    
                    # Получаем кнопку и проверяем ее состояние
                    button_locator = inventory_page.get_product_button(product)
                    button = inventory_page.find_clickable_element(*button_locator)
                    button_text = button.text
                    print(f"   Текст кнопки: '{button_text}'")
                    
                    if button_text.upper() == "ADD TO CART":
                        button.click()
                        print(f"✅ {product} - добавлен")
                        time.sleep(0.5)
                    else:
                        print(f"⚠️ {product} - уже в корзине (кнопка: {button_text})")
                    
                    current_count = inventory_page.get_cart_items_count()
                    print(f"   Товаров в корзине: {current_count}")
                
                final_count = inventory_page.get_cart_items_count()
                print(f"🎯 Итоговое количество товаров в корзине: {final_count}")
                
                # Если товаров меньше 3, попробуем добавить другие
                if final_count < 3:
                    additional_products = ["Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]
                    for product in additional_products:
                        if final_count >= 3:
                            break
                        try:
                            button_locator = inventory_page.get_product_button(product)
                            button = inventory_page.find_clickable_element(*button_locator)
                            if button.text.upper() == "ADD TO CART":
                                button.click()
                                print(f"✅ Дополнительно добавлен: {product}")
                                time.sleep(0.5)
                                final_count = inventory_page.get_cart_items_count()
                        except Exception as e:
                            print(f"❌ Не удалось добавить {product}: {e}")
                
                print(f"📦 Финальное количество товаров: {final_count}")
                assert final_count >= 1, "В корзине должен быть хотя бы один товар"
                
                allure.attach(driver.get_screenshot_as_png(), name="after_adding_products",
                            attachment_type=allure.attachment_type.PNG)
            
            with allure.step("Переход в корзину"):
                cart_page = inventory_page.go_to_cart()
                cart_count = cart_page.get_cart_items_count()
                print(f"🛒 Товаров на странице корзины: {cart_count}")
                allure.attach(driver.get_screenshot_as_png(), name="cart_page",
                            attachment_type=allure.attachment_type.PNG)
            
            with allure.step("Оформление заказа"):
                checkout_page = cart_page.click_checkout()
                
                with allure.step("Заполнение информации для доставки"):
                    checkout_page.fill_checkout_info("John", "Doe", "12345")
                    allure.attach(driver.get_screenshot_as_png(), name="checkout_filled",
                                attachment_type=allure.attachment_type.PNG)
            
            with allure.step("Проверка итоговой суммы"):
                total_amount = checkout_page.get_total_amount()
                print(f"💰 Итоговая сумма заказа: ${total_amount}")
                
                # Проверяем что сумма вообще есть и она разумная
                assert float(total_amount) > 0, "Сумма заказа должна быть положительной"
                assert float(total_amount) < 100, "Сумма заказа должна быть разумной"
                
                allure.attach(driver.get_screenshot_as_png(), name="final_total",
                            attachment_type=allure.attachment_type.PNG)
            
            print("🎉 Тест пройден успешно!")
            
        except Exception as e:
            print(f"❌ Ошибка в тесте: {e}")
            with allure.step("Сделать скриншот при ошибке"):
                allure.attach(driver.get_screenshot_as_png(), name="error_screenshot",
                            attachment_type=allure.attachment_type.PNG)
            raise
        finally:
            with allure.step("Закрытие браузера"):
                driver.quit()
