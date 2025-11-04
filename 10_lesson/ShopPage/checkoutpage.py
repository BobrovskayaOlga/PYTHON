from selenium.webdriver.common.by import By
from basepage import BasePage
import allure

class CheckoutPage(BasePage):
    """
    Класс для работы со страницей оформления заказа SauceDemo.
    """
    
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    TOTAL_AMOUNT = (By.CLASS_NAME, "summary_total_label")
    
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.
        
        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        super().__init__(driver)
    
    @allure.step("Ввести имя: '{first_name}'")
    def enter_first_name(self, first_name):
        """
        Ввод имени в поле ввода.
        
        Args:
            first_name: имя для ввода
            
        Returns:
            CheckoutPage: текущий экземпляр страницы для цепочки вызовов
        """
        first_name_field = self.find_element(*self.FIRST_NAME_INPUT)
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        return self
    
    @allure.step("Ввести фамилию: '{last_name}'")
    def enter_last_name(self, last_name):
        """
        Ввод фамилии в поле ввода.
        
        Args:
            last_name: фамилия для ввода
            
        Returns:
            CheckoutPage: текущий экземпляр страницы для цепочки вызовов
        """
        last_name_field = self.find_element(*self.LAST_NAME_INPUT)
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        return self
    
    @allure.step("Ввести почтовый индекс: '{postal_code}'")
    def enter_postal_code(self, postal_code):
        """
        Ввод почтового индекса в поле ввода.
        
        Args:
            postal_code: почтовый индекс для ввода
            
        Returns:
            CheckoutPage: текущий экземпляр страницы для цепочки вызовов
        """
        postal_code_field = self.find_element(*self.POSTAL_CODE_INPUT)
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)
        return self
    
    @allure.step("Нажать кнопку продолжения")
    def click_continue(self):
        """
        Нажатие кнопки продолжения оформления заказа.
        
        Returns:
            CheckoutPage: текущий экземпляр страницы для цепочки вызовов
        """
        self.find_clickable_element(*self.CONTINUE_BUTTON).click()
        return self
    
    @allure.step("Заполнить информацию для оформления заказа")
    def fill_checkout_info(self, first_name, last_name, postal_code):
        """
        Полное заполнение информации для оформления заказа.
        
        Args:
            first_name: имя покупателя
            last_name: фамилия покупателя
            postal_code: почтовый индекс
            
        Returns:
            CheckoutPage: текущий экземпляр страницы для цепочки вызовов
        """
        return (self.enter_first_name(first_name)
                   .enter_last_name(last_name)
                   .enter_postal_code(postal_code)
                   .click_continue())
    
    @allure.step("Получить итоговую сумму заказа")
    def get_total_amount(self):
        """
        Получение итоговой суммы заказа.
        
        Returns:
            str: итоговая сумма заказа
        """
        total_element = self.find_element(*self.TOTAL_AMOUNT)
        total_text = total_element.text
        return total_text.split("$")[1]
    
    @allure.step("Отменить оформление заказа")
    def click_cancel(self):
        """
        Нажатие кнопки отмены оформления заказа.
        
        Returns:
            CheckoutPage: текущий экземпляр страницы для цепочки вызовов
        """
        self.find_clickable_element(*self.CANCEL_BUTTON).click()
        return self
