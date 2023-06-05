import pytest
from selenium.webdriver.common.by import By
from data.data_urls import MAIN_PAGE_URL, DATA_1
from pages.footer_page import FooterPage


class TestFooter:
    def test_tc_02_01_05_verify_the_search_terms_link_is_displayed(self, driver):
        """Check search terms link is displayed"""
        page = FooterPage(driver, MAIN_PAGE_URL)
        page.open()
        search_terms_link = page.check_search_terms_link_is_visible()
        assert search_terms_link is True, "The element is not visible"


@pytest.mark.parametrize('URL', DATA_1)
def test_tc_02_01_05_verify_the_search_terms_link_is_visible_on_each_page_specified_in_data(driver, URL):
    page = FooterPage(driver, url=URL)
    page.open()
    search_terms_link = page.check_search_terms_link_is_visible()
    assert search_terms_link is True, "The element is not visible"
