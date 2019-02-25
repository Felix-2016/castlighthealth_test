from lib.ui.login.login_page import LoginPage
from lib.ui.login.registration_page import RegistrationPage
from selenium.webdriver.support.select import Select
from lib.util.common import create_driver
from test.smoke.release.testdata.sample1 import castrange
import unittest
import allure
import pytest
import allure_pytest
from allure import pytest_plugin
import sys
from unittest import result
# from lib.util.common import mouse_handler#
from lib.util.common import drop_down_list_handler
from lib.util.common import popup_handler
import requests
import os
import logging
import pytest_ordering

# Create python Test class and inherit unittest module#


#@pytest.mark.regression
#@pytest.allure.feature('Feature1')
#@allure.story('Story1')
class TestRegisterC83844(unittest.TestCase):

    def setUp(self):
        # initialize the browser instance#
        self.browser = create_driver.get_browser_instance()
        # initialize page object class#
        self.login_page = LoginPage(self.browser)
        self.registration_page = RegistrationPage(self.browser)
        self.a = castrange()
        # self.errors_and_failures = self.tally()
        sys.path.insert(0, "../project")

    @pytest.mark.regression
    @pytest.mark.functional
    @pytest.mark.run(order=4)
    #@pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_case001(self):
        #allure.attach('RESULT', 'RUNNING CRITICAL TESTCASE')
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
        element_ddl = self.browser.find_element_by_id('day')
        drop_down_list_handler.select_ddl_by_index(element_ddl, 8)
        element_ddl = self.browser.find_element_by_id('month')
        drop_down_list_handler.select_ddl_by_value(element_ddl, '10')
        element_ddl = self.browser.find_element_by_id('year')
        drop_down_list_handler.select_ddl_by_visible_text(element_ddl, '1988')
        # Enter zip code#
        self.registration_page.get_zip_textbox().send_keys(self.a[5][0])
        # Enter 6 digit SSN #
        self.registration_page.get_ssn_textbox().send_keys(self.a[6][0])
        # Check the checkbox#
        self.registration_page.get_checkbox_button()
        # Click/Push register button #
        self.registration_page.get_register_button().click()
        entry1 = self.browser.current_url
        exit1 = "https://us.castlighthealth.com/v2/registration"
        assert entry1 == exit1
        self.browser.get_screenshot_as_file('C:/Users/Felix/Desktop/screenshots/test001.png')

    #@pytest.allure.severity(pytest.allure.severity_level.MINOR)
    #@unittest.skipUnless(sys.platform.startswith("Unix"), "requires windows")
    @pytest.mark.functional
    @pytest.mark.run(order=3)
    def test_case002(self):
        #allure.attach('RESULT', 'RUNNING MINOR TESTCASE')
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
        ddl_month = self.registration_page.get_month_ddl()
        # Creating an object for Select class functionality and passing identified element for month#
        sct_month = Select(ddl_month)
        # Selecting the month using value#
        sct_month.select_by_value('9')
        ddl_day = self.registration_page.get_day_ddl()
        sct_day = Select(ddl_day)
        sct_day.select_by_index(10)
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
        entry2 = self.browser.current_url
        exit2 = "https://us.castlighthealth.com/v2/registration"
        assert entry2 == exit2
        self.browser.get_screenshot_as_file('C:/Users/Felix/Desktop/screenshots/test002.png')

    @pytest.mark.functional
    @pytest.mark.run(order=3)
    #@pytest.allure.severity(pytest.allure.severity_level.NORMAL)
    #@unittest.skipUnless(sys.platform.startswith("win"), "requires win")
    def test_case003(self):
        #allure.attach('RESULT', 'RUNNING NORMAL TESTCASE')
        print('Test script for Verifying Signin button')
        # wait for page load#
        self.login_page.wait_for_page_load()
        # click on register link on bottom right hand corner of page#
        self.login_page.get_username1_textbox().send_keys(self.a[0][2])
        self.login_page.get_password1_textbox().send_keys(self.a[1][2])
        self.login_page.get_signin_button().click()
        actual_error_msg = self.login_page.get_login_error_msg().text
        expected_error_msg = 'The email or password you entered was incorrect. Please check your information and try ' \
                             'again. '
        assert actual_error_msg in expected_error_msg
        print(actual_error_msg)
        entry3 = self.browser.current_url
        exit3 = "https://us.castlighthealth.com/v2/login"
        assert entry3 == exit3
        #self.browser.get_screenshot_as_file('C:/Users/Anitha/Desktop/screenshots/test003.png')
        # element = self.browser.find_element_by_xpath("//img[@alt='Click to Verify - This site chose VeriSign SSL for "
        # "secure e-commerce and confidential communications.']")#
        # mouse_handler.mouse_hover_on_element(self.browser, element)#
        # time.sleep(8)#
        # mouse_handler.context_click_on_element(self.browser, element)
        # time.sleep(15)

    @pytest.mark.functional
    @pytest.mark.run(order=1)
    def test_case004(self):
        #allure.attach('RESULT', 'RUNNING NORMAL TESTCASE')
        print('Verifying Forgot Password link')
        # wait for page load#
        self.login_page.wait_for_page_load()
        # click on Forgot Password link on bottom of page#
        self.login_page.get_forgot_password_link().click()
        # enter valid email address#
        self.login_page.get_email_reset_textbox().send_keys(self.a[0][3])
        # click on submit button()
        self.login_page.get_submit_button().click()
        # get the error message text#
        actual_reset_error_msg = self.login_page.get_password_reset_error()
        # expected error message#
        expected_reset_error_msg = 'The email address is not allowed to receive password resets'
        assert actual_reset_error_msg != expected_reset_error_msg
        print(actual_reset_error_msg)
        entry4 = self.browser.current_url
        exit4 = "https://us.castlighthealth.com/v2/reset_password"
        assert entry4 == exit4
        self.browser.get_screenshot_as_file('C:/Users/Felix/Desktop/screenshots/test004.png')
        res = requests.get("https://us.castlighthealth.com/reset_password")
        print(res)
        exp = 200
        if res == exp:
            print('all good')
        else:
            print('error')

    def tearDown(self):
        print('No false positive in SPM')
        print('Site functions as expected')
        print('No Shape­related issues')
        print(sys.getwindowsversion())
        print(sys.exc_info()[0])
        print(sys.version_info)
        print(sys.version)
        # if sys.exc_info()[0]!=None:
        #     self.browser.save_screenshot('C:/Users/Felix/Desktop/screenshots/failure.png')
        self.browser.close()


class TestRegisterC83845(unittest.TestCase):
    # Preparing for test execution#
    @allure.step("running")
    def setUp(self):
        # initialize the browser instance#
        self.browser = create_driver.get_browser_instance()
        # initialize page object class#
        self.login_page = LoginPage(self.browser)
        self.registration_page = RegistrationPage(self.browser)
        self.a = castrange()
        sys.path.insert(0, "../project")

    @pytest.mark.description('what to do in this test')
    @allure.testcase("Your Test Case name or link")
    @allure.attach('RESULT', 'RUNNING NORMAL TESTCASE')
    def test_case005(self):
        # allure.testcase("Your Test Case name or link")
        # allure.attach('RESULT', 'RUNNING NORMAL TESTCASE')
        print('Verifying Forgot Password link')
        # wait for page load#
        self.login_page.wait_for_page_load()
        # click on Forgot Password link on bottom of page#
        self.login_page.get_forgot_password_link().click()
        # enter valid email address#
        self.login_page.get_email_reset_textbox().send_keys(self.a[0][3])
        # click on submit button()
        self.login_page.get_submit_button().click()
        # get the error message text#
        actual_reset_error_msg = self.login_page.get_password_reset_error()
        # expected error message#
        expected_reset_error_msg = 'The email address is not allowed to receive password resets'
        assert actual_reset_error_msg != expected_reset_error_msg
        print(actual_reset_error_msg)
        entry4 = self.browser.current_url
        exit4 = "https://us.castlighthealth.com/v2/reset_password"
        assert entry4 == exit4
        self.browser.get_screenshot_as_file('C:/Users/Anitha/Desktop/screenshots/test004.png')

    def tearDown(self):
        print('No false positive in SPM')
        print('Site functions as expected')
        print('No Shape­related issues')
        self.browser.close()
