"""This section contains home page tests"""
import json
import time

import allure
import pytest

from pages.main_page import MainPage, PromoBlock
from data.data_urls import MAIN_PAGE_URL, ImageUrls
from data.main_data import product_card_button, error_message


@allure.epic("Main Page")
class TestMainPage:
    @allure.feature("Testing Hot Seller Section")
    class TestHotSellerSection:
        @allure.title("TC 06.01.02 - verify the card is interactive on hover")
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

        def test_check_card_rating(self, driver):
            """This test checks that if a product has a review, then the product card has a rating"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()

        def test_tc_06_01_08_check_btn_add_to_cart_is_visible(self, driver):
            """This test checks that button Add to Cart is visible on the product card when hover by product"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            assert page.btn_is_visible(), 'Button Add to Cart is not visible on the product card'

        @allure.title("TC 06.01.09 - check the color change to add to cart button")
        def test_tc_06_01_09_check_the_color_change_to_add_to_cart_button(self, driver):
            """This test check the color change when hovering over the Add to Cart button"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            background_before, background_after = \
                page.check_the_color_change_to_add_to_cart_button()
            assert background_before != background_after, "Product card button did not change color on hover"

        @pytest.mark.parametrize("item", product_card_button)
        def test_tc_06_01_10_check_the_cursor_change_to_cart_button(self, driver, item):
            """This test check the cursor change when hovering over the cart buttons"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            cursor_before, cursor_after = page.check_the_cursor_change_to_cart_buttons(item)
            assert cursor_before != cursor_after, "Mouse cursor has not changed"

        @pytest.mark.parametrize("item", product_card_button[1:])
        def test_tc_06_01_12_the_color_change_my_wish_and_add_to_compare_button(self, driver, item):
            """This test checks the color change of the add to wishlist button and add to compare button on hover"""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            color_before, color_after = page.check_the_color_change_to_add_to_cart_button()
            assert color_before != color_after, "Product card button did not change color on hover"

        @allure.title("Check the display of the add to wish and add to compare buttons")
        @pytest.mark.parametrize("item", product_card_button)
        def test_tc_06_01_15_check_the_display_of_the_card_buttons(self, driver, item):
            """
            This test will check that the add to wishlist and add to compare buttons are visible on the screen
            """
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            check_display = page.check_element_display(item)
            assert check_display, "Element is not displayed"

        @pytest.mark.xfail(reason="In CI, there is no transition to the user registration page, so the test fails")
        @allure.title("Check the transition to the page my wish after clicking on the button. User is not authorized")
        def test_06_01_17_check_the_transition_to_the_page_my_wish_after_click_on_the_button(self, driver):
            """
            This test will check that after clicking on the add to wishlist button,
            you are redirected to the My Wishlist page
            User is not authorized
            """
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            error_message_text = page.check_the_transition_to_the_page_my_wish_after_click_on_the_button()
            assert error_message == error_message_text, \
                f"The text does not equal {error_message} or did not go to the page 'My desires'"

        @pytest.mark.xfail(reason="In CI, there is no transition to the user registration page, so the test fails")
        @allure.title("Check the transition to the page my wish after clicking on the button. User is authorized")
        def test_06_01_18_check_the_transition_to_the_page_my_wish_after_click_on_the_button(self, driver, sing_in):
            """
            This test will check that after clicking on the add to wishlist button,
            you are redirected to the My Wishlist page
            User is authorized
            """
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            text, card_title = page.check_the_transition_to_the_page_my_wish_after_click_on_the_button_user_authorized()
            assert card_title in text, "Product card was not added to the wishlist"

    @allure.feature("Testing Promo Block")
    class TestPromoBlock:

        @allure.title("TC 13.01.01 - Check the display of the Promo Block under header on the main page")
        def test_tc_13_01_01_check_promo_block_display(self, driver):
            """This test checks if Promo Block under header is displayed on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            promo_block = page.check_promo_block_display()
            assert promo_block is True, "The element is not visible"

        @allure.title("TC 13.01.03 - Check the display of the image in section 1 'home-main' in the Promo Block "
                      "page")
        def test_tc_13_01_03_check_image_in_section1(self, driver):
            """This test checks if the image in section 1 'home-main' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            section1_image = page.check_image_in_section1()
            assert section1_image == ImageUrls.SECTION_1_IMAGE_URL, "The image is not correct"

        @allure.title("TC 13.01.06 - Check the display of the info block text "
                      "in section 1 'home-main' in the Promo Block")
        def test_tc_13_01_06_check_info_block_text_in_section1(self, driver):
            """This test checks if the info block text in section 1 'home-main' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block_text = page.check_info_block_text_in_section1()
            assert info_block_text == "New Luma Yoga Collection", "The text is not correct"

        @allure.title("TC 13.01.07 - Check the display of the info block title "
                      "in section 1 'home-main' in the Promo Block")
        def test_tc_13_01_07_check_info_block_title_in_section1(self, driver):
            """This test checks if the info block title in section 1 'home-main' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block_title = page.check_info_block_title_in_section1()
            assert info_block_title == "Get fit and look fab in new seasonal styles", "The text is not correct"

        @allure.title("TC 13.01.09 - Check the display of section 2 in the Promo Block")
        def test_tc_13_01_09_check_section2_display(self, driver):
            """This test checks if section 2 in Promo Block under header is displayed on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            section2 = page.check_section2_display()
            assert section2 is True, "The element is not visible"

        @allure.title("TC 13.01.10 - Check the display of block 1 'home-pants' in the Promo Block")
        def test_tc_13_01_10_check_section2_block1_display(self, driver):
            """This test checks if block 1 'home-pants' is displayed in section 2
            of Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block1 = page.check_section2_block1_display()
            assert block1 is True, "The element is not visible"

        @allure.title("TC 13.01.16 - Check the display of the image in block 1 'home-pants' in the Promo Block")
        def test_tc_13_01_16_check_image_in_section2_block1(self, driver):
            """This test checks if the image in section 2 block 1 'home-pants' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block1_image = page.check_image_in_section2_block1()
            assert block1_image == ImageUrls.SECTION_2_BLOCK_1_IMAGE_URL, "The image is not correct"

        @allure.title("TC 13.01.17 - Check the display of the info block in block 1 'home-pants' in the Promo Block")
        def test_tc_13_01_17_check_info_block_in_section2_block1(self, driver):
            """This test checks if info block in section 2 block 1 'home-pants' is displayed
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block = page.check_info_block_display_in_section2_block1()
            assert info_block is True, "The element is not visible"

        @allure.title("TC 13.01.18 - Check the display of the title in block 1 'home-pants' in the Promo Block")
        def test_tc_13_01_18_check_info_block_title_in_section2_block1(self, driver):
            """This test checks if the info block title in section 2 block 1 'home-pants' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block_title = page.check_info_block_title_in_section2_block1()
            assert info_block_title == "20% OFF", "The title is not correct"

        @allure.title("TC 13.01.19 - Check the display of the text in block 1 'home-pants' in the Promo Block")
        def test_tc_13_01_19_check_info_block_text_in_section2_block1(self, driver):
            """This test checks if the info block text in section 2 block 1 'home-pants' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block_text = page.check_info_block_text_in_section2_block1()
            assert info_block_text == "Luma pants when you shop today*", "The text is not correct"

        @allure.title("TC 13.01.20 - Check the display of the sign in block 1 'home-pants' in the Promo Block")
        def test_tc_13_01_20_check_info_block_sing_in_section2_block1(self, driver):
            """This test checks if the sign in info block in section 2 block 1 'home-pants' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block_sign = page.check_info_block_sign_in_section2_block1()
            assert info_block_sign == "Shop Pants", "The text is not correct"

        @allure.title("TC 13.01.21 - Check the display of the image in block 2 'home-t-shirts' in the Promo Block")
        def test_tc_13_01_21_check_image_in_section2_block2(self, driver):
            """This test checks if the image in section 2 block 2 'home-t-shirts' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block2_image = page.check_image_in_section2_block2()
            assert block2_image == ImageUrls.SECTION_2_BLOCK_2_IMAGE_URL, "The image is not correct"

        @allure.title("TC 13.01.22 - Check the display of the info block in block 2 't-shirts' in the Promo Block")
        def test_tc_13_01_22_check_info_block_in_section2_block2(self, driver):
            """This test checks if info block in section 2 block 2 'home-t-shirts' is displayed
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block = page.check_info_block_display_in_section2_block2()
            assert info_block is True, "The element is not visible"

        @allure.title("TC 13.01.23 - Check the display of the title in block 2 'home-t-shirts' in the Promo Block")
        def test_tc_13_01_23_check_info_block_title_in_section2_block1(self, driver):
            """This test checks if the info block title in section 2 block 1 'home-t-shirts' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block_title = page.check_info_block_title_in_section2_block2()
            assert info_block_title == "Even more ways to mix and match", "The title is not correct"

        @allure.title("TC 13.01.26 - Check the display of the image in block 3 'home-erin' in the Promo Block")
        def test_tc_13_01_26_check_image_in_section2_block3(self, driver):
            """This test checks if the image in section 2 block 3 'home-erin' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block3_image = page.check_image_in_section2_block3()
            assert block3_image == ImageUrls.SECTION_2_BLOCK_3_IMAGE_URL, "The image is not correct"

        @allure.title("TC 13.01.27 - Check the display of the info block in block 3 'home-erin' in the Promo Block")
        def test_tc_13_01_27_check_info_block_in_section2_block3(self, driver):
            """This test checks if info block in section 2 block 3 'home-erin' is displayed
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block = page.check_info_block_display_in_section2_block3()
            assert info_block is True, "The element is not visible"

        @allure.title("TC 13.01.28 - Check the display of the title in block 3 'home-erin' in the Promo Block")
        def test_tc_13_01_28_check_info_block_title_in_section2_block1(self, driver):
            """This test checks if the info block title in section 2 block 3 'home-erin' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block_title = page.check_info_block_title_in_section2_block3()
            assert info_block_title == "Take it from Erin", "The title is not correct"

        @allure.title("TC 13.01.31 - Check the display of the image in block 4 'home-performance' in the Promo Block")
        def test_tc_13_01_31_check_image_in_section2_block4(self, driver):
            """This test checks if the image in section 2 block 4 'home-performance' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block4_image = page.check_image_in_section2_block4()
            assert block4_image == ImageUrls.SECTION_2_BLOCK_4_IMAGE_URL, "The image is not correct"

        @allure.title("TC 13.01.32 - Check the display of the info block in block 4 'home-performance' in the Promo "
                      "Block")
        def test_tc_13_01_32_check_info_block_in_section2_block4(self, driver):
            """This test checks if info block in section 2 block 4 'home-performance' is displayed
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block = page.check_info_block_display_in_section2_block4()
            assert info_block is True, "The element is not visible"

        @allure.title("TC 13.01.33 - Check the display of the title in block 4 'home-performance' in the Promo Block")
        def test_tc_13_01_33_check_info_block_title_in_section2_block4(self, driver):
            """This test checks if the info block title in section 2 block 4 'home-performance' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block_title = page.check_info_block_title_in_section2_block4()
            assert info_block_title == "Science meets performance", "The title is not correct"

        @allure.title("TC 13.01.36 - Check the display of the image in block 5 'home-eco' in the Promo Block")
        def test_tc_13_01_36_check_image_in_section2_block5(self, driver):
            """This test checks if the image in section 2 block 5 'home-eco' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block5_image = page.check_image_in_section2_block5()
            assert block5_image == ImageUrls.SECTION_2_BLOCK_5_IMAGE_URL, "The image is not correct"

        @allure.title("TC 13.01.37 - Check the display of the info block in block 5 'home-eco' in the Promo Block")
        def test_tc_13_01_37_check_info_block_in_section2_block5(self, driver):
            """This test checks if info block in section 2 block 5 'home-eco' is displayed
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block = page.check_info_block_display_in_section2_block5()
            assert info_block is True, "The element is not visible"

        @allure.title("TC 13.01.38 - Check the display of the title in block 5 'home-eco' in the Promo Block")
        def test_tc_13_01_38_check_info_block_title_in_section2_block5(self, driver):
            """This test checks if the info block title in section 2 block 5 'home-eco' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block_title = page.check_info_block_title_in_section2_block5()
            assert info_block_title == "Twice around, twice as nice", "The title is not correct"
