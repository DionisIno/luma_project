import pytest

from pages.sign_in_page import SignInPage
from data.sign_in_data import sign_in_data
from data.data_urls import SIGN_IN_URL
from data.credentials import credentials

@pytest.fixture(scope="function")
def sign_in_page(driver):
    sign_in_page = SignInPage(driver, SIGN_IN_URL)
    sign_in_page.open()
    return sign_in_page


class TestRegisteredCustomers:
    def test_03_01_01_h1_heading(self, driver, sign_in_page):
        """Check Login Page Heading is present """
        h1_heading = sign_in_page.check_h1_header()
        assert h1_heading is not None and h1_heading.text == sign_in_data["h1_heading"], "H1 Heading is not present"

    def test_03_01_02_registered_customers_heading(self, driver, sign_in_page):
        """Check Registered Customers Heading is present """
        h1_heading = sign_in_page.check_registered_customers_heading()
        assert h1_heading is not None and h1_heading.text == sign_in_data["customer_login_heading"], \
            "Registered Customers heading is not present"

    def test_03_01_06_email_is_appropriately_labeled(self, driver, sign_in_page):
        """Check if Email field is appropriately labeled """
        label = sign_in_page.check_customer_email_label()
        asterisk = sign_in_page.check_customer_email_asterisk()
        assert asterisk is not None and label.text == sign_in_data["email_label"], \
            "Email label or asterisk is not present for Email field"

    def test_03_01_08_value_in_email_matches(self, driver, sign_in_page):
        """Check if the displayed email matches the entered email in Email field"""
        sign_in_page.fill_in_email_field(credentials['email'])
        displayed_email = sign_in_page.get_email_field_attribute('value')
        assert displayed_email == credentials['email'], "Email value in the field doesn't match the entered email"

    def test_03_01_13_password_masking(self, driver, sign_in_page):
        """Check if the entered value is masked in password field"""
        password_input = sign_in_page.check_password_value_masking(credentials['password'])
        assert password_input == "password", "Password input field is not marked as password type"

    def test_03_01_09_password_is_present(self, driver, sign_in_page):
        """Check if the password input field is present"""
        password_input = sign_in_page.check_customer_password_field_is_clickable()
        assert password_input.is_displayed(), "Password input field is not displayed"

    def test_03_01_18_email_field_for_correct_email_format(self, driver, sign_in_page):
        """Check if the entered value is masked in password field"""
        sign_in_page.fill_in_email_field("testmail.mailinator.com")
        email = sign_in_page.get_email_field_attribute('value')
        invalid_email = sign_in_page.is_valid_email(email)
        if invalid_email:
            error_message = sign_in_page.get_error_message()
            expected_error_message = "Please enter a valid email address (Ex: johndoe@domain.com)."
            assert error_message == expected_error_message, "Incorrect error message displayed"
