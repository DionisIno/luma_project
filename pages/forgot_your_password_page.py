import allure

from locators.forgot_your_password_locators import ForgotYourPasswordPageLocators
from pages.base_page import BasePage


@allure.epic('Forgot Your Password Page')
class ForgotYourPasswordPage(BasePage):
    locators = ForgotYourPasswordPageLocators

    @allure.step('Check Forgot Your Password h1 header is visible')
    def check_forgot_psw_h1_header(self):
        '''This method verifies if h1 header is visible on the page'''
        return self.element_is_visible(self.locators.PAGE_HEADER)

    @allure.step('Check Forgot Your Password note is visible')
    def check_forgot_your_psw_note(self):
        """This method verifies if note is visible under heading"""
        return self.element_is_visible(self.locators.FORGOT_YOUR_PASSWORD_NOTE)

    @allure.step('Check FYP Email label is visible')
    def check_forgot_psw_email_label(self):
        """This method verifies if Email label is visible"""
        return self.element_is_visible(self.locators.EMAIL_LABEL)

    @allure.step('Check FYP Email asterisk is displayed')
    def check_forgot_psw_email_asterisk(self):
        """This method verifies if asterisk is displayed next to Email label"""
        email_label = self.check_forgot_psw_email_label()
        asterisk_script = self.find_required_element()
        return self.driver.execute_script(asterisk_script, email_label)

    @allure.step('Check FYP Email field is clickable')
    def check_forgot_psw_email_field_is_clickable(self):
        """This method verifies if Email field is clickable"""
        return self.element_is_clickable(self.locators.EMAIL)

    @allure.step('Activate FYP Email field and check style')
    def activate_forgot_psw_email_field_and_check_style(self):
        """
        This method activates the Email field
        and checks if the style of the field changes upon activation.
        """
        return self.activate_field_and_check_style(self.locators.EMAIL)

    @allure.step('Fill in FYP Email field')
    def fill_in_forgot_psw_email_field(self, email):
        """This method fills in the Email field with the provided email"""
        return self.fill_in_field(self.check_forgot_psw_email_field_is_clickable(), email)

    @allure.step('Get FYP Email field attribute')
    def get_forgot_psw_email_field_attribute(self, attribute):
        """This method gets the entered value from Email field"""
        return self.check_forgot_psw_email_field_is_clickable().get_attribute(attribute)

    @allure.step('Check FYP captcha input field is clickable')
    def check_forgot_psw_captcha_field_is_clickable(self):
        """This method verifies if captcha field is clickable"""
        return self.element_is_clickable(self.locators.FORGOT_YOUR_PASSWORD_CAPTCHA)

    @allure.step('Check the label for FYP captcha input field is visible')
    def check_forgot_psw_captcha_label(self):
        """This method verifies if captcha label is visible"""
        return self.element_is_visible(self.locators.FORGOT_YOUR_PASSWORD_CAPTCHA_LABEL)

    @allure.step('Check asterisk for FYP Captcha input field label is displayed')
    def check_forgot_psw_captcha_asterisk(self):
        """This method verifies if asterisk is displayed next to captcha label"""
        captcha_label = self.check_forgot_psw_captcha_label()
        asterisk_script = self.find_required_element()
        return self.driver.execute_script(asterisk_script, captcha_label)

    @allure.step('Activate FYP Captcha input field and check style')
    def activate_forgot_psw_captcha_field_and_check_style(self):
        """
        This method activates the captcha field
        and checks if the style of the field changes upon activation.
        """
        return self.activate_field_and_check_style(self.locators.FORGOT_YOUR_PASSWORD_CAPTCHA)
        
    @allure.step('Fill in FYP Email field')
    def fill_in_forgot_psw_captcha_field(self, text):
        """This method fills in the captcha field with the provided email"""
        return self.fill_in_field(self.check_forgot_psw_captcha_field_is_clickable(), text)

    @allure.step('Get FYP Captcha input field attribute')
    def get_forgot_psw_captcha_field_attribute(self, attribute):
        """This method gets the entered value from captcha field"""
        return self.check_forgot_psw_captcha_field_is_clickable().get_attribute(attribute)

    @allure.step('Check Reload captcha button is visible')
    def check_reload_captcha_button_is_visible(self):
        """This method verifies if reload_captcha button field is visible"""
        return self.element_is_visible(self.locators.RELOAD_CAPTCHA_BUTTON)

    @allure.step('Check Reload captcha button is clickable')
    def check_reload_captcha_button_is_clickable(self):
        """This method verifies if reload_captcha button field is clickable"""
        return self.element_is_clickable(self.locators.RELOAD_CAPTCHA_BUTTON)

    @allure.step('Click on Reload captcha button')
    def click_reload_captcha_button(self):
        """This method clicks on reload captcha button"""
        self.check_reload_captcha_button_is_clickable().click()

    @allure.step('Check Captcha image is visible')
    def check_captcha_image_is_visible(self):
        """This method verifies if captcha image is visible"""
        return self.element_is_visible(self.locators.RELOAD_CAPTCHA_IMAGE)

    @allure.step('Check Reset My Password button is visible')
    def check_reset_my_password_button_is_visible(self):
        """This method verifies if reset my password button field is visible"""
        return self.element_is_visible(self.locators.RESET_MY_PASSWORD_BUTTON)

    @allure.step('Check Reset My Password button is clickable')
    def check_reset_my_password_button_is_clickable(self):
        """This method verifies if reset my password button field is clickable"""
        return self.element_is_clickable(self.locators.RESET_MY_PASSWORD_BUTTON)

    @allure.step('Click on Reset My Password button button')
    def click_reset_my_password_button(self):
        """This method clicks on reset my password button"""
        self.check_reset_my_password_button_is_clickable().click()

    @allure.step('Get FYP Email input field error')
    def get_error_field_is_required(self):
        """This method clicks on reset my password button"""
        return self.get_error_message(self.locators.RESET_MY_PASSWORD_CAPTCHA_ERROR)

    @allure.step('Fill in Email field')
    def fill_in_email_field(self, email):
        """This method fills in Email field with provided email"""
        self.fill_in_field(self.check_forgot_psw_email_field_is_clickable(), email)

    @allure.step('Get error for email input is required ')
    def get_error_email_input_is_required(self):
        """This method to get the error indicating the captcha input was invalid"""
        return self.get_error_message(self.locators.RESET_MY_PASSWORD_EMAIL_ERROR)

    @allure.step('Get error for incorrect captcha input')
    def get_error_incorrect_captcha_message_(self):
        """This method to get the error indicating the email input is required"""
        return self.get_error_message(self.locators.ERROR_MESSAGE)

    @allure.step('Get error captcha input field required ')
    def get_error_captcha_input_is_required(self):
        """This method to get the error indicating the captcha input is required"""
        return self.get_error_message(self.locators.RESET_MY_PASSWORD_CAPTCHA_ERROR)

