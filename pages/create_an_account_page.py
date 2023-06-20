import time

import allure

from locators.create_account_page_locators import CreateAccountPageLocators
from pages.base_page import BasePage


@allure.epic('Create an Account Page')
class CreateAccountPage(BasePage):
    locators = CreateAccountPageLocators

    @allure.step('Check h1 header')
    def check_h1_header(self):
        heading = self.element_is_visible(self.locators.CREATE_NEW_CUSTOMER_ACCOUNT_HEADER)
        return heading

    @allure.step('Create an account with registered e-mail')
    def create_with_email(self):
        """ Verify that customer can't Create An Account with registered e-mail"""
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('test')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('test')
        self.element_is_visible(self.locators.EMAIL).send_keys('teston120@mailinator.com')
        self.element_is_visible(self.locators.PASSWORD).send_keys('!Q@W3e4rASD')
        self.element_is_visible(self.locators.PASSWORD_CONFIRMATION).send_keys('!Q@W3e4rASD')
        self.element_is_clickable(self.locators.CREATE_AN_ACCOUNT_BUTTON).click()
        message = self.element_is_visible(self.locators.MESSAGE_ERROR)
        return message.text if message else None

    @allure.step('Create an account')
    def create_with_correct_data(self):
        """ Verify that customer can Create An Account with correct data"""
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('test2')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('testoviy2')
        self.element_is_visible(self.locators.EMAIL).send_keys('testoviy754@mailitestov.test')
        self.element_is_visible(self.locators.PASSWORD).send_keys('!Q@W3e4rASD')
        self.element_is_visible(self.locators.PASSWORD_CONFIRMATION).send_keys('!Q@W3e4rASD')
        self.element_is_clickable(self.locators.CREATE_AN_ACCOUNT_BUTTON).click()
        message = self.element_is_visible(self.locators.MESSAGE_SUCCESS)
        return message.text if message else None
