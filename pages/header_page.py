from locators.header_page_locators import HeaderPageLocators
from locators.create_account_page_locators import CreateAccountPageLocators
from locators.sign_in_page_locators import SingInPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    header_locators = HeaderPageLocators
    create_account_locators = CreateAccountPageLocators
    sign_in_locators = SingInPageLocators

    def click_and_return_element(self, locator):
        element = self.element_is_visible(locator)
        element.click()
        return element

    def check_greeting_message(self):
        return self.element_is_visible(self.header_locators.GREETING_MESSAGE)

    def check_create_account_page_link(self):
        return self.element_is_visible(self.header_locators.CREATE_AN_ACCOUNT)

    def check_create_account_page_header(self):
        return self.element_is_visible(self.create_account_locators.CREATE_NEW_CUSTOMER_ACCOUNT_HEADER)

    def check_sign_in_page_link(self):
        return self.element_is_visible(self.header_locators.SIGN_IN)

    def check_sign_in_page_header(self):
        return self.element_is_visible(self.sign_in_locators.PAGE_HEADER)

    def check_logo_link(self):
        return self.element_is_visible(self.header_locators.LOGO)


