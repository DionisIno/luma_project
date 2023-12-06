import pytest
import allure


from pages.forgot_your_password_page import ForgotYourPasswordPage
from locators.forgot_your_password_locators import ForgotYourPasswordPageLocators
from data.forgot_your_password_data import forgot_your_password_data, forgot_your_password_errors, \
    captcha, captcha_img_link
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
    def test_17_01_06_email_field_gets_highlighted_when_clicked(self, driver, forgot_psw_page):
        """
        Check the Email field is activated with a cursor and gets highlighted when clicked
        """
        initial_box_shadow, active_box_shadow = forgot_psw_page.activate_forgot_psw_email_field_and_check_style()
        assert active_box_shadow != initial_box_shadow, \
            "Error: Email field style doesn't change on activation"

    @allure.title('TC 17.01.07 Verify displayed email matches the entered email in FYP Email field')
    def test_17_01_07_displayed_value_in_email_field_matches_entered(self, driver, forgot_psw_page):
        """Check if the displayed email matches the entered email in Email field"""
        forgot_psw_page.fill_in_forgot_psw_email_field(credentials['email'])
        displayed_email = forgot_psw_page.get_forgot_psw_email_field_attribute('value')
        assert displayed_email == credentials['email'], "Email value in the field doesn't match the entered email"

    @allure.title('TC 17.01.08 Verify Email field for correct email format')
    def test_17_01_08_email_field_for_correct_email_format(self, driver, forgot_psw_page):
        """Check error message for incorrect email format in email field"""
        forgot_psw_page.fill_in_forgot_psw_email_field(credentials['incorrect_email'])
        email = forgot_psw_page.get_forgot_psw_email_field_attribute('value')
        invalid_email = forgot_psw_page.is_valid_email(email)
        if invalid_email:
            error_message = forgot_psw_page.get_error_message()
            assert error_message == forgot_your_password_errors['incorrect_email_format_msg'], \
                "The error message is incorrect or missing"

    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.09 Verify FYP captcha input field is present')
    def test_17_01_09_email_field_is_present(self, driver, forgot_psw_page):
        """Check if the captcha input field is present"""
        captcha_input = forgot_psw_page.check_forgot_psw_captcha_field_is_clickable()
        assert captcha_input.is_displayed(), "The captcha input field is not displayed"

    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.10 Verify FYP captcha input field is correct format and clickable')
    def test_17_01_10_captcha_field_is_correct_format_and_clickable(self, driver, forgot_psw_page):
        """Check if the captcha input is of correct format (input-text) and clickable"""
        captcha_input = forgot_psw_page.check_forgot_psw_captcha_field_is_clickable()
        assert "text" in captcha_input.get_attribute("type") \
               and captcha_input.is_enabled(), \
            "The captcha input field does not accept text or is not clickable"

    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.11 Verify FYP captcha input field is appropriately labeled')
    def test_17_01_11_captcha_field_is_appropriately_labeled(self, driver, forgot_psw_page):
        """Check if Email field is appropriately labeled """
        captcha_label = forgot_psw_page.check_forgot_psw_captcha_label()
        captcha_asterisk = forgot_psw_page.check_forgot_psw_captcha_asterisk()
        assert captcha_asterisk is not None \
               and captcha_label.text == forgot_your_password_data["captcha_field_label"], \
            "The captcha label or asterisk is not present for captcha field"

    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.12 Verify FYP captcha field highlighting on click')
    def test_17_01_12_captcha_field_gets_highlighted_when_clicked(self, driver, forgot_psw_page):
        """
        Check the captcha field is activated with a cursor and gets highlighted when clicked
        """
        initial_box_shadow, active_box_shadow = forgot_psw_page.activate_forgot_psw_captcha_field_and_check_style()
        assert active_box_shadow != initial_box_shadow, \
            "Error: captcha input field style doesn't change on activation"

    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.13 Verify displayed captcha matches the entered value in FYP captcha field')
    def test_17_01_13_displayed_value_in_captcha_field_matches_entered(self, driver, forgot_psw_page):
        """The test checks if the displayed captcha matches the entered value in the captcha field"""
        forgot_psw_page.fill_in_forgot_psw_captcha_field(captcha)
        displayed_captcha = forgot_psw_page.get_forgot_psw_captcha_field_attribute('value')
        assert displayed_captcha == captcha, "Captcha value in the field doesn't match the entered captcha"

    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.14 Verify Reload captcha button is present')
    def test_17_01_14_reload_captcha_id_displayed(self, driver, forgot_psw_page):
        """Check if the 'Reload captcha' button is present"""
        reload_captcha_button = forgot_psw_page.check_reload_captcha_button_is_visible()
        assert reload_captcha_button is not None \
               and reload_captcha_button.text == forgot_your_password_data['reload_captcha_btn'], \
               f'''The {forgot_your_password_data['reload_captcha_btn']} button is not visible'''

    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.15 Verify Reload captcha button is clickable')
    def test_17_01_15_reload_captcha_is_clickable(self, driver, forgot_psw_page):
        """Check that the 'Reload captcha' button is clickable"""
        reload_captcha_button = forgot_psw_page.check_reload_captcha_button_is_clickable()
        assert reload_captcha_button is not None, "Reload captcha button element not found"

    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.16 Verify click Reload captcha button generates a new captcha image')
    def test_17_01_16_click_reload_captcha_generates_captcha_image(self, driver, forgot_psw_page):
        """
        Check that the 'Reload captcha' button generates a new captcha image
        and ensure the new image source is different from the original image source
        """
        captcha_image = forgot_psw_page.check_captcha_image_is_visible()
        image_src = captcha_image.get_attribute("src")
        forgot_psw_page.click_reload_captcha_button()
        new_image_src = captcha_image.get_attribute("src")
        assert new_image_src.endswith("png") and new_image_src != image_src, \
            "The new captcha image source is empty or incorrect or did not reload"

    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.17 Verify captcha image is present by default')
    def test_17_01_17_captcha_image_is_displayed(self, driver, forgot_psw_page):
        """Check that the captcha image is present by default"""
        captcha_image = forgot_psw_page.check_captcha_image_is_visible()
        image_src = captcha_image.get_attribute("src")
        assert captcha_image.is_displayed(), "The captcha image is not visible"
        assert image_src and image_src.endswith("png"), "The new captcha image source is empty or incorrect"

    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.18 Verify captcha image has alternative text')
    def test_17_01_18_captcha_image_is_displayed(self, driver, forgot_psw_page):
        """Check that the captcha image is present by default"""
        captcha_image = forgot_psw_page.check_captcha_image_is_visible()
        image_alt_text = captcha_image.get_attribute("alt")
        assert image_alt_text == forgot_your_password_data['captcha_image_alt_text'], \
            "The captcha image is incorrect or missing"

    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.19 Verify Reset My Password button is present')
    def test_17_01_19_reload_captcha_id_displayed(self, driver, forgot_psw_page):
        """Check if the 'Reload captcha' button is present"""
        reload_captcha_button = forgot_psw_page.check_reset_my_password_button_is_visible()
        assert reload_captcha_button is not None \
               and reload_captcha_button.text == forgot_your_password_data['reset_my_password_btn'], \
            f'''The {forgot_your_password_data['reset_my_password_btn']} button is not visible'''

    @allure.title('TC 17.01.20 Verify Reset My Password button is clickable')
    def test_17_01_20_reset_my_password_button_is_clickable(self, driver, forgot_psw_page):
        """Check that the 'Reset My Password' button is clickable"""
        reset_my_psw_button = forgot_psw_page.check_reset_my_password_button_is_clickable()
        assert reset_my_psw_button is not None, "Reload captcha button element not found"


@allure.epic('Forgot Your Password Functionality')
class TestForgotYourPasswordFunctionality:
    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.24 Verify Error on resetting My Password with invalid captcha')
    def test_17_01_24_error_if_reset_my_password_with_invalid_captcha(self, driver, forgot_psw_page):
        """Check error message on attempt to reset password with invalid captcha"""
        forgot_psw_page.fill_in_email_field(credentials['valid_email'])
        forgot_psw_page.fill_in_forgot_psw_captcha_field(captcha)
        forgot_psw_page.click_reset_my_password_button()
        error_message = forgot_psw_page.get_error_incorrect_captcha_message_()
        assert error_message == forgot_your_password_errors['incorrect_captcha_msg'], \
            "The error message is incorrect or missing"

    @allure.title('TC 17.01.25 Verify error on resetting My Password with empty email')
    def test_17_01_25_error_if_reset_my_password_with_empty_email(self, driver, forgot_psw_page):
        """Check error message on attempt to reset password with empty email field"""
        # forgot_psw_page.fill_in_forgot_psw_captcha_field(captcha)
        forgot_psw_page.click_reset_my_password_button()
        error_message = forgot_psw_page.get_error_email_input_is_required()
        assert error_message == forgot_your_password_errors['required_field_msg'], \
            "The error message is incorrect or missing"

    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.26 Verify error on resetting My Password with empty captcha')
    def test_17_01_26_error_if_reset_my_password_with_empty_captcha(self, driver, forgot_psw_page):
        """Check error message on attempt to reset password with empty captcha input field"""
        forgot_psw_page.fill_in_email_field(credentials['valid_email'])
        forgot_psw_page.click_reset_my_password_button()
        error_message = forgot_psw_page.get_error_captcha_input_is_required()
        assert error_message == forgot_your_password_errors['required_field_msg'], \
            "The error message is incorrect or missing"

    @pytest.mark.skip(reason="Skipped because the Captcha removed from the UI and the test is not working")
    @allure.title('TC 17.01.27 Verify all fields got cleared after the failed attempt to reset password')
    def test_17_01_27_fields_are_cleared_after_failed_attempt_to_reset_password(self, driver, forgot_psw_page):
        """Check if all the fields are getting cleared after failed attempt to reset password with invalid captcha"""
        forgot_psw_page.fill_in_email_field(credentials['valid_email'])
        forgot_psw_page.fill_in_forgot_psw_captcha_field(captcha)
        forgot_psw_page.click_reset_my_password_button()
        displayed_email = forgot_psw_page.get_forgot_psw_email_field_attribute('value')
        displayed_captcha = forgot_psw_page.get_forgot_psw_captcha_field_attribute('value')
        assert displayed_email == "" and displayed_captcha == "", \
            "Inputs fields weren't cleared after failed attempt to reset password"
