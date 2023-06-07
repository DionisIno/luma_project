"""This section contains the basic steps for running gear page tests"""

from locators.gear_page_locators import SideBarLocators
from pages.base_page import BasePage


class GearPage(BasePage):
    locators = SideBarLocators

    def check_bags_element(self):
        bags = self.element_is_clickable(self.locators.BAGS)
        return bags


