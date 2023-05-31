from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    locators = HeaderPageLocators

    def check_greeting_message(self):
        message = self.element_is_visible(self.locators.GREETING_MESSAGE)
        return message

    def check_create_account_link(self):
        link = self.element_is_visible(self.locators.CREATE_AN_ACCOUNT)
        return link

