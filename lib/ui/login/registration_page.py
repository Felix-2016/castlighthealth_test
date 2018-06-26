from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class RegistrationPage():
    def __init__(self, browser):
        self.browser = browser

    def wait_for_registration_page_to_load(self):
        wait = WebDriverWait(self.browser, 30)
        wait.until(expected_conditions.title_contains('Castlight - Registration'))

    def get_email_textbox(self):
        try:
            return self.browser.find_element_by_id("email")
        except:
            return None

    def get_phone_textbox(self):
        try:
            return self.browser.find_element_by_id("mobilePhoneNumber")
        except:
            return None

    def get_password_textbox(self):
        try:
            return self.browser.find_element_by_id("password")
        except:
            return None

    def get_firstname_textbox(self):
        try:
            return self.browser.find_element_by_id("firstName")
        except:
            return None

    def get_last_name_textbox(self):
        try:
            return self.browser.find_element_by_id("lastName")
        except:
            return None

    def get_day_ddl(self):
        try:
            return self.browser.find_element_by_id('day')
        except:
            return None

    def get_month_ddl(self):
        try:
            return self.browser.find_element_by_id('month')
        except:
            return None

    def get_year_ddl(self):
        try:
            return self.browser.find_element_by_id('year')
        except:
            return None

    def get_zip_textbox(self):
        try:
            return self.browser.find_element_by_id("zipCode")
        except:
            return None

    def get_ssn_textbox(self):
        try:
            return self.browser.find_element_by_id("uid-sixDigitSsn")
        except:
            return None

    def get_checkbox_button(self):
        try:
            return self.browser.find_element_by_id("policies")
        except:
            return None

    def get_register_button(self):
        try:
            return self.browser.find_element_by_xpath("//button[@type='submit']")
        except:
            return None
