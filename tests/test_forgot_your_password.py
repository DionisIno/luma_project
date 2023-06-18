import pytest
import allure

from locators.forgot_your_password_locators import ForgotYourPasswordPageLocators
from pages.forgot_your_password_page import ForgotYourPasswordPage
from data.forgot_your_password_data import forgot_your_password_data
from data.data_urls import FORGOT_YOUR_PASSWORD_URL

@pytest.fixture(scope="function")
def forgot_psw_page(driver):
    forgot_psw_page = ForgotYourPasswordPage(driver, FORGOT_YOUR_PASSWORD_URL)
    forgot_psw_page.open()
    return forgot_psw_page

@allure.epic('Forgot Your Password Page')
class TestForgotYourPassword:
    @allure.title('TC 17.01.01 Verify Forgot Your Password Page h1 Header')
    def test_17_01_01_h1_heading(self, driver, forgot_psw_page):
        """Check Login Page Heading is present """
        h1_heading = forgot_psw_page.check_forgot_psw_h1_header()
        assert h1_heading is not None and h1_heading.text == forgot_your_password_data["h1_heading"], \
            "Forgot Your Password H1 Header is incorrect or not present"

    @allure.title('TC 17.01.02 Verify Forgot Your Password note')
    def test_17_01_02_registered_customers_note(self, driver, forgot_psw_page):
        """Check Registered Customers note is present """
        note = forgot_psw_page.check_forgot_your_psw_note()
        assert note is not None and note.text == forgot_psw_page["forgot_your_password_note"], \
            "Forgot Your Password note is incorrect or not present"
