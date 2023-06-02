from data.data_urls import SALE_PAGE_URL
from pages.sale_page import SalePage


class TestSalePage:

    def test_tc_10_01_01(self, driver):
        """Check title of Women's Deals section"""
        page = SalePage(driver, SALE_PAGE_URL)
        page.open()
        title = page.check_text_in_women_deals_title()
        assert title == "WOMEN'S DEALS", f"Expected title: 'WOMEN'S DEALS', Actual title: {title}"

    def test_tc_10_01_02(self, driver):
        """Check that Hoodies and sweatshirts in Women's Deals section is displayed and enabled"""
        page = SalePage(driver, SALE_PAGE_URL)
        page.open()
        hoodies_and_sweatshirts = page.check_women_deals_hoodies_element()
        assert hoodies_and_sweatshirts is not None, "Hoodies and sweatshirts element is not displayed or enabled"
