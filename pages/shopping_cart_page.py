from pages.base_page import BasePage
from locators.shopping_cart_locators import ShoppingCartPageLocators


class ShoppingCartPage(BasePage):
    shopping_locators = ShoppingCartPageLocators

    def check_shopping_cart_title(self):
        shopping_cart_title = self.element_is_visible(self.shopping_locators.TITLE).text
        return shopping_cart_title






