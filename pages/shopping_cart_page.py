import allure
from pages.base_page import BasePage
from locators.shopping_cart_locators import ShoppingCartPageLocators


class ShoppingCartPage(BasePage):
    shopping_locators = ShoppingCartPageLocators

    @allure.step("Check shopping cart title")
    def check_shopping_cart_title(self):
        """This method checks that shopping cart title is displayed correctly"""
        shopping_cart_title = self.element_is_visible(self.shopping_locators.TITLE).text
        return shopping_cart_title

    @allure.step("Check here link is clickable")
    def check_here_link_is_clickable(self):
        """This method checks that here link in the displayed text is clickable"""
        here_link = self.element_is_clickable(self.shopping_locators.HERE_LINK)
        return here_link

    @allure.step("Check that here link leads to the correct url")
    def here_link_actual_url(self):
        """This method checks that here link in the displayed text leads to the correct url"""
        here_link = self.element_is_visible(self.shopping_locators.HERE_LINK)
        here_link.click()
        current_url = self.driver.current_url
        return current_url

    @allure.step("Check that quantity field is clickable")
    def check_quantity_field_is_clickable(self):
        """This method checks that quantity input field is displayed and clickable"""
        quantity_input = self.element_is_clickable(self.shopping_locators.QUANTITY_FIELD)
        return quantity_input

    @allure.step("Fill in quantity field")
    def fill_in_quantity_field(self, quantity):
        """This method fills in quantity input field for checking accuracy of display"""
        input_field = self.element_is_clickable(self.shopping_locators.QUANTITY_FIELD)
        input_field.click()
        input_field.clear()
        input_field.send_keys(quantity)
        update_button = self.element_is_clickable(self.shopping_locators.UPDATE_BUTTON)
        update_button.click()
        return input_field

    @allure.step("Get quantity field attribute")
    def get_quantity_field_attribute(self, attribute):
        """This method gets attribute of the quantity field"""
        quantity_input = self.element_is_clickable(self.shopping_locators.QUANTITY_FIELD)
        return quantity_input.get_attribute(attribute)

    @allure.step("Check subtotal of item")
    def check_subtotal_of_item(self):
        """This method checks that subtotal of item is displayed correctly"""
        subtotal_before_changing = self.element_is_visible(self.shopping_locators.SUBTOTAL_ITEM)
        return subtotal_before_changing.text

    @allure.step("Check subtotal in the Summary Cart")
    def check_subtotal_in_summary(self):
        """This method checks that subtotal in the summary cart is displayed correctly"""
        subtotal_sum = self.element_is_visible(self.shopping_locators.SUBTOTAL_SUMMARY)
        return subtotal_sum.text










