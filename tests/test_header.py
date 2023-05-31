from data.data_urls import MAIN_PAGE_URL, CREATE_ACCOUNT_PAGE_URL
from pages.header_page import HeaderPage


class TestHeader:

    def test_tc_01_01_01_verify_the_greeting_message_is_displayed(self, driver):
        """Check greeting message == 'Default welcome msg!' and is visible"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        message = page.check_greeting_message()
        assert message is not None and message.text == "Default welcome msg!", \
            "The greeting message is not displayed or the text is incorrect"

    def test_tc_01_01_02_verify_the_display_and_interactivity_of_the_create_an_account_link(self, driver):
        """Check 'Create an account' link is displayed and underlined"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        link = page.check_create_account_page_link()
        page.action_move_to_element(link)
        assert link is not None and "underline" in link.value_of_css_property('text-decoration'), \
            "Link 'Create an account' is either not displayed or not underlined on hover"

    def test_tc_01_01_03_verify_the_correctness_create_an_account_link(self, driver):
        """Check 'Create an account' link click redirects to the account’s registration page and \
        the "Create New Customer Account" header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        create_account_link = page.check_create_account_page_link()
        create_account_link.click()
        page_header = page.check_create_account_page_header()
        assert driver.current_url == CREATE_ACCOUNT_PAGE_URL and page_header.text == "Create New Customer Account", \
            "Create an account page is either not opened or the page header is incorrect"

