from data.data_urls import SALE_PAGE_URL, WHAT_IS_NEW_PAGE_URL, GEAR_PAGE_URL
from data.data_urls import TRAINING_PAGE_URL, VIDEO_DOWNLOAD_PAGE_URL, WOMEN_PAGE_URL
from locators.common_locators import CommonLocators
from locators.header_page_locators import HeaderPageLocators
from locators.create_account_page_locators import CreateAccountPageLocators
from locators.sign_in_page_locators import SingInPageLocators
from pages.base_page import BasePage
from locators.training_page_locators import TrainingPageLocators
from locators.training_video_page_locators import TrainingVideoPageLocators
from locators.women_page_locators import WomenPageLocators
from locators.what_is_new_page_locators import WhatIsNewPageLocators
from locators.sale_page_locators import MainContentPromoBlocks
from locators.gear_page_locators import SideBarLocators


class HeaderPage(BasePage):
    header_locators = HeaderPageLocators
    create_account_locators = CreateAccountPageLocators
    sign_in_locators = SingInPageLocators
    training_locators = TrainingPageLocators
    training_video_locators = TrainingVideoPageLocators
    women_locators = WomenPageLocators
    what_is_new_locators = WhatIsNewPageLocators
    sale_locators = MainContentPromoBlocks
    gear_locators = SideBarLocators
    common_locators = CommonLocators

    def check_greeting_message(self):
        return self.element_is_visible(self.header_locators.GREETING_MESSAGE)

    def check_common_header(self):
        return self.element_is_visible(self.common_locators.HEADER_PAGE)

    def redirected_the_link_sale(self):
        element = self.element_is_visible(self.header_locators.SALE)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.sale_locators.HEAD_TEXT)
        return url == SALE_PAGE_URL and text == "Sale"

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
        initial_box_shadow = self.check_element_hover_style(self.header_locators.SEARCH_FIELD, 'box-shadow', 5)
        self.click_and_return_element(self.header_locators.SEARCH_FIELD)
        active_box_shadow = self.check_element_hover_style(self.header_locators.SEARCH_FIELD, 'box-shadow', 5)
        return initial_box_shadow, active_box_shadow

    def link_sale_is_visible_and_interactive(self):
        element = self.element_is_visible(self.header_locators.SALE)
        clickable = self.element_is_clickable(element)
        interactive = self.check_element_hover_style(self.header_locators.SALE, 'pointer', 1)
        return element, clickable, interactive

    def redirected_the_link_training(self):
        element = self.element_is_visible(self.header_locators.TRAINING)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.training_locators.HEAD_TEXT)
        return url == TRAINING_PAGE_URL and text == "Training"

    def redirected_the_link_training_video_download(self):
        self.element_is_visible(self.header_locators.TRAINING)
        self.check_element_hover_style(self.header_locators.TRAINING, 'pointer', 1)
        element = self.element_is_present(self.header_locators.VIDEO_DOWNLOAD)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.training_video_locators.HEAD_TEXT)
        return url == VIDEO_DOWNLOAD_PAGE_URL and text == "Video Download"

    def link_training_is_visible_and_interactive(self):
        self.element_is_visible(self.header_locators.TRAINING)
        interactive = self.check_element_hover_style(self.header_locators.TRAINING, 'pointer', 1)
        element = self.element_is_visible(self.header_locators.VIDEO_DOWNLOAD)
        return element, interactive

    def link_what_is_new_is_visible_and_interactive(self):
        element = self.element_is_visible(self.header_locators.WHAT_IS_NEW)
        clickable = self.element_is_clickable(element)
        interactive = self.check_element_hover_style(self.header_locators.WHAT_IS_NEW, 'pointer', 1)
        return element, clickable, interactive

    def redirection_of_the_link_women(self):
        element = self.element_is_visible(self.header_locators.WOMEN)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.women_locators.WOMEN_HEAD_TEXT)
        return url == WOMEN_PAGE_URL and text == "Women"

    def redirected_the_link_what_is_new(self):
        element = self.element_is_visible(self.header_locators.WHAT_IS_NEW)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.what_is_new_locators.HEAD_TEXT)
        return url == WHAT_IS_NEW_PAGE_URL and text == "What's New"

    def link_gear_is_visible_and_interactive(self):
        element = self.element_is_visible(self.header_locators.GEAR)
        clickable = self.element_is_clickable(element)
        interactive = self.check_element_hover_style(self.header_locators.GEAR, 'pointer', 1)
        element_bags = self.element_is_visible(self.header_locators.BAGS)
        element_fitness_equipment = self.element_is_visible(self.header_locators.FITNESS_EQUIPMENT)
        element_watches = self.element_is_visible(self.header_locators.WATCHES)
        return element, clickable, interactive,element_bags, element_fitness_equipment, element_watches

    def check_bottoms_subsection(self):
        """This method moves the cursor over the 'Men' section, then over the 'Bottoms' subsection
        and returns the 'Pants' and 'Shorts' subsections."""
        self.action_move_to_element(self.element_is_visible(self.header_locators.MEN_SECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.BOTTOMS_SUBSECTION))
        return self.element_is_visible(self.header_locators.PANTS_SHORTS_SUBSECTION)

    def check_bottoms_subsection_link(self):
        self.action_move_to_element(self.element_is_visible(self.header_locators.MEN_SECTION))
        self.click_and_return_element(self.header_locators.BOTTOMS_SUBSECTION)
        return self.element_is_visible(self.common_locators.HEADER_PAGE)
