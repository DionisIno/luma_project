from pages.base_page import BasePage
from locators.shopping_cart_locators import ShoppingCartPageLocators


class ShoppingCartPage(BasePage):
    shopping_locators = ShoppingCartPageLocators

    def check_shopping_cart_title(self):
        shopping_cart_title = self.element_is_visible(self.shopping_locators.TITLE).text
        return shopping_cart_title

    def check_here_link_is_clickable(self):
        here_link = self.element_is_clickable(self.shopping_locators.HERE_LINK)
        return here_link

    def here_link_actual_url(self):
        here_link = self.element_is_visible(self.shopping_locators.HERE_LINK)
        here_link.click()
        current_url = self.driver.current_url
        return current_url









