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
