from locators.header_page_locators import HeaderPageLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):
    locators = HeaderPageLocators

    def check_greeting_message(self):
        message = self.element_is_visible(self.locators.GREETING_MESSAGE)
        return message

