"""This section contains the basic steps for running footer tests"""

import allure
from locators.footer_page_locators import FooterPageLocators
from pages.base_page import BasePage


@allure.epic("Footer Page")
class FooterPage(BasePage):
    footer_locators = FooterPageLocators()

    @allure.step("Check Footer is present in the DOM tree")
    def check_footer_presence(self):
        """Checks Footer is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.FOOTER_SECTION)

    @allure.step("Check Search Terms link is present in the DOM tree")
    def check_search_terms_link_presence(self):
        """Checks Search Terms link is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.SEARCH_TERMS_LINK)

    @allure.step("Check Privacy and Cookie Policy link is present in the DOM tree")
    def check_privacy_and_cookie_policy_link_presence(self):
        """Checks Privacy and Cookie Policy link is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.PRIVACY_AND_COOKIE_POLICY_LINK)

    @allure.step("Check Advanced Search link is present in the DOM tree")
    def check_advanced_search_link_presence(self):
        """Checks Advanced Search link is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.ADVANCED_SEARCH_LINK)

    @allure.step("Check Orders and Returns link is present in the DOM tree")
    def check_orders_and_returns_link_presence(self):
        """Checks Orders and Returns link is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.ORDERS_AND_RETURNS_LINK)

    @allure.step("Check Contact Us link is present in the DOM tree")
    def check_contact_us_link_presence(self):
        """Checks Contact Us link is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.CONTACT_US_LINK)

    @allure.step("Check Write for us link is present in the DOM tree")
    def check_write_for_us_link_presence(self):
        """Checks Write for us link is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.WRITE_FOR_US_LINK)

    @allure.step("Check Copyright section is present in the DOM tree")
    def check_copyright_section_presence(self):
        """Checks Copyright section is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.COPYRIGHT_SECTION)

    @allure.step("Check Copyright text is present in the DOM tree")
    def check_copyright_text_presence(self):
        """Checks Copyright text is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.COPYRIGHT_TEXT)

    @allure.step("Check Subscribe section is present in the DOM tree")
    def check_subscribe_section_presence(self):
        """Checks Subscribe section is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.SUBSCRIBE_SECTION)

    @allure.step("Check Footer is visible on the page")
    def check_footer_is_visible(self):
        """Checks Footer is visible"""
        return self.element_is_visible(self.footer_locators.FOOTER_SECTION)

    @allure.step("Check Search Terms link is visible on the page")
    # def check_search_terms_link_is_visible(self, expected_link):
    def check_search_terms_link_is_visible(self):
        """Checks Search Terms link is visible"""
        return self.element_is_visible(self.footer_locators.SEARCH_TERMS_LINK)

    @allure.step("Check Privacy and Cookie Policy link is visible on the page")
    def check_privacy_and_cookie_policy_link_is_visible(self):
        """Checks Privacy and Cookie Policy link is visible"""
        return self.element_is_visible(self.footer_locators.PRIVACY_AND_COOKIE_POLICY_LINK)

    @allure.step("Check Advanced Search link is visible on the page")
    def check_advanced_search_link_is_visible(self):
        """Checks Advanced Search link is visible"""
        return self.element_is_visible(self.footer_locators.ADVANCED_SEARCH_LINK)

    @allure.step("Check Orders and Returns link is visible on the page")
    def check_orders_and_returns_link_is_visible(self):
        """Checks Orders and Returns link is visible"""
        return self.element_is_visible(self.footer_locators.ORDERS_AND_RETURNS_LINK)

    @allure.step("Check Contact Us link is visible on the page")
    def check_contact_us_link_is_visible(self):
        """Checks Contact Us link is visible"""
        return self.element_is_visible(self.footer_locators.CONTACT_US_LINK)

    @allure.step("Check Write for us link is visible on the page")
    def check_write_for_us_link_is_visible(self):
        """Checks Write for us link is visible"""
        return self.element_is_visible(self.footer_locators.WRITE_FOR_US_LINK)

    @allure.step("Check Copyright section is visible on the page")
    def check_copyright_section_is_visible(self):
        """Checks Copyright section is visible"""
        return self.element_is_visible(self.footer_locators.COPYRIGHT_SECTION)

    @allure.step("Check text of Copyright section is visible on the page")
    def check_text_of_copyright_section_is_visible(self):
        """Checks text of Copyright section is visible"""
        return self.element_is_visible(self.footer_locators.COPYRIGHT_TEXT)

    @allure.step("Check Search Terms link is clickable")
    def check_search_terms_link_clickability(self):
        """Checks Search Terms link clickability"""
        return self.element_is_clickable(self.footer_locators.SEARCH_TERMS_LINK)

    @allure.step("Check Privacy and Cookie Policy link is clickable")
    def check_privacy_and_cookie_policy_link_clickability(self):
        """Checks Privacy and Cookie Policy link clickability"""
        return self.element_is_clickable(self.footer_locators.PRIVACY_AND_COOKIE_POLICY_LINK)

    @allure.step("Check Advanced Search link is clickable")
    def check_advanced_search_link_clickability(self):
        """Checks Advanced Search link clickability"""
        return self.element_is_clickable(self.footer_locators.ADVANCED_SEARCH_LINK)

    @allure.step("Check Orders and Returns link is clickable")
    def check_orders_and_returns_link_clickability(self):
        """Checks Orders and Returns link clickability"""
        return self.element_is_clickable(self.footer_locators.ORDERS_AND_RETURNS_LINK)

    @allure.step("Check Contact Us link is clickable")
    def check_contact_us_link_clickability(self):
        """Checks Contact Us link clickability"""
        return self.element_is_clickable(self.footer_locators.CONTACT_US_LINK)

    @allure.step("Check Write for us link is clickable")
    def check_write_for_us_link_clickability(self):
        """Checks Write for us link clickability"""
        return self.element_is_clickable(self.footer_locators.WRITE_FOR_US_LINK)
