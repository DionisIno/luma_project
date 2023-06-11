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

    def click_link_women_deals(self, element_locator):
        link_locator = self.side_bar_locators.WOMEN_DEALS_ELEMENTS[element_locator]
        element = self.element_is_visible(*link_locator)
        element.click()

    def get_actual_title(self, driver):
        actual_title = driver.title
        return actual_title

    def get_actual_url(self, driver):
        actual_url = driver.current_url
        return actual_url
