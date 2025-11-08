from selenium.webdriver.common.by import By
from BasePage import BasePage
import allure

class FormPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, "input[name='first-name']")
    LAST_NAME = (By.CSS_SELECTOR, "input[name='last-name']")
    ADDRESS = (By.CSS_SELECTOR, "input[name='address']")
    EMAIL = (By.CSS_SELECTOR, "input[name='e-mail']")
    PHONE = (By.CSS_SELECTOR, "input[name='phone']")
    ZIP_CODE = (By.CSS_SELECTOR, "input[name='zip-code']")
    CITY = (By.CSS_SELECTOR, "input[name='city']")
    COUNTRY = (By.CSS_SELECTOR, "input[name='country']")
    JOB_POSITION = (By.CSS_SELECTOR, "input[name='job-position']")
    COMPANY = (By.CSS_SELECTOR, "input[name='company']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-outline-primary.mt-3")
    
    FIELD_IDS = {
        "first-name": "first-name",
        "last-name": "last-name", 
        "address": "address",
        "e-mail": "e-mail",
        "phone": "phone",
        "zip-code": "zip-code",
        "city": "city",
        "country": "country",
        "job-position": "job-position",
        "company": "company"
    }
    
    ERROR_COLOR = "rgba(248, 215, 218, 1)"
    SUCCESS_COLOR = "rgba(209, 231, 221, 1)"
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()
    
    @allure.step("Заполнить поле 'Имя' значением: '{first_name}'")
    def fill_first_name(self, first_name):
        self.find_element(*self.FIRST_NAME).send_keys(first_name)
        return self
    
    @allure.step("Заполнить поле 'Фамилия' значением: '{last_name}'")
    def fill_last_name(self, last_name):
        self.find_element(*self.LAST_NAME).send_keys(last_name)
        return self
    
    @allure.step("Заполнить поле 'Адрес' значением: '{address}'")
    def fill_address(self, address):
        self.find_element(*self.ADDRESS).send_keys(address)
        return self
    
    @allure.step("Заполнить поле 'Email' значением: '{email}'")
    def fill_email(self, email):
        self.find_element(*self.EMAIL).send_keys(email)
        return self
    
    @allure.step("Заполнить поле 'Телефон' значением: '{phone}'")
    def fill_phone(self, phone):
        self.find_element(*self.PHONE).send_keys(phone)
        return self
    
    @allure.step("Заполнить поле 'ZIP-код' значением: '{zip_code}'")
    def fill_zip_code(self, zip_code):
        self.find_element(*self.ZIP_CODE).send_keys(zip_code)
        return self
    
    @allure.step("Заполнить поле 'Город' значением: '{city}'")
    def fill_city(self, city):
        self.find_element(*self.CITY).send_keys(city)
        return self
    
    @allure.step("Заполнить поле 'Страна' значением: '{country}'")
    def fill_country(self, country):
        self.find_element(*self.COUNTRY).send_keys(country)
        return self
    
    @allure.step("Заполнить поле 'Должность' значением: '{job_position}'")
    def fill_job_position(self, job_position):
        self.find_element(*self.JOB_POSITION).send_keys(job_position)
        return self
    
    @allure.step("Заполнить поле 'Компания' значением: '{company}'")
    def fill_company(self, company):
        self.find_element(*self.COMPANY).send_keys(company)
        return self
    
    @allure.step("Заполнить все поля формы данными")
    def fill_all_fields(self, form_data):
        self.fill_first_name(form_data.get('first_name', ''))
        self.fill_last_name(form_data.get('last_name', ''))
        self.fill_address(form_data.get('address', ''))
        self.fill_email(form_data.get('email', ''))
        self.fill_phone(form_data.get('phone', ''))
        self.fill_zip_code(form_data.get('zip_code', ''))
        self.fill_city(form_data.get('city', ''))
        self.fill_country(form_data.get('country', ''))
        self.fill_job_position(form_data.get('job_position', ''))
        self.fill_company(form_data.get('company', ''))
        return self
    
    @allure.step("Отправить форму")
    def submit_form(self):
        button = self.find_clickable_element(*self.SUBMIT_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", button)
        self.driver.execute_script("arguments[0].click();", button)
        return self
    
    @allure.step("Получить цвет фона поля с ID: {field_id}")
    def get_field_background_color(self, field_id):
        field = self.driver.find_element(By.ID, field_id)
        return field.value_of_css_property("background-color")
    
    @allure.step("Проверить цвет поля {field_id}")
    def verify_field_color(self, field_id, expected_color):
        actual_color = self.get_field_background_color(field_id)
        assert actual_color == expected_color, (
            f"Поле {field_id}: ожидался цвет {expected_color}, получен {actual_color}"
        )
        return True
    
    @allure.step("Проверить, что поле ZIP-code подсвечено красным (ошибка)")
    def verify_zip_code_error(self):
        return self.verify_field_color(self.FIELD_IDS["zip-code"], self.ERROR_COLOR)
    
    @allure.step("Проверить, что все валидные поля подсвечены зеленым")
    def verify_valid_fields_success(self, exclude_fields=None):
        if exclude_fields is None:
            exclude_fields = ["zip-code"]
        
        valid_fields = [field for field in self.FIELD_IDS.keys() if field not in exclude_fields]
        
        for field_id in valid_fields:
            self.verify_field_color(self.FIELD_IDS[field_id], self.SUCCESS_COLOR)
        
        return True
