from locators.footer_page_locators import FooterPageLocators
from pages.base_page import BasePage


class FooterPage(BasePage):
    footer_locators = FooterPageLocators()

    def check_search_terms_link_is_visible(self):
        search_terms_link = self.element_is_visible(self.footer_locators.SEARCH_TERMS_LINK)
        return search_terms_link.is_displayed()

    def some_link_is_visible(self):
        search_terms_link = self.element_is_visible(self.footer_locators.DATA_2)
        return search_terms_link.is_displayed()
