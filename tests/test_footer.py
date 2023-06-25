"""This section contains footer tests"""
import allure
import pytest
from selenium.webdriver.common.by import By
from data.data_urls import MAIN_PAGE_URL, DATA_1
from pages.footer_page import FooterPage


@allure.epic("Test Footer")
class TestFooter:

    @allure.title("TC 02.01.01 - Check Footer is present in the DOM tree on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_01_check_footer_is_present_on_each_page_specified_in_data(self, driver, URL):
        """Check if the footer is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        footer_section = page.check_footer_is_present()
        assert footer_section, "Footer is not present in the DOM tree"

    @allure.title("TC 02.01.02 - Check Footer display on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_02_check_footer_visibility_on_each_page_specified_in_data(self, driver, URL):
        """Check if Footer is visible on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        footer_section = page.check_footer_is_visible()
        assert footer_section, "Footer is not visible"

    @allure.title("TC 02.01.05 - Check display of Search Terms link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_05_check_the_search_terms_link_visibility_on_each_page_specified_in_data(self, driver, URL):
        """Check search terms link is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        link = page.check_search_terms_link_is_visible()
        search_terms_link_text = link.text
        assert search_terms_link_text == "Search Terms", "The link is not visible or correct"
