from locators.create_account_page_locators import CreateAccountPageLocators
from pages.base_page import BasePage


class CreateAccountPage(BasePage):
    locators = CreateAccountPageLocators

    def check_h1_header(self):
        return self.element_is_visible(self.locators.CREATE_AN_ACCOUNT_HEADER)

    def check_firstname_label(self):
        return self.element_is_visible(self.locators.CREATE_AN_ACCOUNT_FIRSTNAME)

    def check_firstname_field_is_clickable(self):
        return self.element_is_clickable(self.locators.CREATE_AN_ACCOUNT_FIRSTNAME)

