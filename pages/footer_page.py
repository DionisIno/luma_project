"""This section contains the basic steps for running footer tests"""

import allure
from locators.footer_page_locators import FooterPageLocators
from locators.popular_search_terms_page_locators import PopularSearchTermsPageLocators
from locators.privacy_policy_page_locators import PrivacyPolicyPageLocators
from locators.advanced_search_page_locators import AdvancedSearchPageLocators
from locators.orders_and_returns_page_locators import OrdersAndReturnsPageLocators
from locators.contact_us_page_locators import ContactUsPageLocators
from locators.outside_pages_locators import WriteForUsPageLocators
from pages.base_page import BasePage


@allure.epic("Footer Page")
class FooterPage(BasePage):
    footer_locators = FooterPageLocators()
    locators1 = PopularSearchTermsPageLocators()
    locators2 = PrivacyPolicyPageLocators()
    locators3 = AdvancedSearchPageLocators()
    locators4 = OrdersAndReturnsPageLocators()
    locators5 = ContactUsPageLocators()
    locators6 = WriteForUsPageLocators()

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

    @allure.step("Check Contact Us link is present in the DOM tree")
    def check_subscribe_to_our_mailing_list_link_presence(self):
        """Checks Contact Us link is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.SUBSCRIBE_TO_OUR_MAILING_LIST_LINK)

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

    @allure.step("Check Subscribe Button is present in the DOM tree")
    def check_subscribe_button_presence(self):
        """Checks Subscribe Button is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.SUBSCRIBE_BUTTON)

    @allure.step("Check text on Subscribe Button is present in the DOM tree")
    def check_subscribe_button_text_presence(self):
        """Checks text on Subscribe Button is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.SUBSCRIBE_BUTTON_TEXT)

    @allure.step("Check text Email field in Subscribe section is present in the DOM tree")
    def check_subscribe_email_field_presence(self):
        """Checks Email field in Subscribe section is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.SUBSCRIBE_EMAIL_FIELD)

    @allure.step("Check text Email field in Subscribe section is present in the DOM tree")
    def check_placeholder_presence_in_subscribe_email_field(self):
        """Checks placeholder in Email field in Subscribe section is present in the DOM tree"""
        return self.element_is_present(self.footer_locators.SUBSCRIBE_EMAIL_FIELD).get_attribute('placeholder')

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

    @allure.step("Check Subscribe section is visible on the page")
    def check_subscribe_section_is_visible(self):
        """Checks Subscribe section is visible"""
        return self.element_is_visible(self.footer_locators.SUBSCRIBE_SECTION)

    @allure.step("Check Subscribe Button is visible on the page")
    def check_subscribe_button_is_visible(self):
        """Checks Subscribe Button is visible"""
        return self.element_is_visible(self.footer_locators.SUBSCRIBE_BUTTON)

    @allure.step("Check text on Subscribe Button is visible on the page")
    def check_subscribe_button_text_is_visible(self):
        """Checks text on Subscribe Button is visible"""
        return self.element_is_visible(self.footer_locators.SUBSCRIBE_BUTTON_TEXT)

    @allure.step("Check Subscribe Email Field is visible on the page")
    def check_subscribe_email_field_is_visible(self):
        """Checks Subscribe Email Field is visible"""
        return self.element_is_visible(self.footer_locators.SUBSCRIBE_EMAIL_FIELD)

    @allure.step("Check placeholder in Subscribe Email Field is visible on the page")
    def check_placeholder_in_subscribe_email_field_is_visible(self):
        """Checks placeholder in Subscribe Email Field is visible"""
        return self.element_is_visible(self.footer_locators.SUBSCRIBE_EMAIL_FIELD).get_attribute('placeholder')

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

    @allure.step("Check Subscribe Button is clickable")
    def check_subscribe_button_clickability(self):
        """Checks Subscribe Button clickability"""
        return self.element_is_clickable(self.footer_locators.SUBSCRIBE_BUTTON)

    @allure.step("Check the text of Search Terms link")
    def check_text_of_search_terms_link(self):
        """Checks content of Search Terms link"""
        link_text = self.driver.find_element(*self.footer_locators.SEARCH_TERMS_LINK).text
        return link_text

    @allure.step("Check the text of Privacy and Cookie Policy link")
    def check_text_of_privacy_and_cookie_policy_link(self):
        """Checks content of Privacy and Cookie Policy link"""
        link_text = self.driver.find_element(*self.footer_locators.PRIVACY_AND_COOKIE_POLICY_LINK).text
        return link_text

    @allure.step("Check the text of Advanced Search link")
    def check_text_of_advanced_search_link(self):
        """Checks content of Advanced Search link"""
        link_text = self.driver.find_element(*self.footer_locators.ADVANCED_SEARCH_LINK).text
        return link_text

    @allure.step("Check the text of Orders and Returns link")
    def check_text_of_orders_and_returns_link(self):
        """Checks content of Orders and Returns link"""
        link_text = self.driver.find_element(*self.footer_locators.ORDERS_AND_RETURNS_LINK).text
        return link_text

    @allure.step("Check the text of Contact Us link")
    def check_text_of_contact_us_link(self):
        """Checks content of Contact Us link"""
        link_text = self.driver.find_element(*self.footer_locators.CONTACT_US_LINK).text
        return link_text

    @allure.step("Check the text of Write for us link")
    def check_text_of_write_for_us_link(self):
        """Checks content of Write for us link"""
        link_text = self.driver.find_element(*self.footer_locators.WRITE_FOR_US_LINK).text
        return link_text

    @allure.step("Check the text of Copyright section")
    def check_text_of_copyright_section(self):
        """Checks content of Copyright section"""
        copyright_text = self.driver.find_element(*self.footer_locators.COPYRIGHT_SECTION).text
        return copyright_text

    @allure.step("Check the text on Subscribe Button")
    def check_text_on_subscribe_button(self):
        """Checks content of text on Subscribe Button"""
        button_text = self.driver.find_element(*self.footer_locators.SUBSCRIBE_BUTTON_TEXT).text
        return button_text

    @allure.step("Check the text of placeholder in Subscribe Email Field")
    def check_text_of_subscribe_email_field_placeholder(self):
        """Checks content of text of placeholder in Subscribe Email Field"""
        placeholder_text = self.driver.find_element(*self.footer_locators.SUBSCRIBE_EMAIL_FIELD).get_attribute('placeholder')
        return placeholder_text

    @allure.step("Check Search Terms link leads to the correct page")
    def check_search_terms_link_functionality(self):
        """Checks that Search Terms link leads to the correct page"""
        search_terms_link = self.element_is_visible(self.footer_locators.SEARCH_TERMS_LINK)
        link_functionality = search_terms_link.click()
        return link_functionality

    @allure.step("Check the title of opened page Popular Search Terms is displayed")
    def check_title_display_of_popular_search_terms_page(self):
        """Checks that the title of opened page Popular Search Terms is displayed"""
        return self.get_text(self.locators1.POPULAR_SEARCH_TERMS_TITLE)

    @allure.step("Check Privacy and Cookie Policy link leads to the correct page")
    def check_privacy_and_cookie_policy_link_functionality(self):
        """Checks that Privacy and Cookie Policy link leads to the correct page"""
        privacy_and_cookie_policy_link = self.element_is_visible(self.footer_locators.PRIVACY_AND_COOKIE_POLICY_LINK)
        link_functionality = privacy_and_cookie_policy_link.click()
        return link_functionality

    @allure.step("Check the title of opened page Privacy Policy is displayed")
    def check_title_display_of_privacy_policy_page(self):
        """Checks that the title of opened page Privacy Policy is displayed"""
        return self.get_text(self.locators2.PRIVACY_POLICY_TITLE)

    @allure.step("Check Advanced Search link leads to the correct page")
    def check_advanced_search_link_functionality(self):
        """Checks that Advanced Search link leads to the correct page"""
        advanced_search_link = self.element_is_visible(self.footer_locators.ADVANCED_SEARCH_LINK)
        link_functionality = advanced_search_link.click()
        return link_functionality

    @allure.step("Check the title of opened page Advanced Search is displayed")
    def check_title_display_of_advanced_search_page(self):
        """Checks that the title of opened page Advanced Search is displayed"""
        return self.get_text(self.locators3.ADVANCED_SEARCH_TITLE)

    @allure.step("Check Orders and Returns link leads to the correct page")
    def check_orders_and_returns_link_functionality(self):
        """Checks that Orders and Returns link leads to the correct page"""
        orders_and_returns_link = self.element_is_visible(self.footer_locators.ORDERS_AND_RETURNS_LINK)
        link_functionality = orders_and_returns_link.click()
        return link_functionality

    @allure.step("Check the title of opened page Orders and Returns is displayed")
    def check_title_display_of_orders_and_returns_page(self):
        """Checks that the title of opened page Orders and Returns is displayed"""
        return self.get_text(self.locators4.ORDERS_AND_RETURNS_TITLE)

    @allure.step("Check Contact Us link leads to the correct page")
    def check_contact_us_link_functionality(self):
        """Checks that Contact Us link leads to the correct page"""
        contact_us_link = self.element_is_visible(self.footer_locators.CONTACT_US_LINK)
        link_functionality = contact_us_link.click()
        return link_functionality

    @allure.step("Check the title of opened page Contact is displayed")
    def check_title_display_of_contact_page(self):
        """Checks that the title of opened page Contact is displayed"""
        return self.get_text(self.locators5.CONTACT_TITLE)

    @allure.step("Check Write for us link leads to the correct page")
    def check_write_for_us_link_functionality(self):
        """Checks that Write for us leads to the correct page"""
        return self.element_is_visible(self.footer_locators.WRITE_FOR_US_LINK).click()

    @allure.step("Check the item in menu of opened page Write For Us is displayed")
    def check_item_display_of_write_for_us_page(self):
        """Checks that the item in menu of opened page Write For Us is displayed"""
        return self.get_text(self.locators6.WRITE_FOR_US_MENU_ITEM)

