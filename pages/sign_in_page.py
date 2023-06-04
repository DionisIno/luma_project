import re

from locators.sign_in_page_locators import SingInPageLocators
from pages.base_page import BasePage


class SignInPage(BasePage):
    locators = SingInPageLocators

    def check_h1_header(self):
        '''This method verifies if h1 header is visible on the page'''
        return self.element_is_visible(self.locators.PAGE_HEADER)

    def check_registered_customers_heading(self):
        """This method verifies if heading is visible"""
        return self.element_is_visible(self.locators.REGISTERED_CUSTOMERS_HEADER)

    def check_customer_email_label(self):
        """This method verifies if Email label is visible"""
        return self.element_is_visible(self.locators.CUSTOMER_EMAIL_LABEL)

    def find_required_element(self):
        """This method finds the required element, making it visible to the user."""
        return "return window.getComputedStyle(arguments[0],'::after').getPropertyValue('content')"

    def check_customer_email_asterisk(self):
        """This method verifies if asterisk is displayed next to Email label"""
        email_label = self.check_customer_email_label()
        asterisk_script = self.find_required_element()
        return self.driver.execute_script(asterisk_script, email_label)

    def check_customer_email_field_is_clickable(self):
        """This method verifies if Email field is clickable"""
        return self.element_is_clickable(self.locators.CUSTOMER_EMAIL)

    def fill_in_email_field(self, email):
        """This method fills in Email field with provided email"""
        email_input = self.check_customer_email_field_is_clickable()
        email_input.click()
        email_input.clear()
        email_input.send_keys(email)
        return email_input

    def get_email_field_attribute(self, attribute):
        """This method fills in Email field with provided email"""
        # email_input = self.check_customer_email_field_is_clickable()
        return self.check_customer_email_field_is_clickable().get_attribute(attribute)

    def check_customer_password_field_is_clickable(self):
        """This method verifies if Password field is clickable"""
        return self.element_is_clickable(self.locators.CUSTOMER_PASSWORD)

    def fill_in_password_field(self, password):
        """This method fills in Password field with provided password"""
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

    def is_valid_email(self, email):
        """This method is validation Email field for correct email format"""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        valid_email = re.match(pattern, email)
        return valid_email is not None

    def get_error_message(self):
        """
        This method validates that the error message is displayed
        when an incorrect email format is entered.
        """
        error_element = self.driver.find_element_by_css_selector("#email-error")
        return error_element.text if error_element else None

    def check_sign_in_button_is_visible(self):
        """This method verifies if Email field is visible"""
        return self.element_is_clickable(self.locators.SIGN_IN_BUTTON)

    def click_sign_in_button(self):
        """This method verifies if the sign-in button is clickable"""
        sign_in_button = self.check_sign_in_button_is_visible()
        try:
            sign_in_button.click()
        except:
            sign_in_button.click()
        return sign_in_button
