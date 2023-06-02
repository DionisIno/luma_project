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
        return self.element_is_visible(self.locators.CUSTOMER_EMAIL_LABEL)

    def check_customer_email_asterisk(self):
        email_label = self.element_is_visible(self.locators.CUSTOMER_EMAIL_LABEL)
        asterisk_script = "return window.getComputedStyle(arguments[0],'::after').getPropertyValue('content')"
        return self.driver.execute_script(asterisk_script, email_label)

