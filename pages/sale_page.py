from locators.sale_page_locators import SideBarLocators
from pages.base_page import BasePage


class SalePage(BasePage):
    side_bar_locators = SideBarLocators

    def check_text_in_women_deals_title(self):
        women_deals_title = self.element_is_visible(self.side_bar_locators.WOMEN_DEALS_TITLE)
        title_women_deals = women_deals_title.text
        return title_women_deals
