import allure

from locators.sale_page_locators import SideBarLocators
from pages.base_page import BasePage


class SalePage(BasePage):
    side_bar_locators = SideBarLocators

    @allure.step("Check text in Women's deals title")
    def check_text_in_women_deals_title(self):
        women_deals_title = self.element_is_visible(self.side_bar_locators.WOMEN_DEALS_TITLE)
        title_women_deals = women_deals_title.text
        return title_women_deals

    @allure.step("Check interactivity of 'Hoodies and sweatshirt' element in Women's deals title")
    def check_women_deals_hoodies_element(self):
        element = self.element_is_clickable(self.side_bar_locators.HOODIES_AND_SWEATSHIRTS_W)
        return element

    @allure.step("Check interactivity of 6 elements in Women's deals title")
    def click_link_women_deals(self, element_locator):
        link_locator = self.side_bar_locators.WOMEN_DEALS_ELEMENTS[element_locator]
        element = self.element_is_visible(*link_locator)
        element.click()

    @allure.step("Get actual title of webpage")
    def get_actual_title(self, driver):
        actual_title = driver.title
        return actual_title

    @allure.step("Get actual URL of webpage")
    def get_actual_url(self, driver):
        actual_url = driver.current_url
        return actual_url

    @allure.step("Check text in Men's deals title")
    def check_text_in_men_deals_title(self):
        men_deals_title = self.element_is_visible(self.side_bar_locators.MEN_DEALS_TITLE)
        title_men_deals = men_deals_title.text
        return title_men_deals
