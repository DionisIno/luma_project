"""This section contains the basic steps for running gear page tests"""

from locators.gear_page_locators import SideBarLocators
from pages.base_page import BasePage


class GearPage(BasePage):
    locators = SideBarLocators

    def check_text_in_category_title(self):
        category_title = self.element_is_visible(self.locators.CATEGORY)
        title_category = category_title.text
        return title_category

    def check_bags_element(self):
        bags = self.element_is_clickable(self.locators.BAGS)
        return bags

    def check_bags_functionality(self):
        bags = self.element_is_visible(self.locators.BAGS)
        link = bags.click()
        return link

    def get_actual_url(self, driver):
        actual_url = driver.current_url
        return actual_url
