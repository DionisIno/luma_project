import allure
import pytest

from data.data_urls import CREATE_ACCOUNT_PAGE_URL
from pages.create_an_account_page import CreateAccountPage
from data.create_an_account import create_account_data


@pytest.fixture(scope="function")
def create_account_page(driver):
    create_account_page = CreateAccountPage(driver, CREATE_ACCOUNT_PAGE_URL)
    create_account_page.open()
    return create_account_page


@allure.epic('Create An Account')
class TestCreateAnAccount:
    @allure.title('TC 04_01_01 Verify Create An Account Page h1 Header')
    def test_04_01_01_h1_heading(self, create_account_page):
        """ Verify that the Create An Account page heading is present. """
        h1_heading = create_account_page.check_h1_header()
        assert h1_heading and h1_heading.text == create_account_data['h1_heading'], \
            "h1 heading is not present"

    @allure.title('TC 04_01_02 Verify Personal Information heading')
    def test_04_01_02_personal_information_heading(self, create_account_page):
        """ Verify that Personal Information heading is present """
        personal_information_legend = create_account_page.check_personal_information_label()
        assert personal_information_legend.text == create_account_data['personal_information_label'], \
            "Personal information legend is incorrect or not present"

    @allure.title('TC 04_01_03 Verify presence of First name label and the required asterisk')
    def test_04_01_03_firstname_labeled(self, create_account_page):
        """ Verify presence of First name label and the required asterisk """
        firstname_label = create_account_page.check_firstname_label()
        asterisk = create_account_page.check_firstname_label_asteriks()
        assert firstname_label.text == create_account_data['firstname_label'] and asterisk == '"*"', \
            "First name label is not present or not displayed"

    @allure.title('TC 04_01_04 Verify First name input field highlighting on label click')
    def test_04_01_04_firstname_highlighted_by_label(self, create_account_page):
        """ Verify that First name input field highlighted when label is clicked"""
        before_activate, after_activate = create_account_page.\
            check_first_name_field_style_before_and_after_click_on_label()
        assert before_activate != after_activate, "First name field is not highlighted when label is clicked"

    @allure.title('TC 04_01_05 Verify First name input field highlighting on click')
    def test_04_01_05_firstname_field_is_highlighted(self, create_account_page):
        """ Verify that First name input field highlighted when clicked"""
        before_activate, after_activate = create_account_page.\
            check_first_name_field_style_before_and_after_click()
        assert before_activate != after_activate, "First name field is not highlighted when clicked"

    @allure.title('TC 04_01_06')
    def test_04_01_06_lastname_labeled(self, create_account_page):
        """ Verify presence of Last name label and the required asterisk """
        lastname_label = create_account_page.check_lastname_label()
        asterisk = create_account_page.check_firstname_label_asteriks()
        assert lastname_label.text == create_account_data['lastname_label'] and asterisk == '"*"', \
            "Last name label is not present or not displayed"

    @allure.title('TC 04_01_07 Verify Last name input field highlighting on label click')
    def test_04_01_04_lastname_highlighted_by_label(self, create_account_page):
        """ Verify that Last name input field highlighted when label is clicked"""
        before_activate, after_activate = create_account_page.\
            check_last_name_field_style_before_and_after_click_on_label()
        assert before_activate != after_activate, "Last name field is not highlighted when label is clicked"

    @allure.title('TC 04_01_08 Verify Last name input field highlighting on click')
    def test_04_01_08_lastname_field_is_highlighted(self, create_account_page):
        """ Verify that Last name input field highlighted when clicked"""
        before_activate, after_activate = create_account_page. \
            check_last_name_field_style_before_and_after_click()
        assert before_activate != after_activate, "Last name field is not highlighted when clicked"

    @allure.title('TC 04_01_09 Verify checkbox is present and unchecked')
    def test_04_01_09_sign_up_for_letters_checkbox(self, create_account_page):
        """ Verify that checkbox is present and unchecked"""
        sign_up_checkbox = create_account_page.check_sign_up_checkbox_label()
        flag_checkbox = create_account_page.check_checkbox_flag()
        # flag_checkbox = sign_up_checkbox.is_selected()
        assert sign_up_checkbox.text == create_account_data['sign_up_label'] \
            and flag_checkbox is False, \
            "Sign Up for Newsletter checkbox is not presented or not unchecked"

    @allure.title('TC 04_01_09 Verify checkbox is present and unchecked')
    def test_04_01_10_sign_in_information_label(self, create_account_page):
        """ Verify that checkbox is present and unchecked"""
        sign_in_information_label = create_account_page.check_sign_in_information_label()
        assert sign_in_information_label.text == create_account_data["sign_in_information_label"], \
            "Sign in Information label is not presented or not visible"

    @allure.title('test 04.02.08 create an account with registered email')
    def test_tc_04_02_08_create_account_with_registered_email(self, driver):
        """ Verify that customer can't Create An Account with registered email before """
        page = CreateAccountPage(driver, CREATE_ACCOUNT_PAGE_URL)
        page.open()
        message = page.create_with_email()
        assert message == 'There is already an account with this email address. If you are sure that it is your' \
                          ' email address, click here to get your password and access your account.', "No error message"

    @allure.title('test 04.02.01 create an account with correct data')
    @pytest.mark.skip(reason="customer will Create An Account with correct data")
    def test_tc_04_02_01_create_account_with_correct_data(self, driver):
        """ Verify that customer can Create An Account with correct data"""
        page = CreateAccountPage(driver, CREATE_ACCOUNT_PAGE_URL)
        page.open()
        message = page.create_with_correct_data()
        assert message == 'Thank you for registering with Main Website Store.', "No success message"

    @allure.title('test 04.02.02 create an account with empty first name')
    def test_tc_04_02_02_create_account_with_empty_first_name(self, driver):
        """ Verify that customer can't Create An Account with empty first name"""
        page = CreateAccountPage(driver, CREATE_ACCOUNT_PAGE_URL)
        page.open()
        message = page.create_with_empty_first_name()
        assert message == 'This is a required field.', "No message"

    @allure.title('test 04.02.03 create an account with empty last name')
    def test_tc_04_02_03_create_account_with_empty_last_name(self, driver):
        """ Verify that customer can't Create An Account with empty last name"""
        page = CreateAccountPage(driver, CREATE_ACCOUNT_PAGE_URL)
        page.open()
        message = page.create_with_empty_last_name()
        assert message == 'This is a required field.', "No message"

    @allure.title('test 04.02.04 create an account with empty e-mail')
    def test_tc_04_02_04_create_account_with_empty_email(self, driver):
        """ Verify that customer can't Create An Account with empty e-mail"""
        page = CreateAccountPage(driver, CREATE_ACCOUNT_PAGE_URL)
        page.open()
        message = page.create_with_empty_email()
        assert message == 'This is a required field.', "No message"

    @allure.title('test 04.02.05 create an account with empty password')
    def test_tc_04_02_05_create_account_with_empty_password(self, driver):
        """ Verify that customer can't Create An Account with empty password"""
        page = CreateAccountPage(driver, CREATE_ACCOUNT_PAGE_URL)
        page.open()
        message = page.create_with_empty_password()
        assert message == ('Password Strength: No Password', 'This is a required field.'), "No message"

    @allure.title('test 04.02.06 create an account with empty confirm password')
    def test_tc_04_02_06_create_account_with_empty_confirm_password(self, driver):
        """ Verify that customer can't Create An Account with empty confirm password"""
        page = CreateAccountPage(driver, CREATE_ACCOUNT_PAGE_URL)
        page.open()
        message = page.create_with_empty_confirm_password()
        assert message == 'This is a required field.', "No message"

    @allure.title('test 04.02.07 create an account with incorrect confirm password')
    def test_tc_04_02_07_create_account_with_incorrect_confirm_password(self, driver):
        """ Verify that customer can't Create An Account with incorrect confirm password"""
        page = CreateAccountPage(driver, CREATE_ACCOUNT_PAGE_URL)
        page.open()
        message = page.create_with_incorrect_confirm_password()
        assert message == 'Please enter the same value again.', "No message"
