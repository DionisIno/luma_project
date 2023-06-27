import allure

from locators.create_account_page_locators import CreateAccountPageLocators
from pages.base_page import BasePage


@allure.epic('Create An Account Page')
class CreateAccountPage(BasePage):
    locators = CreateAccountPageLocators

    @allure.step('Check Create An Account h1 header is visible')
    def check_h1_header(self):
        """ This method verifies if h1 header is visible on the page """
        return self.element_is_visible(self.locators.CREATE_AN_ACCOUNT_HEADER)

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

    @allure.step('Get property of the pseudo-class for required elements')
    def check_element_asteriks(self):
        """ This method gets property 'content' of the ':after' pseudo-class """
        return "return window.getComputedStyle(arguments[0], '::after').getPropertyValue('content')"

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

    @allure.step('Check First Name field is highlighted when clicked')
    def check_first_name_field_style_before_and_after_click(self):
        """ This method verifies if First name input field is highlighted when clicked"""
        before_activate = self.check_element_hover_style(self.locators.FIRST_NAME, 'box-shadow')
        element = self.element_is_visible(self.locators.FIRST_NAME)
        element.click()
        after_activate = self.check_element_hover_style(self.locators.FIRST_NAME, 'box-shadow')
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

    # @allure.step('Check First Name field is clickable')
    # def check_first_name_field_is_clickable(self):
    #     """This method verifies if First Name field is clickable"""
    #     return self.element_is_clickable(self.locators.FIRST_NAME)

    @allure.step('Check Sign Up checkbox label is visible')
    def check_sign_up_checkbox_label(self):
        """ This method verifies if Sign Up checkbox label is visible """
        return self.element_is_visible(self.locators.SIGN_UP_CHECKBOX_LABEL)

    # def get_active_element(self):
    #     """ This method gets active elements using js """
    #     get_active_script = "return document.activeElement"
    #     return self.driver.execute_script(get_active_script)

    @allure.step('Get checked property of checkbox using js')
    def get_checkbox_element(self):
        """ This method gets checked property of checkbox"""
        return "return arguments[0].checked"

    @allure.step('Get checked property of Sign Up checkbox')
    def check_checkbox_flag(self):
        """ This method gets checked property of checkbox"""
        checkbox = self.element_is_visible(self.locators.SIGN_UP_CHECKBOX)
        return self.driver.execute_script(self.get_checkbox_element(), checkbox)

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
