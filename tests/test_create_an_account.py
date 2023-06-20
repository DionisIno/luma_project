import allure
import pytest

from data.data_urls import CREATE_ACCOUNT_PAGE_URL
from pages.create_an_account_page import CreateAccountPage

create_account_data = {
    "h1_heading": 'Create New Customer Account',
    "new_account_personal_information_heading": 'Personal Information'
}


@allure.epic('Test Create an AnAccount')
class TestCreateAnAccount:
    @allure.title('test 04.01.01 h1_heading')
    def test_04_01_01_h1_heading(self, driver):
        """ Verify that the Create An Account page heading is present. """
        create_account_page = CreateAccountPage(driver, CREATE_ACCOUNT_PAGE_URL)
        create_account_page.open()
        h1_heading = create_account_page.check_h1_header()
        assert h1_heading is not None and h1_heading.text == create_account_data['h1_heading'], \
            "H1 Heading is not present"

    @allure.title('test 04.02.08 create an account with registered email')
    def test_tc_04_02_08_create_account_with_registered_email(self, driver):
        """ Verify that customer can't Create An Account with registered email before"""
        page = CreateAccountPage(driver, CREATE_ACCOUNT_PAGE_URL)
        page.open()
        message = page.create_with_email()
        assert message == 'There is already an account with this email address. If you are sure that it is your' \
                          ' email address, click here to get your password and access your account.', "No error message"

    @allure.title('test 04.02.01 create an account with correct data')
    # @pytest.mark.skip(reason="customer will Create An Account with correct data")
    def test_tc_04_02_01_create_account_with_correct_data(self, driver):
        """ Verify that customer can Create An Account with correct data"""
        page = CreateAccountPage(driver, CREATE_ACCOUNT_PAGE_URL)
        page.open()
        message = page.create_with_correct_data()
        assert message == 'Thank you for registering with Main Website Store.', "No success message"
