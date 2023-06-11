"""This section contains "Orders and Returns" page tests"""
import allure
from pages.orders_and_returns_page import OrdersAndReturnsPage
from data.data_urls import ORDERS_AND_RETURNS_PAGE_URL


@allure.epic("Orders and Returns")
class TestOrdersAndReturnsPage:
    @allure.title("TC 05.01.01 - Verify 'Order and Returns' Page Heading is present")
    def test_tc_05_01_01_check_header(self, driver):
        """This test checks "Orders and Returns" header is visible and has correct text"""
        page = OrdersAndReturnsPage(driver, ORDERS_AND_RETURNS_PAGE_URL)
        page.open()
        header_text = page.check_header()
        assert header_text == "Orders and Returns", "Header is not present or text doesn't match"
