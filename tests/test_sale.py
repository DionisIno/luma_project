import allure
import pytest

from data.data_urls import SALE_PAGE_URL
from pages.sale_page import SalePage
from data.sale_data import expected_titles, expected_urls
from locators.sale_page_locators import SideBarLocators


@allure.epic("Sale Page")
class TestSalePage:
    @allure.feature("Testing Side Menu Bar - Women's Deals Section")
    class TestSideMenuBarWomen:
        @allure.title("TC 10.01.01 - Verify 'WOMEN'S DEALS' title is correct")
        def test_tc_10_01_01(self, driver):
            """Check title of Women's Deals section"""
            page = SalePage(driver, SALE_PAGE_URL)
            page.open()
            title = page.check_text_in_women_deals_title()
            assert title == "WOMEN'S DEALS", f"Expected title: 'WOMEN'S DEALS', Actual title: {title}"

        @allure.title("TC 10.01.02, 10.01.04, 10.01.06, 10.01.08, 10.01.10, 10.01.12 - "
                      "Verify 6 links in Women's Deals section are visible and clickable")
        @pytest.mark.parametrize("element_locator", SideBarLocators.WOMEN_DEALS_ELEMENTS.values())
        def test_tc_10_01_02__04__06__08__10__12(self, driver, element_locator):
            """Check that six elements in Women's Deals section are displayed and enabled"""
            page = SalePage(driver, SALE_PAGE_URL)
            page.open()
            element_in_women_deals = page.element_is_clickable(element_locator)
            assert element_in_women_deals is not None, "Element is not displayed or enabled"

        @allure.title("TC 10.01.03, 10.01.05, 10.01.07, 10.01.09, 10.01.11, 10.01.13 - "
                      "Verify 6 links in Women's Deals open the correct pages")
        @pytest.mark.parametrize(
            "element_locator, expected_title, expected_url",
            zip(
                SideBarLocators.WOMEN_DEALS_ELEMENTS.values(),
                expected_titles.values(),
                expected_urls.values(),
            )
        )
        def test_tc_10_01_03__05_07_09_11_13(self, driver, element_locator, expected_title, expected_url):
            """Check that links in Women's Deals section lead to the correct pages after click"""
            page = SalePage(driver, SALE_PAGE_URL)
            page.open()
            element_in_women_deals = page.element_is_clickable(element_locator)
            element_in_women_deals.click()

            assert page.get_actual_url(driver) == expected_url, "URL does not match"
            assert page.get_actual_title(driver) == expected_title, "Title does not match"

    @allure.feature("Testing Side Menu Bar - Men's Deals Section")
    class TestSideMenuBarMen:
        @allure.title("TC 10.02.01 - Verify 'MEN'S DEALS' title is correct")
        @pytest.mark.xfail(reason="This test is expecting failure == Assertion Error "
                                  "because of bug - Mens's instead of Men's")
        def test_tc_10_02_01(self, driver):
            """Check title of Men's Deals section"""
            page = SalePage(driver, SALE_PAGE_URL)
            page.open()
            title = page.check_text_in_men_deals_title()
            assert title == "MEN'S DEALS", f"Expected title: 'MEN'S DEALS', Actual title: {title}"

        @allure.title("TC 10.02.02, 10.02.04, 10.02.06, 10.02.08, 10.02.10 - "
                      "Verify 5 links in Men's Deals section are visible and clickable")
        @pytest.mark.parametrize("element_locator", SideBarLocators.MEN_DEALS_ELEMENTS.values())
        def test_tc_10_02_02__04__06__08__10(self, driver, element_locator):
            """Check that five elements in Men's Deals section are displayed and enabled"""
            page = SalePage(driver, SALE_PAGE_URL)
            page.open()
            element_in_men_deals = page.element_is_clickable(element_locator)
            assert element_in_men_deals is not None, "Element is not displayed or enabled"
