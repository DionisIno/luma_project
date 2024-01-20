import allure
import pytest

from data.data_urls import WOMEN_PAGE_URL
from pages.women_page import WomenPage
from locators.women_page_locators import WomenPageLocators


@allure.epic("WomenPage")
class TestWomenPage:

    @allure.title("TC 12.01.01 - Verify side panel title Shop By is visible")
    def test_tc_12_01_01(self, driver):
        """Check Shop By title is visible"""
        page = WomenPage(driver, WOMEN_PAGE_URL)
        page.open()
        title = page.check_side_panel_name()
        assert title == "Shop By", f"Expected title: 'Shop By, Actual title: {title}"

    @allure.title("TC 12.02.01 - Verify side panel title Category is visible")
    def test_tc_12_02_01(self, driver):
        """Check Category title is visible"""
        page = WomenPage(driver, WOMEN_PAGE_URL)
        page.open()
        title = page.check_side_panel_category_is_visible()
        assert title == "Category", f"Expected title: 'Category, Actual title: {title}"

    @allure.title("TC 12.05.01/02/03/04 - Verify the Sidebar text is visible")
    @pytest.mark.parametrize("item_locator, expected_text", WomenPageLocators.ITEMS)
    def test_item_visibility_and_text(self, driver, item_locator, expected_text):
        """Check if items are visible"""
        page = WomenPage(driver, WOMEN_PAGE_URL)
        page.open()
        element = page.element_is_visible(item_locator)
        assert element is not None, "Element is not visible"
        assert element.text == expected_text, f"Expected text is '{expected_text}', but got '{element.text}'"
