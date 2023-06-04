from locators.sale_page_locators import SideBarLocators
from pages.base_page import BasePage


class SalePage(BasePage):
    side_bar_locators = SideBarLocators

    def check_text_in_women_deals_title(self):
        women_deals_title = self.element_is_visible(self.side_bar_locators.WOMEN_DEALS_TITLE)
        title_women_deals = women_deals_title.text
        return title_women_deals

    def check_women_deals_hoodies_element(self):
        element = self.element_is_clickable(self.side_bar_locators.HOODIES_AND_SWEATSHIRTS_W)
        return element

    def check_women_deals_hoodies_link(self):
        link = self.element_is_visible(self.side_bar_locators.HOODIES_AND_SWEATSHIRTS_W).click()
        return link

    def get_actual_title(self, driver):
        actual_title = driver.title
        return actual_title

    def get_actual_url(self, driver):
        actual_url = driver.current_url
        return actual_url
