from locators.create_account_page_locators import CreateAccountPageLocators
from pages.base_page import BasePage


class CreateAccountPage(BasePage):
    locators = CreateAccountPageLocators

    def check_h1_header(self):
        heading = self.element_is_visible(self.locators.CREATE_NEW_CUSTOMER_ACCOUNT_HEADER)
        return heading
