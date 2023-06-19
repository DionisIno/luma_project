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

    @allure.step('CheckForgot Your Password note is visible')
    def check_forgot_your_psw_note(self):
        """This method verifies if note is visible under heading"""
        return self.element_is_visible(self.locators.FORGOT_YOUR_PASSWORD_NOTE)

    @allure.step('Check Email label is visible')
    def check_forgot_psw_email_label(self):
        """This method verifies if Email label is visible"""
        return self.element_is_visible(self.locators.EMAIL_LABEL)

    @allure.step('Check Email asterisk is visible')
    def check_forgot_psw_email_asterisk(self):
        """This method verifies if asterisk is displayed next to Email label"""
        email_label = self.check_forgot_psw_email_label()
        asterisk_script = self.find_required_element()
        return self.driver.execute_script(asterisk_script, email_label)

    @allure.step('Check Email field is clickable')
    def check_forgot_psw_email_field_is_clickable(self):
        """This method verifies if Email field is clickable"""
        return self.element_is_clickable(self.locators.EMAIL)
