from data.data_urls import WOMEN_PAGE_URL
from pages.women_page import WomenPage


class TestWomenPage:

    def test_tc_12_01_01(self, driver):
        """Check Shop By title is visible"""
        page = WomenPage(driver, WOMEN_PAGE_URL)
        page.open()
        title = page.check_side_panel_name()
        assert title == "Shop By", f"Expected title: 'Shop By, Actual title: {title}"

