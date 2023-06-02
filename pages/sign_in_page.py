from locators.sign_in_page_locators import SingInPageLocators
from pages.base_page import BasePage


class SignInPage(BasePage):
    locators = SingInPageLocators

    def check_h1_header(self):
        """This method verifies if h1 header is visible on the page"""
        return self.element_is_visible(self.locators.PAGE_HEADER)

    def check_registered_customers_heading(self):
        """This method verifies if heading is visible"""
        return self.element_is_visible(self.locators.REGISTERED_CUSTOMERS_HEADER)

    def check_customer_email_label(self):
        """This method verifies if Email label is visible"""
        return self.element_is_visible(self.locators.CUSTOMER_EMAIL_LABEL)

    def check_customer_email_asterisk(self):
        """This method verifies if asterisk is displayed next to Email label"""
        email_label = self.check_customer_email_label()
        asterisk_script = "return window.getComputedStyle(arguments[0],'::after').getPropertyValue('content')"
        return self.driver.execute_script(asterisk_script, email_label)

    def check_customer_password_field_is_clickable(self):
        """This method verifies if Password field is clickable"""
        return self.element_is_clickable(self.locators.CUSTOMER_PASSWORD)

    def fill_in_password_field(self, password):
        """This method fills out the Password field with provided password"""
        password_input = self.check_customer_password_field_is_clickable()
        password_input.send_keys(password)
        return password_input

    def check_password_value_masking(self, password):
        """
        This method verifies if the type attribute of the password input field
        is set to "password" indicating that password value is masked on UI
        """
        password_input = self.fill_in_password_field(password)
        return password_input.get_attribute('type')
