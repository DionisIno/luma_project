from data.data_urls import MAIN_PAGE_URL
from pages.header_page import HeaderPage


class TestHeader:
    """Check greeting message == 'Default welcome msg!' and is visible"""
    def test_tc_01_01_01_verify_the_greeting_message_is_displayed(self, driver):
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        message = page.check_greeting_message()
        assert message is not None and message.text == "Default welcome msg!", \
            "The greeting message is not displayed or the text is incorrect"

