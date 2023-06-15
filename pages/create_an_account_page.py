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
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('test')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('test')
        self.element_is_visible(self.locators.EMAIL).send_keys('teston120@mailinator.com')
        self.element_is_visible(self.locators.PASSWORD).send_keys('!Q@W3e4r')
        self.element_is_visible(self.locators.PASSWORD_CONFIRMATION).send_keys('!Q@W3e4r')
        self.element_is_clickable(self.locators.CREATE_AN_ACCOUNT_BUTTON).click()
        massage = self.element_is_visible(self.locators.MASSAGE_REGISTERED_EMAIL)
        return massage.text
