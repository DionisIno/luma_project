import re
import allure

from locators.sign_in_page_locators import SingInPageLocators
from pages.base_page import BasePage


@allure.epic('Sign In Page')
class SignInPage(BasePage):
    locators = SingInPageLocators

    @allure.step('Check Sign In h1 header is visible')
    def check_h1_header(self):
        '''This method verifies if h1 header is visible on the page'''
        return self.element_is_visible(self.locators.PAGE_HEADER)

    @allure.step('Check Registered Customers heading is visible')
    def check_registered_customers_heading(self):
        """This method verifies if heading is visible"""
        return self.element_is_visible(self.locators.REGISTERED_CUSTOMERS_HEADER)

    @allure.step('Check Email label is visible')
    def check_customer_email_label(self):
        """This method verifies if Email label is visible"""
        return self.element_is_visible(self.locators.CUSTOMER_EMAIL_LABEL)

    @allure.step('Get required element visible')
    def find_required_element(self):
        """This method finds the required element, making it visible to the user."""
        return "return window.getComputedStyle(arguments[0],'::after').getPropertyValue('content')"

    @allure.step('Check Email asterisk is visible')
    def check_customer_email_asterisk(self):
        """This method verifies if asterisk is displayed next to Email label"""
        email_label = self.check_customer_email_label()
        asterisk_script = self.find_required_element()
        return self.driver.execute_script(asterisk_script, email_label)

    @allure.step('Check Email field is clickable')
    def check_customer_email_field_is_clickable(self):
        """This method verifies if Email field is clickable"""
        return self.element_is_clickable(self.locators.CUSTOMER_EMAIL)

    @allure.step('Activate the field and get the styles before and after activation')
    def activate_field_and_check_style(self, locator):
        """
        This method activates the field and checks if the style of the field changes upon activation.
        It returns the styles before and after activation for comparison.
        """
        initial_box_shadow = self.check_element_hover_style(locator, 'box-shadow', 5)
        self.click_and_return_element(locator)
        active_box_shadow = self.check_element_hover_style(locator, 'box-shadow', 5)
        return initial_box_shadow, active_box_shadow

    @allure.step('Activate Email field and check style')
    def activate_email_field_and_check_style(self):
        """
        This method activates the Email field
        and checks if the style of the field changes upon activation.
        """
        return self.activate_field_and_check_style(self.locators.CUSTOMER_EMAIL)

    @allure.step('Fill in Email field')
    def fill_in_email_field(self, email):
        """This method fills in Email field with provided email"""
        email_input = self.check_customer_email_field_is_clickable()
        email_input.click()
        email_input.clear()
        email_input.send_keys(email)
        return email_input

    @allure.step('Get Email field attribute')
    def get_email_field_attribute(self, attribute):
        """This method fills in Email field with provided email"""
        # email_input = self.check_customer_email_field_is_clickable()
        return self.check_customer_email_field_is_clickable().get_attribute(attribute)

    @allure.step('Check Password field is clickable')
    def check_customer_password_field_is_clickable(self):
        """This method verifies if Password field is clickable"""
        return self.element_is_clickable(self.locators.CUSTOMER_PASSWORD)

    @allure.step('Fill in Password field')
    def fill_in_password_field(self, password):
        """This method fills in Password field with provided password"""
        password_input = self.check_customer_password_field_is_clickable()
        password_input.send_keys(password)
        return password_input

    @allure.step('Check Password field is clickable')
    def check_password_value_masking(self, password):
        """
        This method verifies if the type attribute of the password input field
        is set to "password" indicating that password value is masked on UI
        """
        password_input = self.fill_in_password_field(password)
        return password_input.get_attribute('type')

    @allure.step('Check Email field for correct email format')
    def is_valid_email(self, email):
        """This method is validation Email field for correct email format"""
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        valid_email = re.match(pattern, email)
        return valid_email is not None

    @allure.step('Get error message')
    def get_error_message(self, locator):
        """
        This method validates that the error message is displayed
        on attempt to sign in with incorrect credentials.
        """
        error = self.element_is_visible(locator)
        return error.text if error else None

    @allure.step('Check Email field for correct email format')
    def check_sign_in_button_is_visible(self):
        """This method verifies if sign-in button field is visible"""
        return self.element_is_clickable(self.locators.SIGN_IN_BUTTON)

    @allure.step('Check Sign In button is visible')
    def click_sign_in_button(self):
        """This method clicks on sign-in button"""
        self.check_sign_in_button_is_visible().click()

    @allure.step('Check Forgot Your Password_link')
    def check_forgot_your_password_link(self):
        """This method finds 'Forgot your password? link"""
        return self.element_is_visible(self.locators.FORGOT_PASSWORD)

    @allure.step('Check New Customers heading is visible')
    def check_new_customers_heading(self):
        """This method verifies if heading is visible"""
        return self.element_is_visible(self.locators.NEW_CUSTOMERS_HEADER)

    @allure.step('Check New Customers note is visible')
    def check_new_customers_note(self):
        """This method verifies if note is visible"""
        return self.element_is_visible(self.locators.NEW_CUSTOMERS_NOTE)
