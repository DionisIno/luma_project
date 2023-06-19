"""This section contains the basic steps for promotion pants page tests"""

from locators.promotion_pants_page_locators import PantsLocators
from pages.base_page import BasePage


class PromotionPantsPage(BasePage):
    locators = PantsLocators

    def check_text_in_shopping_options_title(self):
        shopping_options = self.element_is_visible(self.locators.SHOPPING_OPTIONS)
        title_shopping_options = shopping_options.text
        return title_shopping_options

    def check_text_in_style_title(self):
        style = self.element_is_visible(self.locators.STYLE)
        title_style = style.text
        return title_style
