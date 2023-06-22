import pytest
import allure

from locators.forgot_your_password_locators import ForgotYourPasswordPageLocators
from pages.forgot_your_password_page import ForgotYourPasswordPage
from data.forgot_your_password_data import forgot_your_password_data
from data.data_urls import FORGOT_YOUR_PASSWORD_URL
from data.credentials import credentials


@pytest.fixture(scope="function")
def forgot_psw_page(driver):
    forgot_psw_page = ForgotYourPasswordPage(driver, FORGOT_YOUR_PASSWORD_URL)
    forgot_psw_page.open()
    return forgot_psw_page

@allure.epic('Forgot Your Password Page')
class TestForgotYourPassword:
    @allure.title('TC 17.01.01 Verify Forgot Your Password Page h1 Header')
    def test_17_01_01_h1_heading(self, driver, forgot_psw_page):
        """Check Login Page Heading is present """
        h1_heading = forgot_psw_page.check_forgot_psw_h1_header()
        assert h1_heading is not None and h1_heading.text == forgot_your_password_data["h1_heading"], \
            "Forgot Your Password H1 Header is incorrect or not present"

    @allure.title('TC 17.01.02 Verify Forgot Your Password note')
    def test_17_01_02_registered_customers_note(self, driver, forgot_psw_page):
        """Check Registered Customers note is present """
        note = forgot_psw_page.check_forgot_your_psw_note()
        assert note is not None and note.text == forgot_your_password_data["forgot_your_password_note"], \
            "Forgot Your Password note is incorrect or not present"

    @allure.title('TC 17.01.03 Verify FYP Email field is present')
    def test_17_01_03_email_field_is_present(self, driver, forgot_psw_page):
        """Check if the Email input field is present"""
        email_input = forgot_psw_page.check_forgot_psw_email_field_is_clickable()
        assert email_input.is_displayed(), "Email input field is not displayed"

    @allure.title('TC 17.01.04 Verify FYP Email field is correct format and clickable')
    def test_17_01_04_email_field_is_correct_format_and_clickable(self, driver, forgot_psw_page):
        """Check if the Email input is of correct format (input-text) and clickable"""
        email_input = forgot_psw_page.check_forgot_psw_email_field_is_clickable()
        assert "input-text" in email_input.get_attribute("class") \
               and email_input.is_enabled(), \
            "Email input field does not accept text or is not clickable"

    @allure.title('TC 17.01.05 Verify FYP Email field is appropriately labeled')
    def test_17_01_05_email_is_appropriately_labeled(self, driver, forgot_psw_page):
        """Check if Email field is appropriately labeled """
        label = forgot_psw_page.check_forgot_psw_email_label()
        asterisk = forgot_psw_page.check_forgot_psw_email_asterisk()
        assert asterisk is not None and label.text == forgot_your_password_data["email_label"], \
            "Email label or asterisk is not present for Email field"

    @allure.title('TC 17.01.06 Verify FYP Email field highlighting on click')
    def test_17_01_07_email_field_gets_highlighted_when_clicked(self, driver, forgot_psw_page):
        """
        Check the Email field is activated with a cursor and gets highlighted when clicked
        """
        initial_box_shadow, active_box_shadow = forgot_psw_page.activate_forgot_psw_email_field_and_check_style()
        assert active_box_shadow != initial_box_shadow, \
            "Error: Email field style doesn't change on activation"

    @allure.title('TC 17.01.07 Verify displayed email matches the entered email in FYP Email field')
    def test_17_01_07_value_in_email_matches(self, driver, forgot_psw_page):
        """Check if the displayed email matches the entered email in Email field"""
        forgot_psw_page.fill_in_forgot_psw_email_field(credentials['email'])
        displayed_email = forgot_psw_page.get_forgot_psw_email_field_attribute('value')
        assert displayed_email == credentials['email'], "Email value in the field doesn't match the entered email"
