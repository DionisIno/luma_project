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
    def test_tc_02_01_01_check_presence_of_footer_on_pages(self, driver, URL):
        """Checks if the footer is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        footer_section = page.check_footer_presence()
        assert footer_section, "Footer is not present in the DOM tree"

    @allure.title("TC 02.01.02 - Check Footer display on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_02_check_visibility_of_footer_on_pages(self, driver, URL):
        """Checks if Footer is visible on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        footer_section = page.check_footer_is_visible()
        assert footer_section, "Footer is not visible"

    @allure.title("TC 02.01.03 - Check Search Terms link is present in the DOM tree on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_03_check_presence_of_search_terms_link_on_pages(self, driver, URL):
        """Checks if the Search Terms link is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        search_terms_link = page.check_search_terms_link_presence()
        assert search_terms_link, "The Search Terms link is not present in the DOM tree"

    @allure.title("TC 02.01.04 - Check display of Search Terms link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_04_check_visibility_of_search_terms_link_on_pages(self, driver, URL):
        """Checks if Search Terms link is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        search_terms_link = page.check_search_terms_link_is_visible()
        assert search_terms_link, "The Search Terms link is not visible"

    @allure.title("TC 02.01.05 - Check if Search Terms link is clickable on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_05_check_clickability_of_search_terms_link_on_pages(self, driver, URL):
        """This test checks if Search Terms link is clickable on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        search_terms_link = page.check_search_terms_link_clickability()
        assert search_terms_link, "The Search Terms link is not clickable"

    @allure.title("TC 02.01.07 - Check text of Search Terms link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_07_check_text_of_search_terms_link_on_pages(self, driver, URL):
        """Checks if text of Search Terms link is correct on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        link = page.check_search_terms_link_is_visible()
        link_text = link.text
        assert link_text == "Search Terms", "Text of Search Terms link is not correct"

    @allure.title("TC 02.01.08 - Check Privacy and Cookie Policy link is present in the DOM tree "
                  "on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_08_check_presence_of_privacy_and_cookie_policy_link_on_pages(self, driver, URL):
        """Checks if Privacy and Cookie Policy link is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        privacy_and_cookie_policy_link = page.check_privacy_and_cookie_policy_link_presence()
        assert privacy_and_cookie_policy_link, "The Privacy and Cookie Policy link is not present in the DOM tree"

    @allure.title("TC 02.01.09 - Check display of Privacy and Cookie Policy link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_09_check_visibility_of_privacy_and_cookie_policy_link_on_pages(self, driver, URL):
        """Checks if Privacy and Cookie Policy link is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        privacy_and_cookie_policy_link = page.check_privacy_and_cookie_policy_link_is_visible()
        assert privacy_and_cookie_policy_link, "The Privacy and Cookie Policy link is not visible"

    @allure.title("TC 02.01.10 - Check if Privacy and Cookie Policy link is clickable on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_10_check_clickability_of_privacy_and_cookie_policy_link_on_pages(self, driver, URL):
        """This test checks if Privacy and Cookie Policy link is clickable on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        privacy_and_cookie_policy_link = page.check_privacy_and_cookie_policy_link_clickability()
        assert privacy_and_cookie_policy_link, "The Privacy and Cookie Policy link is not clickable"

    @allure.title("TC 02.01.13 - Check Advanced Search link is present in the DOM tree "
                  "on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_13_check_presence_of_advanced_search_link_on_pages(self, driver, URL):
        """Checks if Advanced Search link is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        advanced_search_link = page.check_advanced_search_link_presence()
        assert advanced_search_link, "The Advanced Search link is not present in the DOM tree"

    @allure.title("TC 02.01.14 - Check display of Advanced Search link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_14_check_visibility_of_advanced_search_link_on_pages(self, driver, URL):
        """Checks if Advanced Search link is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        advanced_search_link = page.check_advanced_search_link_is_visible()
        assert advanced_search_link, "The Advanced Search link is not visible"

    @allure.title("TC 02.01.15 - Check if Advanced Search link is clickable on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_15_check_clickability_of_advanced_search_link_on_pages(self, driver, URL):
        """This test checks if Advanced Search link is clickable on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        advanced_search_link = page.check_advanced_search_link_clickability()
        assert advanced_search_link, "The Advanced Search link is not clickable"

    @allure.title("TC 02.01.18 - Check Orders and Returns link is present in the DOM tree "
                  "on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_18_check_presence_of_orders_and_returns_link_on_pages(self, driver, URL):
        """Checks if Orders and Returns link is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        orders_and_returns_link = page.check_orders_and_returns_link_presence()
        assert orders_and_returns_link, "The Orders and Returns link is not present in the DOM tree"

    @allure.title("TC 02.01.19 - Check display of Orders and Returns link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_19_check_visibility_of_orders_and_returns_link_on_pages(self, driver, URL):
        """Checks if Orders and Returns link is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        orders_and_returns_link = page.check_orders_and_returns_link_is_visible()
        assert orders_and_returns_link, "The Orders and Returns link is not visible"

    @allure.title("TC 02.01.20 - Check if Orders and Returns link is clickable on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_20_check_clickability_of_orders_and_returns_link_on_pages(self, driver, URL):
        """This test checks if Orders and Returns link is clickable on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        orders_and_returns_link = page.check_orders_and_returns_link_clickability()
        assert orders_and_returns_link, "The Orders and Returns link is not clickable"

    @allure.title("TC 02.01.23 - Check Contact Us link is present in the DOM tree on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_23_check_presence_of_contact_us_link_on_pages(self, driver, URL):
        """Checks if Contact Us link is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        contact_us_link = page.check_contact_us_link_presence()
        assert contact_us_link, "The Contact Us link is not present in the DOM tree"

    @allure.title("TC 02.01.25 - Check if Contact Us link is clickable on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_25_check_clickability_of_contact_us_link_on_pages(self, driver, URL):
        """This test checks if Contact Us link is clickable on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        contact_us_link = page.check_contact_us_link_clickability()
        assert contact_us_link, "The Contact Us link is not clickable"

    @allure.title("TC 02.01.28 - Check Write for us link is present in the DOM tree on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_28_check_presence_of_write_for_us_link_on_pages(self, driver, URL):
        """Checks if Write for us link is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        write_for_us_link = page.check_write_for_us_link_presence()
        assert write_for_us_link, "The Write for us link is not present in the DOM tree"

    @allure.title("TC 02.01.30 - Check if Write for us link is clickable on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_30_check_clickability_of_write_for_us_link_on_pages(self, driver, URL):
        """This test checks if Write for us link is clickable on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        write_for_us_link = page.check_write_for_us_link_clickability()
        assert write_for_us_link, "The Write for us link is not clickable"
