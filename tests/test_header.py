from data.data_urls import MAIN_PAGE_URL
from pages.header_page import HeaderPage


class TestHeader:

    def test_tc_01_01_01_verify_the_greeting_message_is_displayed(self, driver):
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        assert page.check_greeting_message(), "The greeting message is not displayed"

