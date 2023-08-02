"""This section contains footer tests"""
import allure
import pytest
from selenium.webdriver.common.by import By
from data.data_urls import MAIN_PAGE_URL, DATA_1, FooterLinks
from pages.footer_page import FooterPage
from data.footer_data import FooterElementsText


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

    @pytest.mark.xfail(reason="In CI the test is not stable and needs to be improved")
    @allure.title("TC 02.01.06 Check if Search Terms link is interactive")
    def test_tc_02_01_06_check_interactivity_of_search_terms_link(self, driver):
        """This test checks if Search Terms link is underlined while hovering over it"""
        page = FooterPage(driver, MAIN_PAGE_URL)
        page.open()
        underlined_link = page.check_element_hover_style(page.footer_locators.SEARCH_TERMS_LINK, "text-decoration", 2)
        assert "underline" in underlined_link, "The Search Terms link is not underlined while hovering over it"

    @allure.title("TC 02.01.07 - Check text of Search Terms link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_07_check_text_of_search_terms_link_on_pages(self, driver, URL):
        """Checks if text of Search Terms link is correct on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        actual_text = page.check_text_of_search_terms_link()
        expected_text = FooterElementsText.SEARCH_TERMS_LINK_TEXT
        assert actual_text == expected_text, \
            f"Actual text '{actual_text}' of Search Terms link does not match expected '{expected_text}'"

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

    @allure.title("TC 02.01.12 - Check text of Privacy and Cookie Policy link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_12_check_text_of_privacy_and_cookie_policy_link_on_pages(self, driver, URL):
        """Checks if text of Privacy and Cookie Policy link matches expected on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        actual_text = page.check_text_of_privacy_and_cookie_policy_link()
        expected_text = FooterElementsText.PRIVACY_AND_COOKIE_POLICY_LINK_TEXT
        assert actual_text == expected_text, \
            f"Actual text '{actual_text}' of Privacy and Cookie Policy link does not match expected '{expected_text}'"

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

    @allure.title("TC 02.01.17 - Check text of Advanced Search link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_17_check_text_of_advanced_search_link_on_pages(self, driver, URL):
        """Checks if text of Advanced Search link is correct on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        actual_text = page.check_text_of_advanced_search_link()
        expected_text = FooterElementsText.ADVANCED_SEARCH_LINK_TEXT
        assert actual_text == expected_text, \
            f"Actual text '{actual_text}' of Advanced Search link does not match expected '{expected_text}'"

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

    @allure.title("TC 02.01.22 - Check text of Orders and Returns link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_22_check_text_of_orders_and_returns_link_on_pages(self, driver, URL):
        """Checks if text of Orders and Returns link is correct on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        actual_text = page.check_text_of_orders_and_returns_link()
        expected_text = FooterElementsText.ORDERS_AND_RETURNS_LINK_TEXT
        assert actual_text == expected_text, \
            f"Actual text '{actual_text}' of Orders and Returns link does not match expected '{expected_text}'"

    @allure.title("TC 02.01.23 - Check 'Contact us' link is present in the DOM tree on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_23_check_presence_of_contact_us_link_on_pages(self, driver, URL):
        """Checks if 'Contact us' link is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        contact_us_link = page.check_contact_us_link_presence()
        assert contact_us_link, "The 'Contact us' link is not present in the DOM tree"

    @allure.title("TC 02.01.24 - Check display of 'Contact us' link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_24_check_visibility_of_contact_us_link_on_pages(self, driver, URL):
        """Checks if 'Contact us' link is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        contact_us_link = page.check_contact_us_link_is_visible()
        assert contact_us_link, "The 'Contact us' link is not visible"

    @allure.title("TC 02.01.25 - Check if 'Contact us' link is clickable on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_25_check_clickability_of_contact_us_link_on_pages(self, driver, URL):
        """This test checks if 'Contact us' link is clickable on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        contact_us_link = page.check_contact_us_link_clickability()
        assert contact_us_link, "The 'Contact us' link is not clickable"

    @allure.title("TC 02.01.27 - Check text of 'Contact us' link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_27_check_text_of_contact_us_link_on_pages(self, driver, URL):
        """Checks if text of 'Contact us' link is correct on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        actual_text = page.check_text_of_contact_us_link()
        expected_text = FooterElementsText.CONTACT_US_LINK_TEXT
        assert actual_text == expected_text, \
            f"Actual text '{actual_text}' of 'Contact us' link does not match expected '{expected_text}'"

    @allure.title("TC 02.01.28 - Check Write for us link is present in the DOM tree on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_28_check_presence_of_write_for_us_link_on_pages(self, driver, URL):
        """Checks if Write for us link is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        write_for_us_link = page.check_write_for_us_link_presence()
        assert write_for_us_link, "The Write for us link is not present in the DOM tree"

    @allure.title("TC 02.01.29 - Check display of Write for us link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_29_check_visibility_of_write_for_us_link_on_pages(self, driver, URL):
        """Checks if Write for us link is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        write_for_us_link = page.check_write_for_us_link_is_visible()
        assert write_for_us_link, "The Write for us link is not visible"

    @allure.title("TC 02.01.30 - Check if Write for us link is clickable on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_30_check_clickability_of_write_for_us_link_on_pages(self, driver, URL):
        """This test checks if Write for us link is clickable on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        write_for_us_link = page.check_write_for_us_link_clickability()
        assert write_for_us_link, "The Write for us link is not clickable"

    @allure.title("TC 02.01.32 - Check text of Write for us link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_32_check_text_of_write_for_us_link_on_pages(self, driver, URL):
        """Checks if text of Write for us link is correct on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        actual_text = page.check_text_of_write_for_us_link()
        expected_text = FooterElementsText.WRITE_FOR_US_LINK_TEXT
        assert actual_text == expected_text, \
            f"Actual text '{actual_text}' of Write for us link does not match expected '{expected_text}'"

    @allure.title("TC 02.01.33 - Check Copyright section is present in the DOM tree on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_33_check_presence_of_copyright_section_on_pages(self, driver, URL):
        """Checks if Copyright section is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        copyright_section = page.check_copyright_section_presence()
        assert copyright_section, "The Copyright section is not present in the DOM tree"

    @allure.title("TC 02.01.34 - Check display of Copyright section on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_34_check_visibility_of_copyright_section_on_pages(self, driver, URL):
        """Checks if Copyright section is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        copyright_section = page.check_copyright_section_is_visible()
        assert copyright_section, "The Copyright section is not visible"

    @allure.title("TC 02.01.35 - Check Copyright text is present in the DOM tree on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_35_check_presence_of_copyright_text_on_pages(self, driver, URL):
        """Checks if Copyright text is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        copyright_span = page.check_copyright_text_presence()
        assert copyright_span, "The Copyright text is not present in the DOM tree"

    @allure.title("TC 02.01.36 - Check display of Copyright text on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_36_check_visibility_of_copyright_text_on_pages(self, driver, URL):
        """Checks if Copyright text is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        copyright_span = page.check_text_of_copyright_section_is_visible()
        assert copyright_span, "The Copyright text is not visible"

    @allure.title("TC 02.01.37 - Check text of Copyright section on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_37_check_text_of_copyright_section_on_pages(self, driver, URL):
        """Checks if text of Copyright section is correct on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        actual_text = page.check_text_of_copyright_section()
        expected_text = FooterElementsText.COPYRIGHT_TEXT
        assert actual_text == expected_text, \
            f"Actual text '{actual_text}' of Copyright section does not match expected '{expected_text}'"

    @pytest.mark.skip(reason="Subscribe section has been replaced by 'Subscribe to our mailing list' link")
    @allure.title("TC 02.01.38 - Check Subscribe section is present in the DOM tree on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_38_check_presence_of_subscribe_section_on_pages(self, driver, URL):
        """Checks if Subscribe section is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_section = page.check_subscribe_section_presence()
        assert subscribe_section, "The Subscribe section is not present in the DOM tree"

    @pytest.mark.skip(reason="Subscribe section has been replaced by 'Subscribe to our mailing list' link")
    @allure.title("TC 02.01.39 - Check display of Subscribe section on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_39_check_visibility_of_subscribe_section_on_pages(self, driver, URL):
        """Checks if Subscribe section is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_section = page.check_subscribe_section_is_visible()
        assert subscribe_section, "The Subscribe section is not visible"

    @pytest.mark.skip(reason="Subscribe section has been replaced by 'Subscribe to our mailing list' link")
    @allure.title("TC 02.01.40 - Check Subscribe Button is present in the DOM tree on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_40_check_presence_of_subscribe_button_on_pages(self, driver, URL):
        """Checks if Subscribe Button is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_button = page.check_subscribe_button_presence()
        assert subscribe_button, "The Subscribe Button is not present in the DOM tree"

    @pytest.mark.skip(reason="Subscribe section has been replaced by 'Subscribe to our mailing list' link")
    @allure.title("TC 02.01.41 - Check display of Subscribe Button on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_41_check_visibility_of_subscribe_button_on_pages(self, driver, URL):
        """Checks if Subscribe Button is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_button = page.check_subscribe_button_is_visible()
        assert subscribe_button, "The Subscribe Button is not visible"

    @pytest.mark.skip(reason="Subscribe section has been replaced by 'Subscribe to our mailing list' link")
    @allure.title("TC 02.01.42 - Check if Subscribe Button is clickable on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_42_check_clickability_of_subscribe_button_on_pages(self, driver, URL):
        """This test checks if Subscribe Button is clickable on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_button = page.check_subscribe_button_clickability()
        assert subscribe_button, "The Subscribe Button is not clickable"

    @pytest.mark.skip(reason="Subscribe section has been replaced by 'Subscribe to our mailing list' link")
    @allure.title("TC 02.01.44 - Check text on Subscribe Button is present in the DOM tree "
                  "on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_44_check_presence_of_subscribe_button_text_on_pages(self, driver, URL):
        """Checks if text on Subscribe Button is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_button_text = page.check_subscribe_button_text_presence()
        assert subscribe_button_text, "Text on Subscribe Button is not present in the DOM tree"

    @pytest.mark.skip(reason="Subscribe section has been replaced by 'Subscribe to our mailing list' link")
    @allure.title("TC 02.01.45 - Check display of text on Subscribe Button on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_45_check_visibility_of_subscribe_button_text_on_pages(self, driver, URL):
        """Checks if text on Subscribe Button is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_button_text = page.check_subscribe_button_text_is_visible()
        assert subscribe_button_text, "The text on Subscribe Button is not visible"

    @pytest.mark.skip(reason="Subscribe section has been replaced by 'Subscribe to our mailing list' link")
    @allure.title("TC 02.01.46 - Check text on Subscribe Button on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_46_check_text_on_subscribe_button_on_pages(self, driver, URL):
        """Checks if text on Subscribe Button is correct on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        actual_text = page.check_text_on_subscribe_button()
        expected_text = FooterElementsText.SUBSCRIBE_BUTTON_TEXT
        assert actual_text == expected_text, \
            f"Actual text '{actual_text}' on Subscribe Button does not match expected '{expected_text}'"

    @pytest.mark.skip(reason="Subscribe section has been replaced by 'Subscribe to our mailing list' link")
    @allure.title("TC 02.01.47 - Check Email field in Subscribe section is present in the DOM tree "
                  "on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_47_check_presence_of_subscribe_email_field_on_pages(self, driver, URL):
        """Checks if Email field in Subscribe section is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_email_field = page.check_subscribe_email_field_presence()
        assert subscribe_email_field, "Email field in Subscribe section is not present in the DOM tree"

    @pytest.mark.skip(reason="Subscribe section has been replaced by 'Subscribe to our mailing list' link")
    @allure.title("TC 02.01.48 - Check display of Subscribe Email Field on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_48_check_visibility_of_subscribe_email_field_on_pages(self, driver, URL):
        """Checks if Subscribe Email Field is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_email_field = page.check_subscribe_email_field_is_visible()
        assert subscribe_email_field, "The Subscribe Email Field is not visible"

    @pytest.mark.skip(reason="Subscribe section has been replaced by 'Subscribe to our mailing list' link")
    @allure.title("TC 02.01.49 - Check placeholder in Subscribe Email Field is present in the DOM tree "
                  "on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_49_check_presence_of_placeholder_in_subscribe_email_field_on_pages(self, driver, URL):
        """Checks if placeholder in Email field is present in the DOM tree on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_email_field_placeholder = page.check_placeholder_presence_in_subscribe_email_field()
        assert subscribe_email_field_placeholder, "Placeholder in Email field is not present in the DOM tree"

    @pytest.mark.skip(reason="Subscribe section has been replaced by 'Subscribe to our mailing list' link")
    @allure.title(
        "TC 02.01.50 - Check display of placeholder in Subscribe Email Field on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_50_check_visibility_of_placeholder_in_subscribe_email_field_on_pages(self, driver, URL):
        """Checks if placeholder in Subscribe Email Field is visible on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_email_field_placeholder = page.check_placeholder_in_subscribe_email_field_is_visible()
        assert subscribe_email_field_placeholder, "The placeholder in Subscribe Email Field is not visible"

    @pytest.mark.skip(reason="Subscribe section has been replaced by 'Subscribe to our mailing list' link")
    @allure.title("TC 02.01.51 - Check text of placeholder in Subscribe Email Field on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_51_check_text_of_placeholder_in_subscribe_email_field_on_pages(self, driver, URL):
        """Checks if text of placeholder in Subscribe Email Field is correct on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        actual_text = page.check_text_of_subscribe_email_field_placeholder()
        expected_text = FooterElementsText.SUBSCRIBE_EMAIL_FIELD_PLACEHOLDER_TEXT
        assert actual_text == expected_text, \
            f"Actual text '{actual_text}' of placeholder in Subscribe Email Field " \
            f"does not match expected '{expected_text}'"

    @allure.title("TC 02.01.52 - Check 'Subscribe to our mailing list' link is present "
                  "in the DOM tree on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_52_check_presence_of_subscribe_to_our_mailing_list_link_on_pages(self, driver, URL):
        """Checks if 'Subscribe to our mailing list' link is present in the DOM tree on each page
        specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_link = page.check_subscribe_to_our_mailing_list_link_presence()
        assert subscribe_link, "The 'Subscribe to our mailing list' link is not present in the DOM tree"

    @allure.title("TC 02.01.53 - Check 'Subscribe to our mailing list' link is visible "
                  "on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_53_check_display_of_subscribe_to_our_mailing_list_link_on_pages(self, driver, URL):
        """Checks if 'Subscribe to our mailing list' link is visible on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_link = page.check_subscribe_to_our_mailing_list_link_is_visible()
        assert subscribe_link, "The 'Subscribe to our mailing list' link is not visible in the DOM tree"

    @allure.title("TC 02.01.54 - Check if 'Subscribe to our mailing list' link is clickable "
                  "on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_54_check_clickability_of_subscribe_to_our_mailing_list_link_on_pages(self, driver, URL):
        """This test checks if 'Subscribe to our mailing list' link is clickable on each page specified in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        subscribe_link = page.check_subscribe_to_our_mailing_list_link_clickability()
        assert subscribe_link, "The 'Subscribe to our mailing list' link is not clickable"

    @allure.title("TC 02.01.56 - Check text of 'Subscribe to our mailing list' link on each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_01_56_check_text_of_subscribe_to_our_mailing_list_link_on_pages(self, driver, URL):
        """Checks if text of 'Subscribe to our mailing list' link is correct on each page in DATA_1"""
        page = FooterPage(driver, url=URL)
        page.open()
        actual_text = page.check_text_of_subscribe_to_our_mailing_list_link()
        expected_text = FooterElementsText.SUBSCRIBE_TO_OUR_MAILING_LIST_TEXT
        assert actual_text == expected_text, \
            f"Actual text '{actual_text}' of 'Subscribe to our mailing list' link does not match expected '{expected_text}'"

    @allure.title("TC 02.02.01 - Check Search Terms link in footer leads to the correct page "
                  "from each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_02_01_check_search_terms_link_functionality(self, driver, URL):
        """Check that Search Terms link in footer is correct"""
        page = FooterPage(driver, url=URL)
        page.open()
        page.check_search_terms_link_functionality()
        title = page.check_title_display_of_popular_search_terms_page()
        assert page.get_actual_url_of_current_page() == FooterLinks.POPULAR_SEARCH_TERMS_URL \
               and title == "Popular Search Terms", "The Search Terms link is not correct or the new page is not loaded"

    @allure.title("TC 02.02.02 - Check Privacy and Cookie Policy link in footer leads to the correct page "
                  "from each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_02_02_check_privacy_and_cookie_policy_link_functionality(self, driver, URL):
        """Check that Privacy and Cookie Policy link in footer is correct"""
        page = FooterPage(driver, url=URL)
        page.open()
        page.check_privacy_and_cookie_policy_link_functionality()
        title = page.check_title_display_of_privacy_policy_page()
        assert page.get_actual_url_of_current_page() == FooterLinks.PRIVACY_AND_COOKIE_POLICY_URL \
               and title == "Privacy Policy", "The Privacy and Cookie Policy link is not correct or the new page is " \
                                              "not loaded"

    @allure.title("TC 02.02.03 - Check Advanced Search link in footer leads to the correct page "
                  "from each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_02_03_check_advanced_search_link_functionality(self, driver, URL):
        """Check that Advanced Search link in footer is correct"""
        page = FooterPage(driver, url=URL)
        page.open()
        page.check_advanced_search_link_functionality()
        title = page.check_title_display_of_advanced_search_page()
        assert page.get_actual_url_of_current_page() == FooterLinks.ADVANCED_SEARCH_URL \
               and title == "Advanced Search", "The Advanced Search link is not correct or the new page is not loaded"

    @allure.title("TC 02.02.04 - Check Orders and Returns link in footer leads to the correct page "
                  "from each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_02_04_check_orders_and_returns_link_functionality(self, driver, URL):
        """Check that Orders and Returns link in footer is correct"""
        page = FooterPage(driver, url=URL)
        page.open()
        page.check_orders_and_returns_link_functionality()
        title = page.check_title_display_of_orders_and_returns_page()
        assert page.get_actual_url_of_current_page() == FooterLinks.ORDERS_AND_RETURNS_URL \
               and title == "Orders and Returns", "The Orders and Returns link is not correct " \
                                                  "or the new page is not loaded"

    @allure.title("TC 02.02.05 - Check Contact Us link in footer leads to the correct page "
                  "from each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_02_05_check_contact_us_link_functionality(self, driver, URL):
        """Check that Contact Us link in footer is correct"""
        page = FooterPage(driver, url=URL)
        page.open()
        page.check_contact_us_link_functionality()
        title = page.check_title_display_of_contact_page()
        assert page.get_actual_url_of_current_page() == FooterLinks.CONTACT_URL \
               and title == "Contact", "The Contact Us link is not correct or the new page is not loaded"

    @allure.title("TC 02.02.06 - Check Write for us link in footer leads to the correct page "
                  "from each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_02_06_check_write_for_us_link_functionality(self, driver, URL):
        """Check that Write for us link in footer is correct"""
        page = FooterPage(driver, url=URL)
        page.open()
        page.check_write_for_us_link_functionality()
        title = page.check_item_display_of_write_for_us_page()
        assert page.get_actual_url_of_current_page() == FooterLinks.WRITE_FOR_US_URL \
               and title == "Write For Us", "The Write for us link is not correct or the new page is not loaded"

    @allure.title("TC 02.02.07 - Check 'Subscribe to our mailing list' link in footer leads to the correct page "
                  "from each page specified in DATA_1")
    @pytest.mark.parametrize('URL', DATA_1)
    def test_tc_02_02_07_check_subscribe_to_our_mailing_list_link_functionality(self, driver, URL):
        """Check that 'Subscribe to our mailing list' link in footer is correct"""
        page = FooterPage(driver, url=URL)
        page.open()
        page.check_subscribe_to_our_mailing_list_link_functionality()
        title = page.check_title_display_of_subscribe_page()
        assert page.get_actual_url_of_current_page() == FooterLinks.SUBSCRIBE_TO_OUR_MAILING_LIST_URL \
               and title == "Subscribe", "The 'Subscribe to our mailing list' link is not correct " \
                                         "or the new page is not loaded"

