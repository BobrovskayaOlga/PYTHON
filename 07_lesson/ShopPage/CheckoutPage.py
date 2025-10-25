from selenium.webdriver.common.by import By
from BasePage import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    TOTAL_AMOUNT = (By.CLASS_NAME, "summary_total_label")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def enter_first_name(self, first_name):
        first_name_field = self.find_element(*self.FIRST_NAME_INPUT)
        first_name_field.clear()
        first_name_field.send_keys(first_name)
        return self
    
    def enter_last_name(self, last_name):
        last_name_field = self.find_element(*self.LAST_NAME_INPUT)
        last_name_field.clear()
        last_name_field.send_keys(last_name)
        return self
    
    def enter_postal_code(self, postal_code):
        postal_code_field = self.find_element(*self.POSTAL_CODE_INPUT)
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)
        return self
    
    def click_continue(self):
        self.find_clickable_element(*self.CONTINUE_BUTTON).click()
        return self
    
    def fill_checkout_info(self, first_name, last_name, postal_code):
        return (self.enter_first_name(first_name)
                   .enter_last_name(last_name)
                   .enter_postal_code(postal_code)
                   .click_continue())
    
    def get_total_amount(self):
        total_element = self.find_element(*self.TOTAL_AMOUNT)
        total_text = total_element.text
        return total_text.split("$")[1]
