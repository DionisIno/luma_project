import allure
import pytest

from data.data_urls import SALE_PAGE_URL
from pages.sale_page import SalePage
from data.sale_data import expected_titles_w, expected_urls_w, expected_titles_m, expected_urls_m, \
    expected_titles_gear, expected_urls_gear, img_src, promo_blocks_titles, promo_blocks_contents, \
    expected_titles_promo_blocks, expected_urls_promo_blocks, img_src_three_columns, \
    three_columns_block_titles, three_columns_blocks_contents
from locators.sale_page_locators import SideBarLocators, MainContentPromoBlocks


@pytest.fixture(scope="function")
def sale_page(driver):
    """This function navigate to Sale page and open it for testing"""
    sale_page = SalePage(driver, SALE_PAGE_URL)
    sale_page.open()
    return sale_page


@allure.epic("Sale Page")
class TestSalePage:
    @allure.feature("Testing Side Menu Bar - Women's Deals Section")
    class TestSideMenuBarWomen:
        @allure.title("TC 10.01.01 - Verify 'WOMEN'S DEALS' title is correct")
        def test_tc_10_01_01(self, sale_page):
            """Check title of Women's Deals section"""
            title = sale_page.check_text_in_women_deals_title()
            assert title == "WOMEN'S DEALS", f"Expected title: 'WOMEN'S DEALS', Actual title: {title}"

        @allure.title("TC 10.01.02, 10.01.04, 10.01.06, 10.01.08, 10.01.10, 10.01.12 - "
                      "Verify 6 links in Women's Deals section are visible and clickable")
        @pytest.mark.parametrize("element_locator", SideBarLocators.WOMEN_DEALS_ELEMENTS.values())
        def test_tc_10_01_02__04__06__08__10__12(self, element_locator, sale_page):
            """Check that six elements in Women's Deals section are displayed and enabled"""
            element_in_women_deals = sale_page.element_is_clickable(element_locator)
            assert element_in_women_deals is not None, "Element is not displayed or enabled"

        @allure.title("TC 10.01.03, 10.01.05, 10.01.07, 10.01.09, 10.01.11, 10.01.13 - "
                      "Verify 6 links in Women's Deals open the correct pages")
        @pytest.mark.parametrize(
            "element_locator, expected_title, expected_url",
            zip(
                SideBarLocators.WOMEN_DEALS_ELEMENTS.values(),
                expected_titles_w.values(),
                expected_urls_w.values(),
            )
        )
        def test_tc_10_01_03__05_07_09_11_13(self, sale_page, element_locator, expected_title, expected_url):
            """Check that six links in Women's Deals section lead to the correct pages after click"""
            element_in_women_deals = sale_page.element_is_clickable(element_locator)
            element_in_women_deals.click()
            assert sale_page.get_actual_url_of_current_page() == expected_url \
                   and sale_page.get_actual_title_of_current_page() == expected_title, "Either the title or URL of " \
                                                                                       "the page does not match the " \
                                                                                       "expected value"

    @allure.feature("Testing Side Menu Bar - Men's Deals Section")
    class TestSideMenuBarMen:
        @allure.title("TC 10.02.01 - Verify 'MEN'S DEALS' title is correct")
        @pytest.mark.xfail(reason="This test is expecting failure == Assertion Error "
                                  "because of error in spelling Men's")
        def test_tc_10_02_01(self, sale_page):
            """Check title of Men's Deals section"""
            title = sale_page.check_text_in_men_deals_title()
            assert title == "MEN'S DEALS", f"Expected title: 'MEN'S DEALS', Actual title: {title}"

        @allure.title("TC 10.02.02, 10.02.04, 10.02.06, 10.02.08, 10.02.10 - "
                      "Verify 5 links in Men's Deals section are visible and clickable")
        @pytest.mark.parametrize("element_locator", SideBarLocators.MEN_DEALS_ELEMENTS.values())
        def test_tc_10_02_02__04__06__08__10(self, sale_page, element_locator):
            """Check that five elements in Men's Deals section are displayed and enabled"""
            element_in_men_deals = sale_page.element_is_clickable(element_locator)
            assert element_in_men_deals is not None, "Element is not displayed or enabled"

        @allure.title("TC 10.02.03, 10.02.05, 10.02.07, 10.02.09, 10.02.11 - "
                      "Verify 5 links in Men's Deals open the correct pages")
        @pytest.mark.parametrize(
            "element_locator, expected_title, expected_url",
            zip(
                SideBarLocators.MEN_DEALS_ELEMENTS.values(),
                expected_titles_m.values(),
                expected_urls_m.values(),
            )
        )
        def test_tc_10_01_03__05_07_09_11_13(self, sale_page, element_locator, expected_title, expected_url):
            """Check that five links in Men's Deals section lead to the correct pages after click"""
            element_in_men_deals = sale_page.element_is_clickable(element_locator)
            element_in_men_deals.click()
            assert sale_page.get_actual_url_of_current_page() == expected_url \
                   and sale_page.get_actual_title_of_current_page() == expected_title, "Either the title or URL of " \
                                                                                       "the page does not match the " \
                                                                                       "expected value"

    @allure.feature("Testing Side Menu Bar - Gear Deals Section")
    class TestSideMenuBarGear:
        @allure.title("TC 10.03.01 - Verify 'GEAR DEALS' title is correct")
        def test_tc_10_03_01(self, sale_page):
            """Check title of Gear Deals section"""
            title = sale_page.check_text_in_gear_deals_title()
            assert title == "GEAR DEALS", f"Expected title: 'GEAR DEALS', Actual title: {title}"

        @allure.title("TC 10.03.02, 10.02.04 - "
                      "Verify 2 links in Gear Deals section are visible and clickable")
        @pytest.mark.parametrize("element_locator", SideBarLocators.GEAR_DEALS_ELEMENTS.values())
        def test_tc_10_03_02__04(self, sale_page, element_locator):
            """Check that two elements in Gear Deals section are displayed and enabled"""
            element_in_men_deals = sale_page.element_is_clickable(element_locator)
            assert element_in_men_deals is not None, "Element is not displayed or enabled"

        @allure.title("TC 10.03.03, 10.03.05 - "
                      "Verify 2 links in Gear Deals open the correct pages")
        @pytest.mark.parametrize(
            "element_locator, expected_title, expected_url",
            zip(
                SideBarLocators.GEAR_DEALS_ELEMENTS.values(),
                expected_titles_gear.values(),
                expected_urls_gear.values(),
            )
        )
        def test_tc_10_03_03__05(self, sale_page, element_locator, expected_title, expected_url):
            """Check that two links in Gear Deals section lead to the correct pages after click"""
            element_in_gear_deals = sale_page.element_is_clickable(element_locator)
            element_in_gear_deals.click()

            assert sale_page.get_actual_url_of_current_page() == expected_url \
                   and sale_page.get_actual_title_of_current_page() == expected_title, "Either the title or URL of " \
                                                                                       "the page does not match the " \
                                                                                       "expected value"

    @allure.feature("Testing Promo Blocks, Main Block (Women's Deals) and 2 columns block - Men's Bargain, Gear Steals")
    class TestPromoBlocks:
        @allure.title("TC 10.04.01 - Verify that the Women Deals contains an image")
        def test_tc_10_04_01(self, sale_page):
            """Check img existence of Women's Deals section"""
            img = sale_page.check_img_in_main_block()
            assert img == img_src["sale_women_img"], "Image doesn't exist or isn't accurate"

        @allure.title("TC 10.04.04 - Verify that the Men's Deals contains an image")
        def test_tc_10_04_04(self, sale_page):
            """Check img existence of Men's Deals section"""
            img = sale_page.check_img_in_men_block()
            assert img == img_src["sale_men_img"], "Image doesn't exist or isn't accurate"

        @allure.title("TC 10.04.07 - Verify that the Gear Deals contains an image")
        def test_tc_10_04_07(self, sale_page):
            """Check img existence of Gear Deals section"""
            img = sale_page.check_img_in_gear_block()
            assert img == img_src["sale_gear_img"], "Image doesn't exist or isn't accurate"

        @allure.title("TC 10.04.02 - Verify the text in main block - Women's Deals")
        def test_tc_10_04_02(self, sale_page):
            """Check title-text and content-text in main block - Women's Deals"""
            title = sale_page.check_title_text_in_main_block()
            content = sale_page.check_content_text_in_main_block()
            assert title == promo_blocks_titles["sale_women_title"] \
                   and content == promo_blocks_contents["sale_women_content"], "Either title or content isn't accurate."

        @allure.title("TC 10.04.05 - Verify the text in 2 columns block - Men's Deals")
        def test_tc_10_04_05(self, sale_page):
            """Check title-text and content-text in 2 columns block - Men's Deals"""
            title = sale_page.check_title_text_in_men_block()
            content = sale_page.check_content_text_in_men_block()
            assert title == promo_blocks_titles["sale_men_title"] \
                   and content == promo_blocks_contents["sale_men_content"], "Either title or content isn't accurate."

        @allure.title("TC 10.04.08 - Verify the text in 2 columns block - Gear Deals")
        def test_tc_10_04_08(self, sale_page):
            """Check title-text and content-text in 2 columns block - Gear Deals"""
            title = sale_page.check_title_text_in_gear_block()
            content = sale_page.check_content_text_in_gear_block()
            assert title == promo_blocks_titles["sale_gear_title"] \
                   and content == promo_blocks_contents["sale_gear_content"], "Either title or content isn't accurate."

        @allure.title("TC 10.04.03, 10.04.06, 10.04.09 - "
                      "Verify that links in Main block, 2 columns block open the correct pages")
        @pytest.mark.parametrize(
            "element_locator, expected_title, expected_url",
            zip(
                MainContentPromoBlocks.MAIN_AND_2COLUMNS_BLOCKS_BUTTONS.values(),
                expected_titles_promo_blocks.values(),
                expected_urls_promo_blocks.values(),
            )
        )
        def test_tc_10_04_03__06__09(self, sale_page, element_locator, expected_title, expected_url):
            """Check that two links in Gear Deals section lead to the correct pages after click"""
            element_in_promo_block = sale_page.element_is_clickable(element_locator)
            element_in_promo_block.click()

            assert sale_page.get_actual_url_of_current_page() == expected_url \
                   and sale_page.get_actual_title_of_current_page() == expected_title, "Either the title or URL of " \
                                                                                       "the page does not match the " \
                                                                                       "expected value"

        @allure.title("TC 10.04.10 - Verify that the sale-20-off contains an image")
        def test_tc_10_04_10(self, sale_page):
            """Check img existence of 1st column in 3-columns Promo Block section"""
            img = sale_page.check_img_in_first_block()
            assert img == img_src_three_columns["first_column_img"], "Image doesn't exist or isn't accurate"

        @allure.title("TC 10.04.12 - Verify that the sale-free-shipping contains an image")
        def test_tc_10_04_12(self, sale_page):
            """Check img existence of 2nd column in 3-columns Promo Block section"""
            img = sale_page.check_img_in_second_block()
            assert img == img_src_three_columns["second_column_img"], "Image doesn't exist or isn't accurate"

        @allure.title("TC 10.04.14 - Verify that the sale-women-t-shirts contains an image")
        def test_tc_10_04_14(self, sale_page):
            """Check img existence of 3rd column in 3-columns Promo Block section"""
            img = sale_page.check_img_in_third_block()
            assert img == img_src_three_columns["third_column_img"], "Image doesn't exist or isn't accurate"

        @allure.title("TC 10.04.11 - Verify the text in 3-columns block- sale-20-off")
        def test_tc_10_04_11(self, sale_page):
            """Check title-text and content-text in 3-columns block - sale-20-off"""
            title = sale_page.check_title_text_in_first_block()
            content = sale_page.check_content_text_in_first_block()
            assert title == three_columns_block_titles["first_column"] \
                   and content == three_columns_blocks_contents["first_column"], "Either title or content isn't " \
                                                                                 "accurate."

        @allure.title("TC 10.04.13 - Verify the text in 3-columns block - sale-free-shipping")
        def test_tc_10_04_13(self, sale_page):
            """Check title-text and content-text in 3-columns block - sale-free-shipping"""
            title = sale_page.check_title_text_in_second_block()
            content = sale_page.check_content_text_in_second_block()
            assert title == three_columns_block_titles["second_column"] \
                   and content == three_columns_blocks_contents["second_column"], "Either title or content isn't " \
                                                                                  "accurate."

        @allure.title("TC 10.04.15 - Verify the text in 3-columns block - sale-women-t-shirts")
        def test_tc_10_04_15(self, sale_page):
            """Check title-text and content-text in 3-columns block - sale-women-t-shirts"""
            title = sale_page.check_title_text_in_third_block()
            content = sale_page.check_content_text_in_third_block()
            assert title == three_columns_block_titles["third_column"] \
                   and content == three_columns_blocks_contents["third_column"], "Either title or content isn't " \
                                                                                 "accurate."
