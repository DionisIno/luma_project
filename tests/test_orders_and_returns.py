"""This section contains "Orders and Returns" page tests"""
import allure
import pytest
from pages.orders_and_returns_page import OrdersAndReturnsPage
from data.data_urls import ORDERS_AND_RETURNS_PAGE_URL
from data.orders_and_returns_data import orders_and_returns_data as data


@pytest.fixture(scope="function")
def page(driver):
    page = OrdersAndReturnsPage(driver, ORDERS_AND_RETURNS_PAGE_URL)
    page.open()
    return page


@allure.epic("Orders and Returns")
class TestOrdersAndReturnsPage:
    @allure.title("TC 05.01.01 - Verify that 'Order and Returns' Page Heading is present")
    def test_tc_05_01_01_check_header(self, driver, page):
        """This test checks "Orders and Returns" header is visible and has correct text"""
        header_text = page.check_header()
        assert header_text == data['page_header'], "Header is not present or text doesn't match"

    @allure.title("TC 05.01.02 - Verify that 'Order and Returns' form header is present")
    def test_tc_05_01_02_check_header(self, driver, page):
        """This test checks "Orders and Returns" form header is visible and has correct text"""
        form_header_text = page.check_form_header()
        assert form_header_text == data['form_header'], "Form header is not present or text doesn't match"

    @allure.title("TC 05.01.03 - Verify that 'Order ID' input field is visible")
    def test_tc_05_01_03_check_order_id_field(self, driver, page):
        """This test checks Order ID input field is visible"""
        order_id_input = page.check_order_id_input_is_visible()
        assert order_id_input is not None, "Order ID input field is not present or visible"
