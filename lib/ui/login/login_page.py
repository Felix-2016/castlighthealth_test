from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage():
    def __init__(self,browser):
        self.browser = browser

    def wait_for_page_load(self):
        wait = WebDriverWait(self.browser,30)
        wait.until(expected_conditions.title_contains('Castlight - Sign In'))

    def get_register_button(self):
        try:
            return self.browser.find_element_by_xpath("(//a[contains(text(),'Register')])[1]")
        except:
            return None

    def get_signin_button(self):
        try:
            return self.browser.find_element_by_xpath("//button[@type='submit']")
        except:
            return None

    def get_register_link(self):
        try:
            return self.browser.find_element_by_xpath("(//a[text()='Register'])[2]")
        except:
            return None

    def get_username1_textbox(self):
        try:
            return self.browser.find_element_by_id("email")
        except:
            return None

    def get_password1_textbox(self):
        try:
            return self.browser.find_element_by_id("password")
        except:
            return None

    def get_login_error_msg(self):
        try:
            return self.browser.find_element_by_xpath("//div[contains(text(),'The email or password')]")
        except:
            return None

    def get_forgot_password_link(self):
        try:
            return self.browser.find_element_by_xpath("//a[text()='Forgot Password?']")
        except:
            return None

    def get_email_reset_textbox(self):
        try:
            return self.browser.find_element_by_id('email-address')
        except:
            return None

    def get_submit_button(self):
        try:
            return self.browser.find_element_by_xpath("//button[@type='submit']")
        except:
            return None

    def get_password_reset_error(self):
        try:
            return self.browser.find_element_by_xpath("//div[contains(text(),'The email address')]")
        except:
            return None




