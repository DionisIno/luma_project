"""This section contains home page tests"""
import json
import time

from pages.main_page import MainPage
from data.data_urls import MAIN_PAGE_URL


class TestMainPage:
    class TestHotSellerSection:

        def test_verify_the_card_is_interactive_on_hover(self, driver):
            """This test checks that the card is interactive"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            shadow_before, shadow_after = page.check_for_shadow_appearance_when_hovering_over_the_card()
            assert shadow_before != shadow_after, \
                "Card is not interactive"

        def test_verify_the_card_has_title(self, driver):
            """This test checks that the card has title"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            title_text = page.check_product_card_title()
            assert len(title_text) > 0, "Card has no title"

        def test_check_for_duplicate_titles_after_clicking_on_the_card(self, driver):
            """This test checks for the same titles after clicking on the product card and going to the product page"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            text_before, text_after = page.check_the_correct_page_title_after_click_on_the_card()
            assert text_before == text_after, \
                "Headers are not equal or redirect to the wrong page of the site"

        def test_check_card_price(self, driver):
            """This test checks that the card has a price and a price in USD"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            text = page.check_card_price()
            assert len(text) > 0 and "$" in text, "The price is not present and does not contain the $ sign"

        def test_example(self, driver, sing_in):

            page = MainPage(driver, MAIN_PAGE_URL)

        def test_tc_06_01_08_check_btn_add_to_cart_is_visible(self, driver):
            """This test checks that button Add to Cart is visible on the product card when hover by product"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            assert page.btn_is_visible(), 'Button Add to Cart is not visible on the product card'

