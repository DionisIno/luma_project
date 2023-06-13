from locators.women_page_locators import WomenPageLocators
from pages.base_page import BasePage
import allure


@allure.epic('WomenPage')
class WomenPage(BasePage):
    side_panel_locators = WomenPageLocators

    @allure.step('Check the side Shop By title is visible')
    def check_side_panel_name(self):
        shop_by_title = self.element_is_visible(self.side_panel_locators.SHOP_BY)
        title_shop_by = shop_by_title.text
        return title_shop_by

    @allure.step('Check the side Category title is visible')
    def check_side_panel_category_is_visible(self):
        category_title = self.element_is_visible(self.side_panel_locators.CATEGORY_TITLE)
        text_title = category_title.text
        return text_title
