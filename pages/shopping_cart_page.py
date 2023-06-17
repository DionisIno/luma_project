import allure
from pages.base_page import BasePage
from locators.shopping_cart_locators import ShoppingCartPageLocators


class ShoppingCartPage(BasePage):
    shopping_locators = ShoppingCartPageLocators

    @allure.step("Check shopping cart title")
    def check_shopping_cart_title(self):
        """This method check that shopping cart title is displayed correctly"""
        shopping_cart_title = self.element_is_visible(self.shopping_locators.TITLE).text
        return shopping_cart_title

    @allure.step("Check here link is clickable")
    def check_here_link_is_clickable(self):
        """This method check that here link in the displayed text is clickable"""
        here_link = self.element_is_clickable(self.shopping_locators.HERE_LINK)
        return here_link

    @allure.step("Check here link leads to correct url")
    def here_link_actual_url(self):
        """This method check that here link in the displayed text leads to the correct url"""
        here_link = self.element_is_visible(self.shopping_locators.HERE_LINK)
        here_link.click()
        current_url = self.driver.current_url
        return current_url









