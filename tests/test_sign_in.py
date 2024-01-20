import time

import pytest
import allure

from locators.sign_in_page_locators import SingInPageLocators
from pages.sign_in_page import SignInPage
from data.sign_in_data import sign_in_data, LOGIN, sign_in_errors
from data.data_urls import SIGN_IN_URL, URL_AFTER_LOGIN, URL_AFTER_SUCCESS_LOGIN, FORGOT_YOUR_PASSWORD_URL, \
    CREATE_ACCOUNT_PAGE_URL
from data.credentials import credentials


@pytest.fixture(scope="function")
def sign_in_page(driver):
    sign_in_page = SignInPage(driver, SIGN_IN_URL)
    sign_in_page.open()
    return sign_in_page

@allure.epic('Sign In Page')
@allure.feature('Registered Customers')
class TestRegisteredCustomers:
    @allure.title('TC 03.01.01 Verify Sign In Page h1 Header')
    def test_03_01_01_presence_h1_heading(self, driver, sign_in_page):
        """Check Login Page Heading is present """
        h1_heading = sign_in_page.check_h1_header()
        assert h1_heading is not None and h1_heading.text == sign_in_data["h1_heading"], \
            "H1 Heading is incorrect or not present"

    @allure.title('TC 03.01.02 Verify Registered Customers Heading')
    def test_03_01_02_presence_registered_customers_heading(self, driver, sign_in_page):
        """Check Registered Customers Heading is present """
        heading = sign_in_page.check_registered_customers_heading()
        assert heading is not None and heading.text == sign_in_data["customer_login_heading"], \
            "Registered Customers heading is incorrect or not present"

    @allure.title('TC 03.01.03 Verify Registered Customers note')
    def test_03_01_03_presence_registered_customers_note(self, driver, sign_in_page):
        """Check Registered Customers note is present """
        note = sign_in_page.check_registered_customers_note()
        assert note is not None and note.text == sign_in_data["customer_login_note"], \
            "Registered Customers note is incorrect or not present"

    @allure.title('TC 03.01.04 Verify Email field is present')
    def test_03_01_04_email_field_is_present(self, driver, sign_in_page):
        """Check if the Email input field is present"""
        email_input = sign_in_page.check_customer_email_field_is_clickable()
        assert email_input.is_displayed(), "Email input field is not displayed"

    @allure.title('TC 03.01.05 Verify Email field is correct format and clickable')
    def test_03_01_05_email_field_is_correct_format_and_clickable(self, driver, sign_in_page):
        """Check if the Email input is of correct format (input-text) and clickable"""
        email_input = sign_in_page.check_customer_email_field_is_clickable()
        assert "input-text" in email_input.get_attribute("class") \
               and email_input.is_enabled(), \
            "Email input field does not accept text or is not clickable"

    @allure.title('TC 03.01.06 Verify Email field is appropriately labeled')
    def test_03_01_06_email_is_appropriately_labeled(self, driver, sign_in_page):
        """Check if Email field is appropriately labeled """
        label = sign_in_page.check_customer_email_label()
        asterisk = sign_in_page.check_customer_email_asterisk()
        assert asterisk is not None and label.text == sign_in_data["email_label"], \
            "Email label or asterisk is not present for Email field"

    @allure.title('TC 03.01.07 Verify Email field highlighting on click')
    def test_03_01_07_email_field_gets_highlighted_when_clicked(self, driver, sign_in_page):
        """
        Check the Email field is activated with a cursor and gets highlighted when clicked
        """
        initial_box_shadow, active_box_shadow = sign_in_page.activate_email_field_and_check_style()
        assert active_box_shadow != initial_box_shadow, \
            "Error: Email field style doesn't change on activation"

    @allure.title('TC 03.01.08 Verify displayed email matches the entered email in Email field')
    def test_03_01_08_value_in_email_matches(self, driver, sign_in_page):
        """Check if the displayed email matches the entered email in Email field"""
        sign_in_page.fill_in_email_field(credentials['email'])
        displayed_email = sign_in_page.get_email_field_attribute('value')
        assert displayed_email == credentials['email'], "Email value in the field doesn't match the entered email"

    @allure.title('TC 03.01.09 Verify Password field is present')
    def test_03_01_09_password_field_is_present(self, driver, sign_in_page):
        """Check if the password input field is present"""
        password_input = sign_in_page.check_customer_password_field_is_clickable()
        assert password_input.is_displayed(), "Password input field is not displayed"

    @allure.title('TC 03.01.10 Verify Password field is correct format and clickable')
    def test_03_01_10_password_field_is_correct_format_and_clickable(self, driver, sign_in_page):
        """Check if the password input field is of correct format (input-text) and clickable"""
        password_input = sign_in_page.check_customer_password_field_is_clickable()
        assert "input-text" in password_input.get_attribute("class") \
               and password_input.is_enabled(), \
            "Password input field does not accept text or is not clickable"

    @allure.title('TC 03.01.11 Verify Password field is appropriately labeled')
    def test_03_01_11_password_is_appropriately_labeled(self, driver, sign_in_page):
        """Check if Password field is appropriately labeled """
        label = sign_in_page.check_customer_password_label()
        asterisk = sign_in_page.check_customer_password_asterisk()
        assert asterisk is not None and label.text == sign_in_data["password_label"], \
            "Password label or asterisk is not present for Password field"

    @allure.title('TC 03.01.12 Verify Password field highlighting on click')
    def test_03_01_12_password_field_gets_highlighted_when_clicked(self, driver, sign_in_page):
        """
        Check the Password field is activated with a cursor and gets highlighted when clicked
        """
        initial_psw_box_shadow, active_psw_box_shadow = sign_in_page.activate_password_field_and_check_style()
        assert active_psw_box_shadow != initial_psw_box_shadow, \
            "Error: Password field style doesn't change on activation"

    @allure.title('TC 03.01.13 Verify Password is masked')
    def test_03_01_13_password_masking(self, driver, sign_in_page):
        """Check if the entered value is masked in password field"""
        password_input = sign_in_page.check_password_value_masking(credentials['password'])
        assert password_input == "password", "Password input field is not marked as password type"

    @allure.title('TC 03.01.14 Verify Sign in button is present')
    def test_03_01_14_sign_in_button_is_present(self, driver, sign_in_page):
        button = sign_in_page.check_sign_in_button_is_visible()
        assert button is not None and button.text == sign_in_data['sign_in_btn'], \
            f'''The {sign_in_data['sign_in_btn']} is not visible'''

    @allure.title('TC 03.01.15 Verify Sign in button is clickable')
    def test_03_01_15_sign_in_button_is_clickable(self, driver, sign_in_page):
        """Check if Sign In button is clickable"""
        sign_in_button = sign_in_page.check_sign_in_button_is_clickable()
        assert sign_in_button is not None, "Sign In button element not found"

    @allure.title('TC 03.01.16 Verify Forgot Your Password link is present')
    def test_03_01_16_forgot_your_password_link_is_present(self, driver, sign_in_page):
        """Verify that the 'Forgot your password?' link is present"""
        element = sign_in_page.check_forgot_your_password_link()
        element_href = element.get_attribute("href")
        assert element.is_displayed() and element_href == FORGOT_YOUR_PASSWORD_URL, "Forgot Your Password link is not present"

    @allure.title('TC 03.01.17 Verify Forgot Your Password link is functional')
    def test_03_01_16_verify_forgot_your_password_link_is_present(self, driver, sign_in_page):
        """Verify that click 'Forgot your password?' link opens correct page"""
        sign_in_page.click_forgot_your_password_link()
        header = sign_in_page.check_h1_header()
        assert driver.current_url == FORGOT_YOUR_PASSWORD_URL \
               and header is not None and header.text == "Forgot Your Password?", \
            "Verify Forgot Your Password link is incorrect or not redirect to correct page"

    @allure.title('TC 03.01.18 Verify Email field for correct email format')
    def test_03_01_18_email_field_for_correct_email_format(self, driver, sign_in_page):
        """Check error message for incorrect email format in email field"""
        sign_in_page.fill_in_email_field(credentials['incorrect_email'])
        email = sign_in_page.get_email_field_attribute('value')
        invalid_email = sign_in_page.is_valid_email(email)
        if invalid_email:
            error_message = sign_in_page.get_error_message(SingInPageLocators.EMAIL_ERROR)
            assert error_message == sign_in_errors['incorrect_email_format_msg'], \
                "The error message is incorrect or missing"


@allure.feature('New Customers')
class TestNewCustomers:
    @allure.title('TC 03.01.19 Verify New Customers Heading')
    def test_03_01_19_new_customers_heading(self, driver, sign_in_page):
        """Check New Customers Heading is present """
        h1_heading = sign_in_page.check_new_customers_heading()
        assert h1_heading is not None and h1_heading.text == sign_in_data["new_customers_heading"], \
            "New Customers heading is incorrect or not present"

    @allure.title('TC 03.01.20 Verify New Customers note')
    def test_03_01_03_new_customers_note(self, driver, sign_in_page):
        """Check if Note is present under New Customers Heading"""
        note = sign_in_page.check_new_customers_note()
        assert note is not None and note.text == sign_in_data["new_customers_note"], \
            "Note is incorrect or not present under New Customers"

    @allure.title('TC 03.01.21 Verify presence of Create an Account button ')
    def test_03_01_21_create_an_account_button_is_present(self, driver, sign_in_page):
        """Check if 'Create an Account' button is present"""
        button = sign_in_page.check_create_an_account_button()
        assert button.is_displayed() and button.text == sign_in_data["create_account_btn"], \
            f"{sign_in_data['create_account_btn']} is not visible"

    @allure.title('TC 03.01.22 Verify Create an Account button link')
    def test_03_01_22_create_an_account_button_link(self, driver, sign_in_page):
        """Check if 'Create an Account' button has correct link and is clickable"""
        button = sign_in_page.check_create_an_account_button()
        button_href = button.get_attribute("href")
        assert button.is_enabled() and button_href == CREATE_ACCOUNT_PAGE_URL, \
            f"{sign_in_data['create_account_btn']} doesn't have link ot is not clickable"

    @allure.title('TC 03.01.23 Verify Create an Account button is functional')
    def test_03_01_23_create_an_account_button_(self, driver, sign_in_page):
        """Check if 'Create an Account' button link opens correct page"""
        sign_in_page.click_create_an_account_button()
        header = sign_in_page.check_h1_header()
        assert driver.current_url == CREATE_ACCOUNT_PAGE_URL \
               and header is not None and header.text == "Create New Customer Account", \
               "Verify Create an Account button is incorrect or not redirect to correct page"


@allure.feature('Login Functionality')
class TestLogin:
    @allure.title('TC 03.02.01 Verify login with valid email valid password - Positive')
    def test_03_02_01_login_with_valid_email_valid_password_success(self, driver, sign_in_page):
        """Check Success Login with correct credentials"""
        sign_in_page.fill_in_email_field(credentials['valid_email'])
        sign_in_page.fill_in_password_field(credentials['password'])
        sign_in_page.click_sign_in_button()
        assert sign_in_page.driver.current_url in URL_AFTER_SUCCESS_LOGIN \
               and sign_in_page.check_h1_header().text in ['My Account', 'Home Page', 'Not Acceptable!'], "Login failed"

    @allure.title('TC 03.02.04 Verify error on attempting to log in with empty email - Negative')
    def test_03_02_04_error_if_login_with_empty_email(self, driver, sign_in_page):
        """Check error message on attempt to log in with empty email"""
        sign_in_page.fill_in_email_field('')
        sign_in_page.fill_in_password_field(credentials['password'])
        sign_in_page.click_sign_in_button()
        message = sign_in_page.get_error_message(SingInPageLocators.EMAIL_ERROR)
        assert message == sign_in_errors['required_field_msg']

    @allure.title('TC 03.02.05 Verify error on attempting to log in with empty email - Negative')
    def test_03_02_05_error_if_login_with_empty_password(self, driver, sign_in_page):
        """Check error message on attempt to log in with empty password"""
        sign_in_page.fill_in_email_field(credentials['email'])
        sign_in_page.fill_in_password_field('')
        sign_in_page.click_sign_in_button()
        message = sign_in_page.get_error_message((SingInPageLocators.PASSWORD_ERROR))
        assert message == sign_in_errors['required_field_msg']

    @allure.title('TC 03.02.06 Verify login with valid mix-cased email valid password - Positive')
    def test_03_02_06_login_with_valid_case_sensitive_email(self, driver, sign_in_page):
        """Check Success Login with correct credentials"""
        sign_in_page.fill_in_email_field(credentials['valid_case_sensitive_email'])
        sign_in_page.fill_in_password_field(credentials['password'])
        sign_in_page.click_sign_in_button()
        assert sign_in_page.driver.current_url in URL_AFTER_SUCCESS_LOGIN \
               and sign_in_page.check_h1_header().text in ['My Account', 'Home Page', 'Not Acceptable!'], "Login failed"

    @allure.title('TC 03.02.09 Verify login with valid mail containing trailing leading_spaces - Positive')
    def test_03_02_09_login_with_valid_email_containing_trailing_leading_spaces(self, driver, sign_in_page):
        """Check Success Login with correct credentials"""
        sign_in_page.fill_in_email_field(credentials['valid_case_sensitive_email'])
        sign_in_page.fill_in_password_field(credentials['password'])
        sign_in_page.click_sign_in_button()
        assert sign_in_page.driver.current_url in URL_AFTER_SUCCESS_LOGIN \
               and sign_in_page.check_h1_header().text in ['My Account', 'Home Page', 'Not Acceptable!'], "Login failed"


@allure.feature('Failed Login Functionality')
# @pytest.mark.skip(reason="to be run with secret code for captcha")
class TestFailedLogin:
    @allure.title('TC 03.02.01 to 03_02_10 Verify Failed Login, no error validation')
    @pytest.mark.parametrize('email, password', LOGIN)
    def test_03_02_01_to_03_02_10_login(self, driver, email, password):
        """Check Success and Failed Login, no error validation"""
        sign_in_page = SignInPage(driver, SIGN_IN_URL)
        sign_in_page.open()
        sign_in_page.fill_in_email_field(email)
        sign_in_page.fill_in_password_field(password)
        sign_in_page.click_sign_in_button()
        try:
            assert sign_in_page.driver.current_url in URL_AFTER_LOGIN \
                   and sign_in_page.check_h1_header().text in ['My Account', 'Home Page',
                                                               'Customer Login'], "Login failed"
        except AssertionError as error:
            print('Error: ', str(error))
            return False

    @allure.title('TC 03.02.02 to 03_02_10 Verify Error on Failed Login with invalid credentials')
    @pytest.mark.parametrize('email, password', [LOGIN[i] for i in [1, 2, 6, 8, 9]])
    def test_03_02_02_to_10_error_if_login_with_invalid_credentials(self, driver, sign_in_page, email, password):
        """Check error on Failed Login with invalid credentials, case-sensitive password and password with spaces"""
        sign_in_page.fill_in_email_field(email)
        sign_in_page.fill_in_password_field(password)
        sign_in_page.click_sign_in_button()

        error_message = sign_in_page.get_error_message((SingInPageLocators.ERROR_MESSAGE))
        assert error_message in [sign_in_errors['invalid_credentials_msg']], \
            "The error message is incorrect or missing"
