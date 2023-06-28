"""This section contains the basic steps for promotion pants page tests"""

from locators.pants_promo_page_locators import PantsPromoPageLocators
from pages.base_page import BasePage


class PromotionPantsPage(BasePage):
    locators = PantsPromoPageLocators

    def check_text_in_shopping_options_title(self):
        shopping_options = self.element_is_visible(self.locators.SHOPPING_OPTIONS)
        title_shopping_options = shopping_options.text
        return title_shopping_options

    def check_text_in_style_title(self):
        style = self.element_is_visible(self.locators.STYLE)
        title_style = style.text
        return title_style
