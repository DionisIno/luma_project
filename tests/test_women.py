from data.data_urls import WOMEN_PAGE_URL
from pages.women_page import WomenPage
import allure


@allure.epic("WomenPage")
class TestWomenPage:

    @allure.title("TC 12.01.01 Check side panel title Shop By is visible")
    def test_tc_12_01_01(self, driver):
        """Check Shop By title is visible"""
        page = WomenPage(driver, WOMEN_PAGE_URL)
        page.open()
        title = page.check_side_panel_name()
        assert title == "Shop By", f"Expected title: 'Shop By, Actual title: {title}"

    @allure.title("TC 12.02.01 Check side panel title Category is visible")
    def test_tc_12_02_01(self, driver):
        """Check Category title is visible"""
        page = WomenPage(driver, WOMEN_PAGE_URL)
        page.open()
        title = page.check_side_panel_category_is_visible()
        assert title == "Category", f"Expected title: 'Category, Actual title: {title}"
