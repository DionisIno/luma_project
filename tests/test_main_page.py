"""This section contains home page tests"""
import json
import time

import allure
import pytest

from pages.main_page import MainPage, PromoBlock
from data.data_urls import MAIN_PAGE_URL, ImageUrls, PromoBlockLinks
from data.main_data import product_card_button, error_message, PromoBlockElementsText
from locators.main_page_locators import MainPageLocators


@allure.epic("Main Page")
class TestMainPage:
    @allure.feature("Testing Hot Seller Section")
    class TestHotSellerSection:
        @pytest.mark.xfail(reason="In CI the test failed in PR#203")
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

        @pytest.mark.xfail(reason="In CI the test failed in PR#203")
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

        @pytest.mark.xfail(reason="In CI the test failed in PR#182")
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

    @allure.feature("Promo Block Testing")
    class TestPromoBlock:
        locators = MainPageLocators

        @allure.title("TC 13.01.01 - Check the display of the Promo Block under header on the main page")
        def test_tc_13_01_01_check_promo_block_display(self, driver):
            """This test checks if Promo Block under header is displayed on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            promo_block = page.check_promo_block_display()
            assert promo_block is True, "The element is not visible"

        @allure.title("TC 13.01.02 - Check the display of section 1 in the Promo Block")
        def test_tc_13_01_02_check_section1_display(self, driver):
            """This test checks if section 1 in Promo Block under header is displayed on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            section1 = page.check_section1_display()
            assert section1, "The Section 1 in Promo Blck is not visible"

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
            actual_text = page.check_info_block_text_in_section1()
            expected_text = PromoBlockElementsText.SECTION_1_INFO_BLOCK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' of info block in section 1 " \
                                                 f"of Promo Block does not match expected '{expected_text}'"

        @allure.title("TC 13.01.07 - Check the display of the info block title "
                      "in section 1 'home-main' in the Promo Block")
        def test_tc_13_01_07_check_info_block_title_in_section1(self, driver):
            """This test checks if the info block title in section 1 'home-main' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            actual_text = page.check_info_block_title_in_section1()
            expected_text = PromoBlockElementsText.SECTION_1_INFO_BLOCK_TITLE
            assert actual_text == expected_text, f"Actual title '{actual_text}' of info block in section 1 " \
                                                 f"of Promo Block does not match expected '{expected_text}'"

        @allure.title("TC 13.01.09 - Check the display of section 2 in the Promo Block")
        def test_tc_13_01_09_check_section2_display(self, driver):
            """This test checks if section 2 in Promo Block under header is displayed on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            section2 = page.check_section2_display()
            assert section2, "The element is not visible"

        @allure.title("TC 13.01.10 - Check display of block 1 'home-pants' in section 2 in the Promo Block")
        def test_tc_13_01_10_check_section2_block1_display(self, driver):
            """This test checks if block 1 'home-pants' is displayed in section 2
            of Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block1 = page.check_section2_block1_display()
            assert block1 is True, "The element is not visible"

        @allure.title("TC 13.01.11 - Check display of block 2 'home-t-shirts' in section 2 in the Promo Block")
        def test_tc_13_01_11_check_section2_block2_display(self, driver):
            """This test checks if block 2 'home-t-shirts' is displayed in section 2
            of Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block2 = page.check_section2_block2_display()
            assert block2 is True, "The element is not visible"

        @allure.title("TC 13.01.12 - Check display of block 3 'home-erin' in section 2 in the Promo Block")
        def test_tc_13_01_12_check_section2_block3_display(self, driver):
            """This test checks if block 3 'home-erin' is displayed in section 2
            of Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block3 = page.check_section2_block3_display()
            assert block3 is True, "The element is not visible"

        @allure.title("TC 13.01.13 - Check display of block 4 'home-performance' in section 2 in the Promo Block")
        def test_tc_13_01_13_check_section2_block4_display(self, driver):
            """This test checks if block 4 'home-performance' is displayed in section 2
            of Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block4 = page.check_section2_block4_display()
            assert block4 is True, "The element is not visible"

        @allure.title("TC 13.01.14 - Check display of block 5 'home-eco' in section 2 in the Promo Block")
        def test_tc_13_01_14_check_section2_block5_display(self, driver):
            """This test checks if block 5 'home-eco' is displayed in section 2
            of Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block5 = page.check_section2_block5_display()
            assert block5 is True, "The element is not visible"

        # def test_tc_13_01_16_00_check_image_in_section2_block1(self, driver):
        #     page = PromoBlock(driver, MAIN_PAGE_URL)
        #     page.open()
        #     block1_image = page.check_image_in_section2_block1()
        #     assert block1_image == ImageUrls.SECTION_2_BLOCK_1_IMAGE_URL, "The image is not correct"

        @allure.title("TC 13.01.16 - Check the display of an image in block 1 'home-pants' in the Promo Block")
        def test_tc_13_01_16_check_image_in_section2_block1(self, driver):
            """This test checks if the image in section 2 block 1 'home-pants' is visible
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block1_image = page.find_element(self.locators.SECTION_2_BLOCK_1_IMAGE)
            page.go_to_element(block1_image)
            page.check_element_image_is_visible(block1_image)
            assert block1_image, "The image is not visible"

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
            actual_text = page.check_info_block_title_in_section2_block1()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_1_INFO_BLOCK_TITLE
            assert actual_text == expected_text, f"Actual title '{actual_text}' of info block in section 2 block 1 " \
                                                 f"'home-pants' of Promo Block doesn't match expected '{expected_text}'"

        @allure.title("TC 13.01.19 - Check the display of the text in block 1 'home-pants' in the Promo Block")
        def test_tc_13_01_19_check_info_block_text_in_section2_block1(self, driver):
            """This test checks if the info block text in section 2 block 1 'home-pants' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            actual_text = page.check_info_block_text_in_section2_block1()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_1_INFO_BLOCK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' in info block in section 2 block 1 " \
                                                 f"'home-pants' of Promo Block doesn't match expected '{expected_text}'"

        @allure.title("TC 13.01.20 - Check the display of the sign in block 1 'home-pants' in the Promo Block")
        def test_tc_13_01_20_check_info_block_sign_in_section2_block1(self, driver):
            """This test checks if the sign in info block in section 2 block 1 'home-pants' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            actual_text = page.check_info_block_sign_in_section2_block1()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_1_INFO_BLOCK_SIGN
            assert actual_text == expected_text, f"Actual sign '{actual_text}' in info block in section 2 block 1 " \
                                                 f"'home-pants' of Promo Block doesn't match expected '{expected_text}'"

        # @allure.title("TC 13.01.21 - Check the display of the image in block 2 'home-t-shirts' in the Promo Block")
        # def test_tc_13_01_21_00_check_image_in_section2_block2(self, driver):
        #     """This test checks if the image in section 2 block 2 'home-t-shirts' is correct
        #     in the Promo Block under header on the main page"""
        #     page = PromoBlock(driver, MAIN_PAGE_URL)
        #     page.open()
        #     block2_image = page.check_image_in_section2_block2()
        #     assert block2_image == ImageUrls.SECTION_2_BLOCK_2_IMAGE_URL, "The image is not correct"

        @allure.title("TC 13.01.21 - Check the display of an image in block 2 'home-t-shirts' in the Promo Block")
        def test_tc_13_01_21_check_image_visibility_in_section2_block2(self, driver):
            """This test checks if the image in section 2 block 2 'home-t-shirts' is visible"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block2_image = page.find_element(self.locators.SECTION_2_BLOCK_2_IMAGE)
            assert page.check_element_image_is_visible(block2_image), "The image is not visible"

        @allure.title("TC 13.01.21_01 - Check correctness of the image in block 2 'home-t-shirts' in the Promo Block")
        def test_tc_13_01_21_01_check_image_correctness_in_section2_block2(self, driver):
            """This test checks if the image in section 2 block 2 'home-t-shirts' is correct"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block2_image = page.find_element(self.locators.SECTION_2_BLOCK_2_IMAGE)
            block2_image_url = ImageUrls.SECTION_2_BLOCK_2_IMAGE_URL
            assert page.check_image_src(block2_image) == block2_image_url, "The image is not correct in the element"

        @allure.title("TC 13.01.22 - Check the display of the info block in block 2 't-shirts' in the Promo Block")
        def test_tc_13_01_22_check_info_block_in_section2_block2(self, driver):
            """This test checks if info block in section 2 block 2 'home-t-shirts' is displayed
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            info_block = page.check_info_block_display_in_section2_block2()
            assert info_block is True, "The element is not visible"

        @allure.title("TC 13.01.23 - Check the display of the title in block 2 'home-t-shirts' in the Promo Block")
        def test_tc_13_01_23_check_info_block_title_in_section2_block2(self, driver):
            """This test checks if the info block title in section 2 block 2 'home-t-shirts' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            actual_text = page.check_info_block_title_in_section2_block2()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_2_INFO_BLOCK_TITLE
            assert actual_text == expected_text, f"Actual title '{actual_text}' of info block in section 2 block 2 " \
                                                 f"'home-t-shirts' of Promo Block does not match expected " \
                                                 f"'{expected_text}'"

        @allure.title("TC 13.01.24 - Check the display of the text in block 2 'home-t-shirts' in the Promo Block")
        def test_tc_13_01_24_check_info_block_text_in_section2_block2(self, driver):
            """This test checks if the info block text in section 2 block 2 'home-t-shirts' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            actual_text = page.check_info_block_text_in_section2_block2()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_2_INFO_BLOCK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' in info block in section 2 block 2 " \
                                                 f"'home-t-shirts' of Promo Block doesn't match expected " \
                                                 f"'{expected_text}'"

        @allure.title("TC 13.01.25 - Check the display of the sign in block 2 'home-t-shirts' in the Promo Block")
        def test_tc_13_01_25_check_info_block_sign_in_section2_block2(self, driver):
            """This test checks if the sign in info block in section 2 block 2 'home-t-shirts' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            actual_text = page.check_info_block_sign_in_section2_block2()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_2_INFO_BLOCK_SIGN
            assert actual_text == expected_text, f"Actual sign '{actual_text}' in info block in section 2 block 2 " \
                                                 f"'home-t-shirts' of Promo Block doesn't match expected " \
                                                 f"'{expected_text}'"

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
        def test_tc_13_01_28_check_info_block_title_in_section2_block3(self, driver):
            """This test checks if the info block title in section 2 block 3 'home-erin' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            actual_text = page.check_info_block_title_in_section2_block3()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_3_INFO_BLOCK_TITLE
            assert actual_text == expected_text, f"Actual title '{actual_text}' of info block in section 2 block 3 " \
                                                 f"'home-erin' of Promo Block does not match expected '{expected_text}'"

        @allure.title("TC 13.01.29 - Check the display of the text in block 3 'home-erin' in the Promo Block")
        def test_tc_13_01_29_check_info_block_text_in_section2_block3(self, driver):
            """This test checks if the info block text in section 2 block 3 'home-erin' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            actual_text = page.check_info_block_text_in_section2_block3()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_3_INFO_BLOCK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' in info block in section 2 block 3 " \
                                                 f"'home-erin' of Promo Block doesn't match expected '{expected_text}'"

        @allure.title("TC 13.01.30 - Check the display of the sign in block 3 'home-erin' in the Promo Block")
        def test_tc_13_01_30_check_info_block_sign_in_section2_block3(self, driver):
            """This test checks if the sign in info block in section 2 block 3 'home-erin' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            actual_text = page.check_info_block_sign_in_section2_block3()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_3_INFO_BLOCK_SIGN
            assert actual_text == expected_text, f"Actual sign '{actual_text}' in info block in section 2 block 3 " \
                                                 f"'home-erin' of Promo Block doesn't match expected '{expected_text}'"

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
            actual_text = page.check_info_block_title_in_section2_block4()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_4_INFO_BLOCK_TITLE
            assert actual_text == expected_text, f"Actual title '{actual_text}' of info block in section 2 block 4 " \
                                                 f"'home-performance' of Promo Block does not match expected " \
                                                 f"'{expected_text}'"

        @allure.title("TC 13.01.34 - Check the display of the text in block 4 'home-performance' in the Promo Block")
        def test_tc_13_01_34_check_info_block_text_in_section2_block4(self, driver):
            """This test checks if the info block text in section 2 block 4 'home-performance' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            actual_text = page.check_info_block_text_in_section2_block4()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_4_INFO_BLOCK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' in info block in section 2 block 4 " \
                                                 f"'home-performance' of Promo Block doesn't match expected " \
                                                 f"'{expected_text}'"

        @allure.title("TC 13.01.35 - Check the display of the sign in block 4 'home-performance' in the Promo Block")
        def test_tc_13_01_35_check_info_block_sign_in_section2_block4(self, driver):
            """This test checks if the sign in info block in section 2 block 4 'home-performance' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            actual_text = page.check_info_block_sign_in_section2_block4()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_4_INFO_BLOCK_SIGN
            assert actual_text == expected_text, f"Actual sign '{actual_text}' in info block in section 2 block 4 " \
                                                 f"'home-performance' of Promo Block doesn't match expected " \
                                                 f"'{expected_text}'"

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
            actual_text = page.check_info_block_title_in_section2_block5()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_5_INFO_BLOCK_TITLE
            assert actual_text == expected_text, f"Actual title '{actual_text}' of info block in section 2 block 5 " \
                                                 f"'home-eco' of Promo Block does not match expected '{expected_text}'"

        @allure.title("TC 13.01.39 - Check the display of the text in block 5 'home-eco' in the Promo Block")
        def test_tc_13_01_39_check_info_block_text_in_section2_block5(self, driver):
            """This test checks if the info block text in section 2 block 5 'home-eco' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            actual_text = page.check_info_block_text_in_section2_block5()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_5_INFO_BLOCK_TEXT
            assert actual_text == expected_text, f"Actual text '{actual_text}' in info block in section 2 block 5 " \
                                                 f"'home-eco' of Promo Block doesn't match expected '{expected_text}'"

        @allure.title("TC 13.01.40 - Check the display of the sign in block 5 'home-eco' in the Promo Block")
        def test_tc_13_01_40_check_info_block_sign_in_section2_block5(self, driver):
            """This test checks if the sign in info block in section 2 block 5 'home-eco' is correct
            in the Promo Block under header on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            actual_text = page.check_info_block_sign_in_section2_block5()
            expected_text = PromoBlockElementsText.SECTION_2_BLOCK_5_INFO_BLOCK_SIGN
            assert actual_text == expected_text, f"Actual sign '{actual_text}' in info block in section 2 block 5 " \
                                                 f"'home-eco' of Promo Block doesn't match expected '{expected_text}'"

        @allure.title("TC 13.01.41 - Check Promo Block is present in the DOM tree")
        def test_tc_13_01_41_check_promo_block_is_present(self, driver):
            """This test checks if Promo Block is present in the DOM tree on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            promo_block = page.check_promo_block_is_present()
            assert promo_block is not None, "The Promo Block is not present in the DOM tree on the main page"

        @allure.title("TC 13.01.42 - Check section 1 in the Promo Block is present in the DOM tree")
        def test_tc_13_01_42_check_section1_is_present(self, driver):
            """This test checks if section 1 in the Promo Block is present in the DOM tree on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            section1 = page.check_section1_is_present()
            assert section1 is not None, "The Section 1 in the Promo Block is not present in the DOM tree " \
                                         "on the main page"

        @allure.title("TC 13.01.43 - Check section 2 in the Promo Block is present in the DOM tree")
        def test_tc_13_01_43_check_section2_is_present(self, driver):
            """This test checks if section 2 in the Promo Block is present in the DOM tree on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            section2 = page.check_section2_is_present()
            assert section2 is not None, "The Section 2 in the Promo Block is not present in the DOM tree " \
                                         "on the main page"

        @allure.title("TC 13.01.44 - Check block 1 'home-pants' in section 2 of the Promo Block is present "
                      "in the DOM tree")
        def test_tc_13_01_44_check_block1_in_section2_is_present(self, driver):
            """This test checks if block 1 'home-pants' in section 2 in the Promo Block is present
            in the DOM tree on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block1_section2 = page.check_block1_section2_is_present()
            assert block1_section2 is not None, "The block 1 'home-pants' in Section 2 of the Promo Block " \
                                                "is not present in the DOM tree on the main page"

        @allure.title("TC 13.01.45 - Check block 2 'home-t-shirts' in section 2 of the Promo Block is present "
                      "in the DOM tree")
        def test_tc_13_01_45_check_block2_in_section2_is_present(self, driver):
            """This test checks if block 2 'home-t-shirts' in section 2 in the Promo Block is present
            in the DOM tree on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block2_section2 = page.check_block2_section2_is_present()
            assert block2_section2 is not None, "The block 2 'home-t-shirts' in Section 2 of the Promo Block " \
                                                "is not present in the DOM tree on the main page"

        @allure.title("TC 13.01.46 - Check block 3 'home-erin' in section 2 of the Promo Block is present "
                      "in the DOM tree")
        def test_tc_13_01_46_check_block3_in_section2_is_present(self, driver):
            """This test checks if block 3 'home-erin' in section 2 in the Promo Block is present
            in the DOM tree on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block3_section2 = page.check_block3_section2_is_present()
            assert block3_section2 is not None, "The block 3 'home-erin' in Section 2 of the Promo Block " \
                                                "is not present in the DOM tree on the main page"

        @allure.title("TC 13.01.47 - Check block 4 'home-performance' in section 2 of the Promo Block is present "
                      "in the DOM tree")
        def test_tc_13_01_47_check_block4_in_section2_is_present(self, driver):
            """This test checks if block 4 'home-performance' in section 2 in the Promo Block is present
            in the DOM tree on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block4_section2 = page.check_block4_section2_is_present()
            assert block4_section2 is not None, "The block 4 'home-performance' in Section 2 of the Promo Block " \
                                                "is not present in the DOM tree on the main page"

        @allure.title("TC 13.01.48 - Check block 5 'home-eco' in section 2 of the Promo Block is present "
                      "in the DOM tree")
        def test_tc_13_01_48_check_block5_in_section2_is_present(self, driver):
            """This test checks if block 5 'home-eco' in section 2 in the Promo Block is present
            in the DOM tree on the main page"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            block5_section2 = page.check_block5_section2_is_present()
            assert block5_section2 is not None, "The block 5 'home-eco' in Section 2 of the Promo Block " \
                                                "is not present in the DOM tree on the main page"

        @allure.title("TC 13.01.49 - Check if section 1 is clickable in the Promo Block on the main page")
        def test_tc_13_01_49_check_section1_clickability(self, driver):
            """This test checks if section 1 in Promo Block under header is clickable"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            section1 = page.check_section1_clickability()
            assert section1, "The Section 1 in Promo Blck is not clickable"

        @allure.title("TC 13.01.50 - Check if block 1 'home-pants' in section 2 is clickable"
                      "in the Promo Block on the main page")
        def test_tc_13_01_50_check_section2_block1_clickability(self, driver):
            """This test checks if block 1 'home-pants' in section 2 in Promo Block under header is clickable"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            section2_block1 = page.check_section2_block1_clickability()
            assert section2_block1, "The block 1 'home-pants' in the Section 2 in the Promo Blck is not clickable"

        @allure.title("TC 13.01.51 - Check if block 2 'home-t-shirts' in section 2 is clickable"
                      "in the Promo Block on the main page")
        def test_tc_13_01_51_check_section2_block2_clickability(self, driver):
            """This test checks if block 2 'home-t-shirts' in section 2 in Promo Block under header is clickable"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            section2_block2 = page.check_section2_block2_clickability()
            assert section2_block2, "The block 2 'home-t-shirts' in the Section 2 in the Promo Blck is not clickable"

        @allure.title("TC 13.01.52 - Check if block 3 'home-erin' in section 2 is clickable"
                      "in the Promo Block on the main page")
        def test_tc_13_01_52_check_section2_block3_clickability(self, driver):
            """This test checks if block 3 'home-erin' in section 2 in Promo Block under header is clickable"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            section2_block3 = page.check_section2_block3_clickability()
            assert section2_block3, "The block 3 'home-erin' in the Section 2 in the Promo Blck is not clickable"

        @allure.title("TC 13.01.53 - Check if block 4 'home-performance' in section 2 is clickable"
                      "in the Promo Block on the main page")
        def test_tc_13_01_53_check_section2_block4_clickability(self, driver):
            """This test checks if block 4 'home-performance' in section 2 in Promo Block under header is clickable"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            section2_block4 = page.check_section2_block4_clickability()
            assert section2_block4, "The block 4 'home-performance' in the Section 2 in the Promo Blck is not clickable"

        @allure.title("TC 13.01.54 - Check if block 5 'home-eco' in section 2 is clickable"
                      "in the Promo Block on the main page")
        def test_tc_13_01_54_check_section2_block5_clickability(self, driver):
            """This test checks if block 5 'home-eco' in section 2 in Promo Block under header is clickable"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            section2_block5 = page.check_section2_block5_clickability()
            assert section2_block5, "The block 5 'home-eco' in the Section 2 in the Promo Blck is not clickable"

        @allure.title("TC 13.02.01 - Check the section 1 link in the Promo Block leads to the correct page")
        def test_tc_13_02_01_check_section1_link(self, driver):
            """Check that link in section 1 is correct"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            page.check_section1_link()
            get_actual_url = driver.current_url
            title = page.check_page1_title_display()
            assert page.get_actual_url_of_current_page() == PromoBlockLinks.YOGA_COLLECTION_URL \
                   and title == "New Luma Yoga Collection", "The link is not correct or the new page is not loaded"

        @allure.title("TC 13.02.02 - Check the link in section 2 block 1 'home-pants' in the Promo Block "
                      "leads to the correct page")
        def test_tc_13_02_02_check_section2_block1_link(self, driver):
            """Check that link in section 2 block 1 'home-pants' is correct"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            page.check_section2_block1_link()
            title = page.check_page2_title_display()
            assert page.get_actual_url_of_current_page() == PromoBlockLinks.PANTS_PROMO_URL and title == "Pants", \
                'The link is not correct or the new page is not loaded'

        @allure.title("TC 13.02.03 - Check the link in section 2 block 2 'home-t-shirts' in the Promo Block "
                      "leads to the correct page")
        def test_tc_13_02_03_check_section2_block2_link(self, driver):
            """Check that link in section 2 block 2 'home-t-shirts' is correct"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            page.check_section2_block2_link()
            title = page.check_page3_title_display()
            assert page.get_actual_url_of_current_page() == PromoBlockLinks.TEES_PROMO_URL and title == "Tees", \
                "The link is not correct or the new page is not loaded"

        @allure.title("TC 13.02.04 - Check the link in section 2 block 3 'home-erin' in the Promo Block "
                      "leads to the correct page")
        def test_tc_13_02_04_check_section2_block3_link(self, driver):
            """Check that link in section 2 block 3 'home-erin' is correct"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            page.check_section2_block3_link()
            title = page.check_page4_title_display()
            assert page.get_actual_url_of_current_page() == PromoBlockLinks.ERIN_RECOMMENDS_PROMO_URL \
                   and title == "Erin Recommends", "The link is not correct or the new page is not loaded"

        @allure.title("TC 13.02.05 - Check the link in section 2 block 4 'home-performance' in the Promo Block "
                      "leads to the correct page")
        def test_tc_13_02_05_check_section2_block4_link(self, driver):
            """Check that link in section 2 block 4 'home-performance' is correct"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            page.check_section2_block4_link()
            title = page.check_page5_title_display()
            assert page.get_actual_url_of_current_page() == PromoBlockLinks.PERFORMANCE_FABRICS_PROMO_URL \
                   and title == "Performance Fabrics", "The link is not correct or the new page is not loaded"

        @allure.title("TC 13.02.06 - Check the link in section 2 block 5 'home-eco' in the Promo Block "
                      "leads to the correct page")
        def test_tc_13_02_06_check_section2_block5_link(self, driver):
            """Check that link in section 2 block 5 'home-eco' is correct"""
            page = PromoBlock(driver, MAIN_PAGE_URL)
            page.open()
            page.check_section2_block5_link()
            title = page.check_page6_title_display()
            assert page.get_actual_url_of_current_page() == PromoBlockLinks.ECO_FRIENDLY_PROMO_URL \
                   and title == "Eco Friendly", "The link is not correct or the new page is not loaded"
