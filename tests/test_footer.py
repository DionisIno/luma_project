import pytest
from selenium.webdriver.common.by import By
from data.data_urls import MAIN_PAGE_URL, DATA_1
from pages.footer_page import FooterPage
from locators.footer_page_locators import FooterPageLocators


class TestFooter:

    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_05_verify_the_search_terms_link_is_visible_on_each_page_specified_in_data(self, driver, URL):
        """Check search terms link is displayed on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        search_terms_link = page.check_search_terms_link_is_visible()
        assert search_terms_link is True, "The element is not visible"


class TestFooterSuits:

    @pytest.mark.parametrize('element', FooterPageLocators.DATA_2)
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_01_uniform_footer_elements_display_on_each_page_specified_in_data(self, driver, URL, element):
        """Check search footer elements in DATA_2 are displayed on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        search_terms_link = page.check_search_terms_link_is_visible()
        assert search_terms_link is True, "The element is not visible"
