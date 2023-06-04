from data.data_urls import MAIN_PAGE_URL, CREATE_ACCOUNT_PAGE_URL, SIGN_IN_URL, SALE_PAGE_URL
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
        assert "underline" in page.check_element_hover_style(page.header_locators.CREATE_AN_ACCOUNT, 'text-decoration'), \
            "Link 'Create an account' is either not displayed or not underlined on hover"

    def test_tc_01_01_03_verify_the_correctness_create_an_account_link(self, driver):
        """Check 'Create an account' link click redirects to the account’s registration page and \
        the "Create New Customer Account" header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.click_and_return_element(page.header_locators.CREATE_AN_ACCOUNT)
        header = page.check_create_account_page_header()
        assert driver.current_url == CREATE_ACCOUNT_PAGE_URL and header.text == "Create New Customer Account", \
            "Create an account page is either not opened or the page header is incorrect"

    def test_tc_01_01_04_verify_the_display_and_interactivity_of_the_sign_in_link(self, driver):
        """Check 'Sign In' link is displayed and underlined"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        assert "underline" in page.check_element_hover_style(page.header_locators.SIGN_IN, 'text-decoration'), \
            "Link 'Sign In' is either not displayed or not underlined on hover"

    def test_tc_01_01_05_verify_the_correctness_sign_in_link(self, driver):
        """Check 'Sign In' link click redirects to the login page and \
                the "Customer Login" header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.click_and_return_element(page.header_locators.SIGN_IN)
        header = page.check_sign_in_page_header()
        assert driver.current_url == SIGN_IN_URL and header.text == "Customer Login", \
            "Sign In page is either not opened or the page header is incorrect"

    def test_tc_01_02_16_verify_the_display_and_interactivity_of_the_logo(self, driver):
        """Check that the cursor changes to a 'hand' indicating the logo is a clickable element, \
        and that clicking on it causes the page to reload and redirect to the main page"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        assert "pointer" in page.check_element_hover_style(page.header_locators.LOGO,
                                                           'cursor'), \
            "Failed: The cursor does not change to a 'hand' when hovering over the logo"
        page.click_and_return_element(page.header_locators.LOGO)
        assert driver.current_url == MAIN_PAGE_URL, "Failed: Clicking on the logo does not redirect to the main page"

    def test_tc_01_03_53_verify_correctly_redirected_the_link_sale(self, driver):
        """Verify 'Sale' link click redirected to the Sale page and \
                the "Sale" header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.click_and_return_element(page.header_locators.SALE)
        header = page.verify_redirected_the_link_sale()
        assert driver.current_url == SALE_PAGE_URL and header.text == "Sale", \
            "Sale page isn't opened or the page header is incorrect"

    def test_tc_01_02_17_verify_the_display_and_interactivity_of_the_cart_icon(self, driver):
        """Verify hovering over the shopping cart icon changes the cursor to a "hand," indicating that the cart is a \
        clickable element, click on it and the message "You have no items in your shopping cart." appears"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        assert "pointer" in page.check_element_hover_style(page.header_locators.CART_ICON, 'cursor'), \
            "Failed: The cursor does not change to a 'hand' when hovering over the cart icon"
        page.click_and_return_element(page.header_locators.CART_ICON)
        assert page.check_cart_message() == "You have no items in your shopping cart.", \
            "Cart icon test failed: incorrect cart message"

