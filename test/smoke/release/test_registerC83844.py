from selenium.webdriver import Firefox, Chrome, Ie
from lib.ui.login.login_page import LoginPage
from lib.ui.login.registration_page import RegistrationPage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from lib.util.common import create_driver
import unittest
import csv
from lib.util.common.csvcompiler import castrange

# Create python Test class and inherit unittest module#


class TestRegisterC83844(unittest.TestCase):
    # Preparing for test execution#
    def setUp(self):
        # initialize the browser instance#
        self.browser = create_driver.get_browser_instance()
        # initialize page object class#
        self.login_page = LoginPage(self.browser)
        self.registration_page = RegistrationPage(self.browser)
        self.a = castrange()

    def test_case001(self):
        # wait for page load#
        self.login_page.wait_for_page_load()
        # click on register button on the top right hand corner of page#
        self.login_page.get_register_button().click()
        # wait for registration page load#
        self.registration_page.wait_for_registration_page_to_load()
        # enter valid email address#
        self.registration_page.get_email_textbox().send_keys(self.a[0][0])
        # enter mobile phone number#
        self.registration_page.get_phone_textbox().send_keys(self.a[1][0])
        # enter valid credentials#
        self.registration_page.get_password_textbox().send_keys(self.a[2][0])
        self.registration_page.get_firstname_textbox().send_keys(self.a[3][0])
        self.registration_page.get_last_name_textbox().send_keys(self.a[4][0])
        ddl_day = self.registration_page.get_day_ddl()
        # Creating an object for Select class functionality and passing identified element for date#
        sct_day = Select(ddl_day)
        # Selecting the date using index#
        sct_day.select_by_index(8)
        ddl_month = self.registration_page.get_month_ddl()
        # Creating an object for Select class functionality and passing identified element for month#
        sct_month = Select(ddl_month)
        # Selecting the month using value#
        sct_month.select_by_value('9')
        ddl_year = self.registration_page.get_year_ddl()
        # Creating an object for Select class functionality and passing identified element for year#
        sct_year = Select(ddl_year)
        # Selecting year by visible text#
        sct_year.select_by_visible_text('1985')
        # Enter zip code#
        self.registration_page.get_zip_textbox().send_keys(self.a[5][0])
        # Enter 6 digit SSN #
        self.registration_page.get_ssn_textbox().send_keys(self.a[6][0])
        # Check the checkbox#
        self.registration_page.get_checkbox_button().click()
        # Click/Push register button #
        self.registration_page.get_register_button().click()

    def test_case002(self):
        # wait for page load#
        self.login_page.wait_for_page_load()
        # click on register link on bottom right hand corner of page#
        self.login_page.get_register_link().click()
        # wait for registration page load#
        self.registration_page.wait_for_registration_page_to_load()
        # enter valid email address#
        self.registration_page.get_email_textbox().send_keys(self.a[0][1])
        # enter mobile phone number#
        self.registration_page.get_phone_textbox().send_keys(self.a[1][1])
        # enter valid credentials#
        self.registration_page.get_password_textbox().send_keys(self.a[2][0])
        self.registration_page.get_firstname_textbox().send_keys(self.a[3][0])
        self.registration_page.get_last_name_textbox().send_keys(self.a[4][0])
        ddl_day = self.registration_page.get_day_ddl()
        # Creating an object for Select class functionality and passing identified element for date#
        sct_day = Select(ddl_day)
        # Selecting the date using index#
        sct_day.select_by_index(8)
        ddl_month = self.registration_page.get_month_ddl()
        # Creating an object for Select class functionality and passing identified element for month#
        sct_month = Select(ddl_month)
        # Selecting the month using value#
        sct_month.select_by_value('9')
        ddl_year = self.registration_page.get_year_ddl()
        # Creating an object for Select class functionality and passing identified element for year#
        sct_year = Select(ddl_year)
        # Selecting year by visible text#
        sct_year.select_by_visible_text('1985')
        # Enter zip code#
        self.registration_page.get_zip_textbox().send_keys(self.a[5][1])
        # Enter 6 digit SSN #
        self.registration_page.get_ssn_textbox().send_keys(self.a[6][1])
        # Check the checkbox#
        self.registration_page.get_checkbox_button().click()
        # Click/Push register button #
        self.registration_page.get_register_button().click()

    def tearDown(self):
        print('Successful Test Execution')
        print('Site functions as expected')
        self.browser.close()

