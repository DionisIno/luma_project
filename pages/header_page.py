from data.data_urls import TRAINING_PAGE_URL, VIDEO_DOWNLOAD_PAGE_URL, WOMEN_PAGE_URL
from locators.header_page_locators import HeaderPageLocators
from locators.create_account_page_locators import CreateAccountPageLocators
from locators.sign_in_page_locators import SingInPageLocators
from pages.base_page import BasePage
from locators.training_page_locators import TrainingPageLocators
from locators.training_video_page_locators import TrainingVideoPageLocators
from locators.women_page_locators import WomenPageLocators


class HeaderPage(BasePage):
    header_locators = HeaderPageLocators
    create_account_locators = CreateAccountPageLocators
    sign_in_locators = SingInPageLocators
    training_locators = TrainingPageLocators
    training_video_locators = TrainingVideoPageLocators
    women_locators = WomenPageLocators

    def check_greeting_message(self):
        return self.element_is_visible(self.header_locators.GREETING_MESSAGE)

    def check_create_account_page_link(self):
        return self.element_is_visible(self.header_locators.CREATE_AN_ACCOUNT)

    def check_create_account_page_header(self):
        return self.element_is_visible(self.create_account_locators.CREATE_NEW_CUSTOMER_ACCOUNT_HEADER)

    def check_sign_in_page_link(self):
        return self.element_is_visible(self.header_locators.SIGN_IN)

    def check_sign_in_page_header(self):
        return self.element_is_visible(self.sign_in_locators.PAGE_HEADER)

    def check_logo_link(self):
        return self.element_is_visible(self.header_locators.LOGO)

    def redirected_the_link_sale(self, page):
        page.click_and_return_element(page.header_locators.SALE)
        return self.element_is_visible(self.header_locators.SALE)

    def check_cart_icon_link(self):
        return self.element_is_visible(self.header_locators.CART_ICON)

    def check_cart_message(self):
        return self.element_is_visible(self.header_locators.CART_BUTTON_MESSAGE).text

    def check_search_field(self):
        return self.element_is_visible(self.header_locators.SEARCH_FIELD).get_attribute('placeholder')

    def enter_search_field_and_get_dropdown(self):
        """
        This method activates the field "Search", enters the term "T-shirt" in the field "Search"
        and returns the combo box that appears after you enter the search term.
        """
        search_field = self.click_and_return_element(self.header_locators.SEARCH_FIELD)
        search_field.send_keys("T-shirt")
        return self.elements_are_visible(self.header_locators.SEARCH_DROPDOWN)

    def activate_search_field_and_check_style(self):
        """
        This method activates the field "Search" and checks if the style of the field changes upon activation.
        It returns the styles before and after activation for comparison.
        """
        initial_box_shadow = self.check_element_hover_style(self.header_locators.SEARCH_FIELD, 'box-shadow')
        self.click_and_return_element(self.header_locators.SEARCH_FIELD)
        active_box_shadow = self.check_element_hover_style(self.header_locators.SEARCH_FIELD, 'box-shadow')
        return initial_box_shadow, active_box_shadow

    def link_sale_is_visible_and_interactive(self):
        element = self.element_is_visible(self.header_locators.SALE)
        clickable = self.element_is_clickable(self.header_locators.SALE)
        interactive = self.check_element_hover_style(self.header_locators.SALE, 'pointer')
        return element, clickable, interactive

    def redirected_the_link_training(self):
        element = self.element_is_visible(self.header_locators.TRAINING)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.training_locators.HEAD_TEXT)
        return url == TRAINING_PAGE_URL and text == "Training"

    def redirected_the_link_training_video_download(self):
        self.check_element_hover_style(self.header_locators.TRAINING, 'pointer')
        element = self.element_is_present(self.header_locators.VIDEO_DOWNLOAD)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.training_video_locators.HEAD_TEXT)
        return url == VIDEO_DOWNLOAD_PAGE_URL and text == "Video Download"

    def link_training_is_visible_and_interactive(self):
        self.element_is_visible(self.header_locators.TRAINING)
        interactive = self.check_element_hover_style(self.header_locators.TRAINING, 'pointer')
        element = self.element_is_visible(self.header_locators.VIDEO_DOWNLOAD)
        return element, interactive

    def link_what_is_new_is_visible_and_interactive(self):
        element = self.element_is_visible(self.header_locators.WHAT_IS_NEW)
        clickable = self.element_is_clickable(self.header_locators.WHAT_IS_NEW)
        interactive = self.check_element_hover_style(self.header_locators.WHAT_IS_NEW, 'pointer')
        return element, clickable, interactive

    def redirection_of_the_link_women(self):
        element = self.element_is_visible(self.header_locators.WOMEN)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.women_locators.WOMEN_HEAD_TEXT)
        return url == WOMEN_PAGE_URL and text == "Women"
