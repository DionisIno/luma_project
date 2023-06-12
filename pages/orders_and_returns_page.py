"""This section contains the basic steps for "Orders and Returns" page tests"""

from locators.orders_and_returns_page_locators import OrdersAndReturnsLocators
from pages.base_page import BasePage


class OrdersAndReturnsPage(BasePage):
    locators = OrdersAndReturnsLocators

    def check_header(self):
        """Checks "Orders and Returns" header text"""
        return self.get_text(self.locators.PAGE_HEADER)

    def check_form_header(self):
        """Checks "Orders and Returns" form header text"""
        return self.get_text(self.locators.FORM_HEADER)

    def check_order_id_input_is_visible(self):
        """Checks "Order ID" input is visible"""
        return self.element_is_visible(self.locators.ORDER_ID_INPUT)