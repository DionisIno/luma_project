from data.data_urls import SALE_PAGE_URL, HOODIES_AND_SWEATSHIRTS_WOMEN
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

    def test_tc_10_01_03(self, driver):
        """Check that Hoodies and sweatshirts in Women's Deals section leads to the correct page after click"""
        page = SalePage(driver, SALE_PAGE_URL)
        page.open()
        page.check_women_deals_hoodies_link()
        expected_title = 'Hoodies & Sweatshirts - Tops - Women'
        expected_url = HOODIES_AND_SWEATSHIRTS_WOMEN
        actual_title = driver.title
        actual_url = driver.current_url
        assert actual_url == expected_url and actual_title == expected_title, \
            f"Expected URL: {expected_url}, Actual URL: {actual_url}\n"\
            f"Expected title: {expected_title}, Actual title: {actual_title}"
