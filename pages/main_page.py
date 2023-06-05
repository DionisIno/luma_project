"""This section contains the basic steps for running homepage tests"""

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators

    def check_for_shadow_appearance_when_hovering_over_the_card(self):
        """Checks for shadows to appear when looking at a card"""
        card_item = self.element_is_visible(self.locators.PRODUCT_CARD)
        shadow_before = card_item.value_of_css_property("box-shadow")
        self.action_move_to_element(card_item)
        shadow_after = card_item.value_of_css_property("box-shadow")
        return shadow_before, shadow_after

    def check_product_card_title(self):
        """Checks product card title"""
        card_item = self.element_is_visible(self.locators.CARD_TITLE)
        text_title = card_item.text
        return text_title