import time
import allure
from pages.base_page import BasePage
from locators.shopping_cart_locators import ShoppingCartPageLocators
import random
import string
from selenium.common.exceptions import NoSuchElementException, TimeoutException


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

    @allure.step("Check 'Proceed to checkout' button is clickable")
    def check_checkout_button_is_clickable(self):
        """This method checks that 'Proceed to checkout' button is clickable"""
        checkout = self.element_is_clickable(self.shopping_locators.CHECKOUT_BUTTON)
        return checkout

    @allure.step("Get a random number between 1 and 10")
    def random_qty(self):
        """This method gets a random number between 1 and 50"""
        random_num = random.randint(1, 10)
        return random_num

    @allure.step("Check Price item")
    def get_price_item(self):
        """This method gets a price item"""
        price_item = self.element_is_visible(self.shopping_locators.PRICE_ITEM)
        price_num = price_item.text[1:]
        return float(price_num)

    @allure.step("Get subtotal of item")
    def get_subtotal_of_item(self):
        """This method gets subtotal of item"""
        subtotal = self.element_is_visible(self.shopping_locators.SUBTOTAL_ITEM)
        subtotal_num = subtotal.text[1:]
        return float(subtotal_num)

    @allure.step("Check subtotal for items: price * qty")
    def check_subtotal_of_item_price_multiply_qty(self):
        """Check subtotal for items: price * qty"""
        input_field = self.element_is_clickable(self.shopping_locators.QUANTITY_FIELD)
        input_field.click()
        input_field.clear()
        qty = self.random_qty()
        input_field.send_keys(qty)
        update_button = self.element_is_clickable(self.shopping_locators.UPDATE_BUTTON)
        update_button.click()
        price = self.get_price_item()
        time.sleep(2)
        subtotal = price * qty
        return subtotal

    @allure.step("Check 'Proceed to checkout' button redirects to the shipping page")
    def check_checkout_button_redirects_to_shipping_page(self):
        """This method checks that 'Proceed to checkout' button redirects to the shipping page"""
        button = self.element_is_clickable(self.shopping_locators.CHECKOUT_BUTTON)
        button.click()
        time.sleep(3)
        current_url = self.driver.current_url
        return current_url


    @allure.step("Get Subtotal in the Summary Card")
    def get_subtotal_in_summary(self):
        """This method gets Subtotal in the Summary Card"""
        subtotal = self.element_is_visible(self.shopping_locators.SUBTOTAL_SUMMARY)
        subtotal_summary_num = subtotal.text[1:]
        return float(subtotal_summary_num)

    @allure.step("Get Discount in the Summary Card")
    def get_discount_in_summary(self):
        """This method gets Discount in the Summary Card"""
        discount = self.element_is_visible(self.shopping_locators.DISCOUNT_SUMMARY)
        discount_summary_num = discount.text[2:]
        return float(discount_summary_num)

    @allure.step("Get Tax in the Summary Card")
    def get_tax_in_summary(self):
        """This method gets Tax in the Summary Card"""
        tax = self.element_is_visible(self.shopping_locators.TAX_SUMMARY)
        tax_summary_num = tax.text[1:]
        return float(tax_summary_num)

    @allure.step("Get Order Total in the Summary Card")
    def get_order_total_in_summary(self):
        """This method gets Order Total in the Summary Card"""
        order_total = self.element_is_visible(self.shopping_locators.ORDER_TOTAL)
        order_total_num = order_total.text[1:]
        return float(order_total_num)

    @allure.step("Check Order Total in the Summary Card")
    def check_order_total(self):
        """Check Order Total = Subtotal - Discount + Tax"""
        input_field = self.element_is_clickable(self.shopping_locators.QUANTITY_FIELD)
        input_field.click()
        input_field.clear()
        qty = self.random_qty()
        input_field.send_keys(qty)
        update_button = self.element_is_clickable(self.shopping_locators.UPDATE_BUTTON)
        update_button.click()
        time.sleep(2)
        subtotal = self.get_subtotal_in_summary()
        try:
            discount = self.get_discount_in_summary()
        except NoSuchElementException:
            discount = 0
        except TimeoutException:
            discount = 0
        try:
            tax = self.get_tax_in_summary()
        except NoSuchElementException:
            tax = 0
        except TimeoutException:
            tax = 0
        order_total = subtotal - discount + tax
        return order_total

    @allure.step("Check remove button deletes item from the shipping page")
    def check_remove_button_deletes_item_from_shopping_cart(self):
        """This method checks that remove button (trash bin icon) deletes item from the shipping page"""
        trash_bin = self.element_is_clickable(self.shopping_locators.DELETE_BUTTON)
        trash_bin.click()
        shopping_cart_message = self.element_is_visible(self.shopping_locators.IS_EMPTY_MESSAGE).text
        return shopping_cart_message

    @allure.step("Check Apply Discount Code is visible")
    def get_text_apply_discount_code(self):
        """This method checks that Apply Discount Code is visible"""
        apply_discount_code = self.element_is_visible(self.shopping_locators.APPLY_DISCOUNT_CODE)
        return apply_discount_code.text

    @allure.step("Apply Discount Code on click")
    def click_apply_discount_code(self):
        """Apply Discount Code on click"""
        self.element_is_clickable(self.shopping_locators.APPLY_DISCOUNT_CODE).click()

    @allure.step("Check the button Apply Discount is displayed correct")
    def check_btn_apply_discount(self):
        """Check the button 'Apply Discount' is displayed correct'"""
        return self.element_is_clickable(self.shopping_locators.BTN_APPLY_DISCOUNT).text

    # random discount code
    code = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))

    @allure.step("Get valid message coupon code")
    def get_valid_msg_coupon_code(self, code):
        """Get valid message coupon code"""
        valid_msg_coupon_code = f'The coupon code "{code}" is not valid.'
        return valid_msg_coupon_code

    @allure.step("Send discount code")
    def send_discount_code(self, code):
        """Send discount code"""
        self.fill_in_field(self.shopping_locators.INPUT_DISCOUNT_CODE, code)

    @allure.step("Click button Apply Discount")
    def click_btn_apply_discount(self):
        """Click button Apply Discount"""
        self.element_is_clickable(self.shopping_locators.BTN_APPLY_DISCOUNT).click()

    @allure.step("Get message discount code is not valid by page")
    def get_msg_discount_code_is_not_valid(self):
        """Get message discount code is not valid by page"""
        msg = self.element_is_visible(self.shopping_locators.MSG_CODE_IS_NOT_VALID).text
        return msg


