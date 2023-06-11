import pytest

from data.data_urls import SALE_PAGE_URL
from pages.sale_page import SalePage
from data.sale_data import expected_title, expected_url
from locators.sale_page_locators import SideBarLocators


class TestSalePage:

    def test_tc_10_01_01(self, driver):
        """Check title of Women's Deals section"""
        page = SalePage(driver, SALE_PAGE_URL)
        page.open()
        title = page.check_text_in_women_deals_title()
        assert title == "WOMEN'S DEALS", f"Expected title: 'WOMEN'S DEALS', Actual title: {title}"

    @pytest.mark.parametrize("element_locator", SideBarLocators.WOMEN_DEALS_ELEMENTS.values())
    def test_tc_10_01_02__04__06__08__10__12(self, driver, element_locator):
        """Check that six elements in Women's Deals section are displayed and enabled"""
        page = SalePage(driver, SALE_PAGE_URL)
        page.open()
        element_in_women_deals = page.element_is_clickable(element_locator)
        assert element_in_women_deals is not None, "Element is not displayed or enabled"

    def test_tc_10_01_03(self, driver):
        """Check that Hoodies and sweatshirts in Women's Deals section leads to the correct page after click"""
        page = SalePage(driver, SALE_PAGE_URL)
        page.open()
        page.check_women_deals_hoodies_link()
        assert page.get_actual_url(driver) == expected_url['hoodies_women_url'] \
            and page.get_actual_title(driver) == expected_title['hoodies_women'], \
            f"Expected URL: {expected_url['hoodies_women_url']}, Actual URL: {page.get_actual_url(driver)}\n"\
            f"Expected title: {expected_title['hoodies_women']}, Actual title: {page.get_actual_title(driver)}"
