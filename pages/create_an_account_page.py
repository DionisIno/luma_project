import time

import allure

from data.create_an_account import create_account_credentials
from locators.common_locators import CommonLocators
from locators.create_account_page_locators import CreateAccountPageLocators
from pages.base_page import BasePage


@allure.epic('Create An Account Page')
class CreateAccountPage(BasePage):
    locators = CreateAccountPageLocators
    common_locators = CommonLocators

    @allure.step('Check Create An Account h1 header is visible')
    def check_h1_header(self):
        """ This method verifies if h1 header is visible on the page """
        return self.element_is_visible(self.common_locators.HEADER_PAGE)

    @allure.step('Check Personal Informatio label is visible')
    def check_personal_information_label(self):
        """ This method verifies if Personal Information label is visible on the page """
        return self.element_is_visible(self.locators.PERSONAL_INFORMATION_LEGEND)

    @allure.step('Check First Name label is visible')
    def check_firstname_label(self):
        """ This method verifies if First Name label is visible """
        return self.element_is_visible(self.locators.FIRST_NAME_LABEL)

    @allure.step('Check Last Name label is visible')
    def check_lastname_label(self):
        """ This method verifies if Last Name label is visible """
        return self.element_is_visible(self.locators.LAST_NAME_LABEL)

    @allure.step('Check Email label is visible')
    def check_email_label(self):
        """ This method verifies if Email label is visible """
        return self.element_is_visible(self.locators.EMAIL_LABEL)

    @allure.step('Check Password label is visible')
    def check_password_label(self):
        """ This method verifies if Password label is visible """
        return self.element_is_visible(self.locators.PASSWORD_LABEL)

    @allure.step('Check Email input field is visible')
    def check_email_input(self):
        """ This method verifies if Email input is visible """
        return self.element_is_visible(self.locators.EMAIL)

    @allure.step('Check Password input field is visible')
    def check_password_input(self):
        """ This method verifies if Password input is visible """
        return self.element_is_visible(self.locators.PASSWORD)

    @allure.step('Check Confirm Password input field is visible')
    def check_confirm_password_input(self):
        """ This method verifies if Confirm Password input is visible """
        return self.element_is_visible(self.locators.PASSWORD_CONFIRMATION)

    @allure.step('Check Confirm Password label is visible')
    def check_password_confirmation_label(self):
        """ This method verifies if Confirm Password label is visible """
        return self.element_is_visible(self.locators.PASSWORD_CONFIRMATION_LABEL)

    @allure.step('Check Create An Account Button is visible')
    def check_create_an_account_is_visible(self):
        """ This method verifies if Create An Account is visible """
        return self.element_is_visible(self.locators.CREATE_AN_ACCOUNT_BUTTON)

    @allure.step('Check Message Password Error hint is visible')
    def check_message_password_error_hint(self):
        """ This method verifies if Message Password Error hint is visible """
        return self.element_is_visible(self.locators.MESSAGE_PASSWORD_ERROR)

    @allure.step('Check Create An Account Button is clickable')
    def check_create_an_account_is_clickable(self):
        """ This method verifies if Create An Account is clickable """
        return self.element_is_clickable(self.locators.CREATE_AN_ACCOUNT_BUTTON)

    @allure.step('Get property of the pseudo-class for required elements')
    def check_element_asteriks(self):
        """ This method gets property 'content' of the ':after' pseudo-class """
        return "return window.getComputedStyle(arguments[0], '::after').getPropertyValue('content')"

    @allure.step('Get property "background-color" of the pseudo-class')
    def check_element_color(self):
        """ This method gets property 'background-color' of the ':before' pseudo-class """
        return "return window.getComputedStyle(arguments[0],'::before').getPropertyValue('background-color')"

    @allure.step('Check First Name label is marked with asterisk')
    def check_firstname_label_asteriks(self):
        """ This method verifies if required first name label is marked with asterisk """
        firstname_label = self.check_firstname_label()
        return self.driver.execute_script(self.check_element_asteriks(), firstname_label)

    @allure.step('Check Last Name label is marked with asterisk')
    def check_lastname_label_asteriks(self):
        """ This method verifies if required last name field is marked with asterisk """
        lastname_label = self.check_lastname_label()
        return self.driver.execute_script(self.check_element_asteriks(), lastname_label)

    @allure.step('Check Email label is marked with asterisk')
    def check_email_label_asteriks(self):
        """ This method verifies if required email label is marked with asterisk """
        email_label = self.check_email_label()
        return self.driver.execute_script(self.check_element_asteriks(), email_label)

    @allure.step('Check Password label is marked with asterisk')
    def check_password_label_asteriks(self):
        """ This method verifies if required Password label is marked with asterisk """
        password_label = self.check_password_label()
        return self.driver.execute_script(self.check_element_asteriks(), password_label)

    @allure.step('Check Confirm Password label is marked with asterisk')
    def check_confirm_password_label_asteriks(self):
        """ This method verifies if required Confirm Password label is marked with asterisk """
        confirm_password_label = self.check_firstname_label()
        return self.driver.execute_script(self.check_element_asteriks(), confirm_password_label)

    @allure.step('Check First Name field is highlighted when clicked')
    def check_first_name_field_style_before_and_after_click(self):
        """ This method verifies if First name input field is highlighted when clicked"""
        before_activate = self.check_element_hover_style(self.locators.FIRST_NAME, 'box-shadow')
        element = self.element_is_visible(self.locators.FIRST_NAME)
        element.click()
        after_activate = self.check_element_hover_style(self.locators.FIRST_NAME, 'box-shadow')
        return before_activate, after_activate

    @allure.step("Check Email field is highlighted when clicked")
    def check_email_field_style_before_and_after_click(self):
        """ This method verifies if Email input field is highlighted when clicked """
        before_activate = self.check_element_hover_style(self.locators.EMAIL, 'box-shadow')
        element = self.element_is_visible(self.locators.EMAIL)
        element.click()
        after_activate = self.check_element_hover_style(self.locators.EMAIL, 'box-shadow')
        return before_activate, after_activate

    @allure.step('Check First Name label is highlighted when label is clicked')
    def check_first_name_field_style_before_and_after_click_on_label(self):
        """ This method verifies if First name input field is highlighted when label is clicked"""
        before_activate = self.check_element_hover_style(self.locators.FIRST_NAME, 'box-shadow')
        element = self.element_is_visible(self.locators.FIRST_NAME_LABEL)
        element.click()
        after_activate = self.check_element_hover_style(self.locators.FIRST_NAME, 'box-shadow')
        return before_activate, after_activate

    @allure.step('Check Last Name field is highlighted when clicked')
    def check_last_name_field_style_before_and_after_click(self):
        """ This method verifies if Last name input field is highlighted when clicked"""
        before_activate = self.check_element_hover_style(self.locators.LAST_NAME, 'box-shadow')
        element = self.element_is_visible(self.locators.LAST_NAME)
        element.click()
        after_activate = self.check_element_hover_style(self.locators.LAST_NAME, 'box-shadow')
        return before_activate, after_activate

    @allure.step('Check Last Name label is highlighted when label is clicked')
    def check_last_name_field_style_before_and_after_click_on_label(self):
        """ This method verifies if Last name input field is highlighted when label is clicked"""
        before_activate = self.check_element_hover_style(self.locators.LAST_NAME, 'box-shadow')
        element = self.element_is_visible(self.locators.LAST_NAME_LABEL)
        element.click()
        after_activate = self.check_element_hover_style(self.locators.LAST_NAME, 'box-shadow')
        return before_activate, after_activate

    @allure.step('Check Email label is highlighted when label is clicked')
    def check_email_field_style_before_and_after_click_on_label(self):
        """ This method verifies if Email input field is highlighted when label is clicked"""
        before_activate = self.check_element_hover_style(self.locators.EMAIL, 'box-shadow')
        element = self.element_is_visible(self.locators.EMAIL_LABEL)
        element.click()
        after_activate = self.check_element_hover_style(self.locators.EMAIL, 'box-shadow')
        return before_activate, after_activate

    @allure.step('Check Email label is highlighted when clicked')
    def check_email_field_style_before_and_after_click(self):
        """ This method verifies if Email input field is highlighted when clicked"""
        before_activate = self.check_element_hover_style(self.locators.EMAIL, 'box-shadow')
        element = self.element_is_visible(self.locators.EMAIL)
        element.click()
        after_activate = self.check_element_hover_style(self.locators.EMAIL, 'box-shadow')
        return before_activate, after_activate

    @allure.step('Check Password label is highlighted when label is clicked')
    def check_password_field_style_before_and_after_click_on_label(self):
        """ This method verifies if Password input field is highlighted when label is clicked"""
        before_activate = self.check_element_hover_style(self.locators.PASSWORD, 'box-shadow')
        element = self.element_is_visible(self.locators.PASSWORD_LABEL)
        element.click()
        after_activate = self.check_element_hover_style(self.locators.PASSWORD, 'box-shadow')
        return before_activate, after_activate

    @allure.step('Check Password label is highlighted when clicked')
    def check_password_field_style_before_and_after_click(self):
        """ This method verifies if Password input field is highlighted when clicked"""
        before_activate = self.check_element_hover_style(self.locators.PASSWORD, 'box-shadow')
        element = self.element_is_visible(self.locators.PASSWORD)
        element.click()
        after_activate = self.check_element_hover_style(self.locators.PASSWORD, 'box-shadow')
        return before_activate, after_activate

    @allure.step('Check Confirm Password label is highlighted when label is clicked')
    def check_confirm_password_field_style_before_and_after_click_on_label(self):
        """ This method verifies if Confirm Password input field is highlighted when label is clicked"""
        before_activate = self.check_element_hover_style(self.locators.PASSWORD_CONFIRMATION, 'box-shadow')
        element = self.element_is_visible(self.locators.PASSWORD_CONFIRMATION_LABEL)
        element.click()
        after_activate = self.check_element_hover_style(self.locators.PASSWORD_CONFIRMATION, 'box-shadow')
        return before_activate, after_activate

    @allure.step('Check Confirm Password label is highlighted when clicked')
    def check_confirm_password_field_style_before_and_after_click(self):
        """ This method verifies if Confirm Password input field is highlighted when clicked"""
        before_activate = self.check_element_hover_style(self.locators.PASSWORD_CONFIRMATION, 'box-shadow')
        element = self.element_is_visible(self.locators.PASSWORD_CONFIRMATION)
        element.click()
        after_activate = self.check_element_hover_style(self.locators.PASSWORD_CONFIRMATION, 'box-shadow')
        return before_activate, after_activate

    @allure.step('Check Sign Up checkbox label is visible')
    def check_sign_up_checkbox_label(self):
        """ This method verifies if Sign Up checkbox label is visible """
        return self.element_is_visible(self.locators.SIGN_UP_CHECKBOX_LABEL)

    @allure.step('Check Sign In Information label is visible')
    def check_sign_in_information_label(self):
        """ This method verifies if Sign in information label is visible """
        return self.element_is_visible(self.locators.SIGN_IN_INFORMATION_LABEL)

    @allure.step('Get checked property of checkbox using js')
    def get_checkbox_element(self):
        """ This method gets checked property of checkbox"""
        return "return arguments[0].checked"

    @allure.step('Get checked property of Sign Up checkbox')
    def check_checkbox_flag(self):
        """ This method gets checked property of checkbox"""
        checkbox = self.element_is_visible(self.locators.SIGN_UP_CHECKBOX)
        return self.driver.execute_script(self.get_checkbox_element(), checkbox)

    @allure.step('Check Password Strength hint is visible')
    def check_password_strength_hint(self):
        """ This method verifies if Password Strength hint is visible on the page """
        return self.element_is_visible(self.locators.PASSWORD_STRENGTH)

    @allure.step('Transform rgb color to hex form')
    def rgb_to_hex(self, rgb_color):
        red, green, blue = rgb_color[rgb_color.find("(") + 1:-1].split(",")
        hex_color = "".join(["#", format(int(red), '02x'), format(int(green), '02x'), format(int(blue), '02x')])
        return hex_color

    @allure.step('Check color password strength hint')
    def check_color_of_password_strength_hint(self):
        """ This method verifies if password strength hint has correct color """
        password_strength_note = self.check_password_strength_hint()
        return self.driver.execute_script(self.check_element_color(), password_strength_note)

    @allure.step('Check password strength hint and color')
    def check_password_strength_hint_with_weak_password(self):
        """ Verify password strength hint and color when password is weak less than 8 symbols """
        password_input = self.check_password_input()
        password_input.send_keys(create_account_credentials['weak_password1'])
        message_error_text = self.check_message_password_error_hint().text
        password_strength_hint_text = self.check_password_strength_hint().text
        rgb_color = self.check_color_of_password_strength_hint()
        hex_color = self.rgb_to_hex(rgb_color)
        return password_strength_hint_text, message_error_text, hex_color

    @allure.step('Create an account with registered e-mail')
    def create_with_email(self):
        """ Verify that customer can't Create An Account with registered e-mail"""
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('test')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('test')
        self.element_is_visible(self.locators.EMAIL).send_keys('teston120@mailinator.com')
        self.element_is_visible(self.locators.PASSWORD).send_keys('!Q@W3e4rASD')
        self.element_is_visible(self.locators.PASSWORD_CONFIRMATION).send_keys('!Q@W3e4rASD')
        self.element_is_clickable(self.locators.CREATE_AN_ACCOUNT_BUTTON).click()
        message = self.element_is_visible(self.locators.MESSAGE_ERROR)
        return message.text if message else None

    @allure.step('Create an account')
    def create_with_correct_data(self):
        """ Verify that customer can Create An Account with correct data"""
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('test717')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('testoviy717')
        self.element_is_visible(self.locators.EMAIL).send_keys('tes717ton754@mailitestov.test')
        self.element_is_visible(self.locators.PASSWORD).send_keys('!Q@W3e4rASD')
        self.element_is_visible(self.locators.PASSWORD_CONFIRMATION).send_keys('!Q@W3e4rASD')
        self.element_is_clickable(self.locators.CREATE_AN_ACCOUNT_BUTTON).click()
        message = self.element_is_visible(self.locators.MESSAGE_SUCCESS)
        return message.text if message else None

    @allure.step('Create an account with empty first name')
    def create_with_empty_first_name(self):
        """ Verify that customer can't Create An Account with empty first name"""
        self.element_is_visible(self.locators.LAST_NAME).send_keys('testoviy727')
        self.element_is_visible(self.locators.EMAIL).send_keys('tes727ton754@mailitestov.test')
        self.element_is_visible(self.locators.PASSWORD).send_keys('!Q@W3e4rASD')
        self.element_is_visible(self.locators.PASSWORD_CONFIRMATION).send_keys('!Q@W3e4rASD')
        self.element_is_clickable(self.locators.CREATE_AN_ACCOUNT_BUTTON).click()
        message = self.element_is_visible(self.locators.MESSAGE_FIRST_NAME_ERROR)
        return message.text if message else None

    @allure.step('Create an account with empty last name')
    def create_with_empty_last_name(self):
        """ Verify that customer can't Create An Account with empty last name"""
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('test727')
        self.element_is_visible(self.locators.EMAIL).send_keys('tes727ton754@mailitestov.test')
        self.element_is_visible(self.locators.PASSWORD).send_keys('!Q@W3e4rASD')
        self.element_is_visible(self.locators.PASSWORD_CONFIRMATION).send_keys('!Q@W3e4rASD')
        self.element_is_clickable(self.locators.CREATE_AN_ACCOUNT_BUTTON).click()
        message = self.element_is_visible(self.locators.MESSAGE_LAST_NAME_ERROR)
        return message.text if message else None

    @allure.step('Create an account with empty e-mail')
    def create_with_empty_email(self):
        """ Verify that customer can't Create An Account with empty e-mail"""
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('test727')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('testoviy727')
        self.element_is_visible(self.locators.PASSWORD).send_keys('!Q@W3e4rASD')
        self.element_is_visible(self.locators.PASSWORD_CONFIRMATION).send_keys('!Q@W3e4rASD')
        self.element_is_clickable(self.locators.CREATE_AN_ACCOUNT_BUTTON).click()
        message = self.element_is_visible(self.locators.MESSAGE_EMAIL_ERROR)
        return message.text if message else None

    @allure.step('Create an account with empty password')
    def create_with_empty_password(self):
        """ Verify that customer can't Create An Account with empty password"""
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('test727')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('testoviy727')
        self.element_is_visible(self.locators.EMAIL).send_keys('tes727ton754@mailitestov.test')
        self.element_is_visible(self.locators.PASSWORD_CONFIRMATION).send_keys('!Q@W3e4rASD')
        self.element_is_clickable(self.locators.CREATE_AN_ACCOUNT_BUTTON).click()
        message_strength = self.element_is_visible(self.locators.PASSWORD_STRENGTH)
        message = self.element_is_visible(self.locators.MESSAGE_PASSWORD_ERROR)
        return message_strength.text, message.text if message and message_strength else None

    @allure.step('Create an account with empty confirm password')
    def create_with_empty_confirm_password(self):
        """ Verify that customer can't Create An Account with empty confirm password"""
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('test727')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('testoviy727')
        self.element_is_visible(self.locators.EMAIL).send_keys('tes727ton754@mailitestov.test')
        self.element_is_visible(self.locators.PASSWORD).send_keys('!Q@W3e4rASD')
        self.element_is_clickable(self.locators.CREATE_AN_ACCOUNT_BUTTON).click()
        message = self.element_is_visible(self.locators.MESSAGE_PASSWORD_CONFIRMATION_ERROR)
        return message.text if message else None

    @allure.step('Create an account with incorrect confirm password')
    def create_with_incorrect_confirm_password(self):
        """ Verify that customer can't Create An Account with incorrect confirm password"""
        self.element_is_visible(self.locators.FIRST_NAME).send_keys('test727')
        self.element_is_visible(self.locators.LAST_NAME).send_keys('testoviy727')
        self.element_is_visible(self.locators.EMAIL).send_keys('tes727ton754@mailitestov.test')
        self.element_is_visible(self.locators.PASSWORD).send_keys('!Q@W3e4rASD')
        self.element_is_visible(self.locators.PASSWORD_CONFIRMATION).send_keys('!Q@W34rASD')
        self.element_is_clickable(self.locators.CREATE_AN_ACCOUNT_BUTTON).click()
        message = self.element_is_visible(self.locators.MESSAGE_PASSWORD_CONFIRMATION_ERROR)
        return message.text if message else None
