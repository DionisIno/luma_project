from data.data_urls import MAIN_PAGE_URL, CREATE_ACCOUNT_PAGE_URL, SIGN_IN_URL
from pages.header_page import HeaderPage


class TestHeader:

    def test_tc_01_01_01_verify_the_greeting_message_is_displayed(self, driver):
        """Check greeting message == 'Default welcome msg!' and is visible"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        message = page.check_greeting_message()
        assert message is not None and message.text == "Default welcome msg!"

    def test_tc_01_01_02_verify_the_display_and_interactivity_of_the_create_an_account_link(self, driver):
        """Check 'Create an account' link is displayed and underlined"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        link = page.check_create_account_page_link()
        page.action_move_to_element(link)
        assert link is not None and "underline" in link.value_of_css_property('text-decoration')

    def test_tc_01_01_03_verify_the_correctness_create_an_account_link(self, driver):
        """Check 'Create an account' link click redirects to the account’s registration page and \
        the "Create New Customer Account" header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.click_and_return_element(page.header_locators.CREATE_AN_ACCOUNT)
        header = page.check_create_account_page_header()
        assert driver.current_url == CREATE_ACCOUNT_PAGE_URL and header.text == "Create New Customer Account"

    def test_tc_01_01_04_verify_the_display_and_interactivity_of_the_sign_in_link(self, driver):
        """Check 'Sign In' link is displayed and underlined"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        link = page.check_sign_in_page_link()
        page.action_move_to_element(link)
        assert link is not None and "underline" in link.value_of_css_property('text-decoration')

    def test_tc_01_01_05_verify_the_correctness_sign_in_link(self, driver):
        """Check 'Sign In' link click redirects to the login page and \
                the "Customer Login" header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.click_and_return_element(page.header_locators.SIGN_IN)
        header = page.check_sign_in_page_header()
        assert driver.current_url == SIGN_IN_URL and header.text == "Customer Login"

    def test_tc_01_02_16_verify_the_display_and_interactivity_of_the_logo(self, driver):
        """Check that the cursor changes to a 'hand' indicating the logo is a clickable element, \
        and that clicking on it causes the page to reload and redirect to the main page"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        logo = page.check_logo_link()
        page.action_move_to_element(logo)
        cursor_type = logo.value_of_css_property('cursor')
        page.click_and_return_element(page.header_locators.LOGO)
        assert cursor_type == 'pointer' and driver.current_url == MAIN_PAGE_URL

