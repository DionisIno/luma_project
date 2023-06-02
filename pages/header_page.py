from locators.header_page_locators import HeaderPageLocators
from locators.create_account_page_locators import CreateAccountPageLocators
from locators.sign_in_page_locators import SingInPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    header_locators = HeaderPageLocators
    create_account_locators = CreateAccountPageLocators
    sign_in_locators = SingInPageLocators

    def check_greeting_message(self):
        message = self.element_is_visible(self.header_locators.GREETING_MESSAGE)
        return message

    def check_create_account_page_link(self):
        link = self.element_is_visible(self.header_locators.CREATE_AN_ACCOUNT)
        return link

    def check_create_account_page_header(self):
        header = self.element_is_visible(self.create_account_locators.CREATE_NEW_CUSTOMER_ACCOUNT_HEADER)
        return header

    def check_sign_in_page_link(self):
        link = self.element_is_visible(self.header_locators.SIGN_IN)
        return link

    def check_sign_in_page_header(self):
        header = self.element_is_visible(self.sign_in_locators.PAGE_HEADER)
        return header

