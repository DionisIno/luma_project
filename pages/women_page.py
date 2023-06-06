from locators.women_page_locators import WomenPageLocators
from pages.base_page import BasePage


class WomenPage(BasePage):
    side_panel_locators = WomenPageLocators

    def check_side_panel_name(self):
        shop_by_title = self.element_is_visible(self.side_panel_locators.SHOP_BY)
        title_shop_by = shop_by_title.text
        return title_shop_by
