from locators.sign_in_page_locators import SingInPageLocators
from pages.base_page import BasePage


class SignInPage(BasePage):
    locators = SingInPageLocators

    def check_h1_header(self):
        heading = self.element_is_visible(self.locators.PAGE_HEADER)
        return heading

    def check_registered_customers_heading(self):
        heading = self.element_is_visible(self.locators.REGISTERED_CUSTOMERS_HEADER)
        return heading

    def check_customer_email_label(self):
        '''This method verifies if email label is visible'''
        return self.element_is_visible(self.locators.CUSTOMER_EMAIL_LABEL)

    def check_customer_email_asterisk(self):
        return self.element_is_visible(self.locators.CUSTOMER_EMAIL_ASTERISK)
