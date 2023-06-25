"""This section contains the basic steps for running footer tests"""

import allure
from locators.footer_page_locators import FooterPageLocators
from pages.base_page import BasePage


@allure.epic("Footer Page")
class FooterPage(BasePage):
    footer_locators = FooterPageLocators()

    @allure.step("Check Footer is present in the DOM tree")
    def check_footer_is_present(self):
        """Checks Footer is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.FOOTER_SECTION)

    @allure.step("Check Footer is visible on the page")
    def check_footer_is_visible(self):
        """Checks Footer is visible on the page"""
        return self.element_is_visible(self.footer_locators.FOOTER_SECTION)

    @allure.step("Check Search Terms link is visible on the page")
    # def check_search_terms_link_is_visible(self, expected_link):
    def check_search_terms_link_is_visible(self):
        """Checks Search Terms link is visible on the page"""
        return self.element_is_visible(self.footer_locators.SEARCH_TERMS_LINK)
