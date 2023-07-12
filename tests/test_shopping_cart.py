import time

import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from pages.shopping_cart_page import ShoppingCartPage
from data.data_urls import SHOPPING_CART_PAGE, MAIN_PAGE_URL, ITEM_CART_URL, SHIPPING_PAGE
from locators.shopping_cart_locators import ShoppingCartPageLocators as shopping_locators


@pytest.fixture(scope="function")
def full_cart_page(driver):
    driver.get(ITEM_CART_URL)
    size_button = wait(driver, 5).until(EC.presence_of_element_located(shopping_locators.SIZE_BUTTON))
    size_button.click()
    color_button = wait(driver, 3).until(EC.presence_of_element_located(shopping_locators.COLOR_BUTTON))
    color_button.click()
    add_to_cart_button = wait(driver, 3).until(EC.presence_of_element_located(shopping_locators.ADD_TO_CART_BUTTON))
    add_to_cart_button.click()
    wait(driver, 5).until(EC.presence_of_element_located(shopping_locators.SHOPPING_CART_LINK))
    shopping_cart_link = wait(driver, 5).until(EC.presence_of_element_located(shopping_locators.SHOPPING_CART_LINK))
    shopping_cart_link.click()


@allure.epic("Shopping Cart")
@allure.feature('Shopping Cart is empty')
class TestShoppingCart:

    @allure.title("tc 07.01.01 Verify that title Shopping Cart is displayed correctly")
    def test_tc_07_01_01_verify_title_shopping_cart_is_displayed_correctly(self, driver):
        """Check Shopping Cart title is displayed correctly"""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        page.open()
        title = page.check_shopping_cart_title()
        assert title == "Shopping Cart", "The title of Shopping Cart is not displayed correctly"

    @allure.title("tc 07.01.03 Verify that here link is displayed and clickable")
    def test_tc_07_01_03_verify_here_link_is_actual(self, driver):
        """Check that the “here” link is displayed and clickable."""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        page.open()
        here_link = page.check_here_link_is_clickable()
        assert here_link is not None, 'The link "here" is not actual'

    @allure.title("tc 07.01.04 Verify that here link leads to the main page")
    def test_tc_07_01_04_verify_here_link_leads_to_the_main_page(self, driver):
        """Verify that the link "here" redirects to the main page."""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        page.open()
        actual_link = page.here_link_actual_url()
        assert actual_link == MAIN_PAGE_URL


@allure.feature('Shopping Cart is full')
class TestShoppingCartFull:

    @allure.title("tc 07.02.01 Verify that title Shopping Cart is displayed correctly when it is full")
    def test_tc_07_02_01_verify_title_shopping_cart_is_displayed_correctly(self, driver, full_cart_page):
        """Check Shopping Cart title is displayed correctly"""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        page.open()
        title = page.check_shopping_cart_title()
        assert title == "Shopping Cart", "The title of Shopping Cart is not displayed correctly"

    @allure.title("tc 07.02.03 Verify that quantity field is displayed and clickable")
    def test_tc_07_02_03_verify_quantity_field_is_clickable(self, driver, full_cart_page):
        """Check that quantity field is displayed and clickable."""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        page.open()
        quantity_field = page.check_quantity_field_is_clickable
        assert quantity_field is not None, 'The quantity input field is not displayed or clickable'

    @allure.title("tc 07.02.04 Verify that entered quantity displayed correctly after changing")
    def test_tc_07_02_04_verify_quantity_field_displayed_correctly(self, driver, full_cart_page):
        """Check that entered quantity displayed correctly after changing."""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        page.fill_in_quantity_field("2")
        displayed_quantity = page.get_quantity_field_attribute("value")
        assert displayed_quantity == "2", "Displayed quantity isn't the same as entered in the quantity field"

    @allure.title("tc 07.02.05 Verify the subtotal amounts in the item cart and in the Summary cart are the same.")
    def test_tc_07_02_05_subtotal_in_the_item_cart_and_in_the_summarys_cart_are_equal(self, driver, full_cart_page):
        """Verify the subtotal amounts in the item cart and in the summary cart are the same."""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        subtotal_item = page.check_subtotal_of_item()
        subtotal_summary = page.check_subtotal_in_summary()
        assert subtotal_item == subtotal_summary, "The subtotals aren't the same"

    @allure.title("tc 07.02.07 Verify that 'Proceed to checkout' button is displayed and clickable")
    def test_tc_07_02_07_verify_proceed_to_checkout_button_is_actual(self, driver, full_cart_page):
        """Check that the 'Proceed to checkout' button is displayed and clickable."""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        checkout_button = page.check_checkout_button_is_clickable
        assert checkout_button is not None, 'The "Proceed to checkout" button is not actual'

    @allure.title("tc 07.02.08 Verify that 'Proceed to checkout' button redirects to the shipping page")
    def test_tc_07_02_08_verify_proceed_to_checkout_button_leads_to_the_shipping_page(self, driver, full_cart_page):
        """Verify that the 'Proceed to checkout' button redirects to the shipping page."""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        link = page.check_checkout_button_redirects_to_shipping_page()
        assert link == SHIPPING_PAGE

    @allure.title("tc 07.02.21 Verify subtotal for items: subtotal = price * qty and displayed correctly.")
    def test_tc_07_02_21_verify_subtotal_items_displayed_correctly_in_the_cart(self, driver, full_cart_page):
        """Verify subtotal for items: subtotal = price * qty and displayed correctly."""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        subtotal = page.check_subtotal_of_item_price_multiply_qty()
        subtotal_by_page = page.get_subtotal_of_item()
        assert subtotal == subtotal_by_page, 'Wrong count Subtotal for items'

    @allure.title("tc 07.02.22 Verify subtotal in Summury Card: subtotal = price * qty and displayed correctly.")
    def test_tc_07_02_22_verify_subtotal_displayed_correctly_in_summary_card(self, driver, full_cart_page):
        """Verify subtotal in summary: subtotal = price * qty and displayed correctly."""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        subtotal = page.check_subtotal_of_item_price_multiply_qty()
        subtotal_by_page = page.get_subtotal_in_summary()
        assert subtotal == subtotal_by_page, 'Wrong count Subtotal in summary'

    @allure.title("tc 07.02.23 Verify Order Total in Summury displayed correctly.")
    def test_tc_07_02_23_verify_order_total_displayed_correctly_in_summary_card(self, driver, full_cart_page):
        """Verify Order Total in Summary: Order Total = Subtotal - Discount + Tax and displayed correctly."""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        order_total = page.check_order_total()
        order_total_by_page = page.get_order_total_in_summary()
        assert order_total == order_total_by_page, 'Wrong count Order Total in summary'

    @allure.title("tc 07.02.10 Verify that remove button deletes item from the shipping page")
    def test_tc_07_02_10_verify_remove_button_delete_item(self, driver, full_cart_page):
        """Check that remove button deletes item from the shipping page"""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        message = page.check_remove_button_deletes_item_from_shopping_cart()
        assert message == "You have no items in your shopping cart.", "Remove button doesn't works correctly"


    @pytest.mark.parametrize("t_header", shopping_locators.TABLE_HEADERS.values())
    def test_tc_07_02_02_Verify_table_headers_in_item_cart_are_visible(self, driver, t_header, full_cart_page):
        """Check that table headers in item cart are visible"""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        headers_in_item_cart = page.element_is_visible(t_header)
        assert headers_in_item_cart is not None, "Table headers are not displayed"

    @allure.title("tc 07.02.24 Verify the Apply Discount Code is displayed")
    def test_tc_07_02_24_verify_field_apply_discount_code_is_displayed(self, driver, full_cart_page):
        """Check that Apply Discount Code is displayed."""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        page.open()
        apply_discount_code = page.get_text_apply_discount_code()
        assert apply_discount_code == "Apply Discount Code", 'The Apply Discount is not displayed correctly.'

    @allure.title("tc 07.02.26 Verify the button 'Apply Discount' is displayed correct")
    def test_tc_07_02_26_verify_button_apply_discount_is_displayed(self, driver, full_cart_page):
        """Check that button 'Apply Discount' is displayed correct"""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        page.open()
        page.click_apply_discount_code()
        btn = page.check_btn_apply_discount()
        assert btn == "Apply Discount", "The button Apply Discount is not displayed correctly."

    @allure.title("tc 07.02.25 Verify the message coupon code is not valid is displayed correct")
    def test_tc_07_02_25_verify_msg_coupon_code_is_not_valid_is_displayed(self, driver, full_cart_page):
        """Check that message coupon code is not valid is displayed correct"""
        page = ShoppingCartPage(driver, SHOPPING_CART_PAGE)
        page.open()
        page.click_apply_discount_code()
        page.send_discount_code(page.code)
        page.click_btn_apply_discount()
        msg = page.get_msg_discount_code_is_not_valid()
        assert msg == page.get_valid_msg_coupon_code(page.code)

