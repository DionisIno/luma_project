"""This section contains the basic steps for running homepage tests"""
import time

import allure

from locators.main_page_locators import MainPageLocators
from locators.yoga_new_page_locators import YogaCollectionPageLocators
from locators.pants_promo_page_locators import PantsPromoPageLocators
from locators.tees_promo_page_locators import TeesPromoPageLocators
from locators.erin_recommends_promo_page_locators import ErinRecommendsPromoPageLocators
from locators.performance_fabrics_promo_page_locators import PerformanceFabricsPromoPageLocators
from locators.eco_friendly_promo_page_locators import EcoFriendlyPromoPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators

    def check_for_shadow_appearance_when_hovering_over_the_card(self):
        """Checks for shadows to appear when looking at a card"""
        card_item = self.element_is_visible(self.locators.PRODUCT_CARD)
        shadow_before = card_item.value_of_css_property("box-shadow")
        self.action_move_to_element(card_item)
        shadow_after = card_item.value_of_css_property("box-shadow")
        return shadow_before, shadow_after

    def check_product_card_title(self):
        """Checks product card title"""
        card_item = self.element_is_visible(self.locators.CARD_TITLE)
        text_title = card_item.text
        return text_title

    def check_the_correct_page_title_after_click_on_the_card(self):
        """
        This method gets the title text of the product card,
        click on the product card, go to the product page,
        get the title of the product and return the titles
        """
        text_before = self.get_text(self.locators.CARD_TITLE)
        self.element_is_visible(self.locators.CARD_IMG).click()
        text_after = self.get_text(self.locators.H1_TITLE)
        return text_before, text_after

    def check_card_price(self):
        """
        This method gets the price of an item
        :return: price in USD
        """
        text = self.get_text(self.locators.CARD_PRICE)
        return text

    def hover_by_item(self):
        """This method finds a visible element Product card,
        simulates a hover action by moving the cursor to it,"""
        card_item = self.element_is_visible(self.locators.PRODUCT_CARD)
        self.action_move_to_element(card_item)

    def btn_is_visible(self):
        """This method check that button Add to Cart is visible
        on the product card when hover by product"""
        self.hover_by_item()
        btn_status = self.element_is_visible(self.locators.PRODUCT_CARD_BUTTONS["add_to_card"])
        return btn_status

    @allure.step("Check the color change on hover on the Add to Cart button")
    def check_the_color_change_to_add_to_cart_button(self):
        """
        This method hovers the mouse cursor over the product card,
        hovers the mouse cursor over the add to cart button,
        and checks for the button color change
        """
        with allure.step("Get button properties before hover"):
            add_to_card_button = self.element_is_present(self.locators.PRODUCT_CARD_BUTTONS["add_to_card"])
            background_before = add_to_card_button.value_of_css_property("background-color")
        with allure.step("Hover mouse cursor on a product card"):
            card = self.element_is_visible(self.locators.PRODUCT_CARD)
            self.action_move_to_element(card)
        with allure.step("Hover mouse cursor over 'add to cart' button"):
            background_after = self.check_element_hover_style_using_js(add_to_card_button, "background-color")
        return background_before, background_after

    @allure.step("Check the cursor change on hover on the card buttons")
    def check_the_cursor_change_to_cart_buttons(self, item):
        """
        This method hovers the mouse cursor over the product card,
        hovers the mouse cursor over the add to cart button,
        and checks for the button cursor change
        """
        with allure.step("Get button properties before hover"):
            cursor_before = self.driver.execute_script("""return window.getComputedStyle(document.body).cursor;""")
        with allure.step("Hover mouse cursor on a product card"):
            card = self.element_is_visible(self.locators.PRODUCT_CARD)
            self.action_move_to_element(card)
        with allure.step("Hover mouse cursor over button"):
            cursor = self.element_is_present(self.locators.PRODUCT_CARD_BUTTONS[item])
            cursor_after = self.check_element_hover_style_using_js(cursor, "cursor")
        return cursor_before, cursor_after

    @allure.step("Check the color change on hover on the wishlist button and add to compare button")
    def check_the_color_change_my_wish_and_add_to_compare_button(self, item):
        """
        This method hovers the mouse cursor over the product card,
        hovers the mouse cursor over the wishlist button and add to compare button,
        and checks for the button color change
        """
        with allure.step("Get button properties before hover"):
            add_to_card_button = self.element_is_present(self.locators.PRODUCT_CARD_BUTTONS[item])
            color_before = add_to_card_button.value_of_css_property("color")
        with allure.step("Hover mouse cursor on a product card"):
            card = self.element_is_visible(self.locators.PRODUCT_CARD)
            self.action_move_to_element(card)
        with allure.step(f"Hover mouse cursor over '{item}' button"):
            color_after = self.check_element_hover_style_using_js(add_to_card_button, "color")
        return color_before, color_after

    @allure.step("Checking the display of an element on the screen")
    def check_element_display(self, item):
        """
        This method checks that the element is displayed on the screen.
        :return: True or False
        """
        product_card = self.element_is_visible(self.locators.PRODUCT_CARD)
        self.action_move_to_element(product_card)
        element = self.element_is_visible(self.locators.PRODUCT_CARD_BUTTONS[item])
        return element.is_displayed()

    @allure.step("Check the transition to the page my desires when clicking on the button. User is not authorized")
    def check_the_transition_to_the_page_my_wish_after_click_on_the_button(self):
        """
        This method hovers the mouse over the product card,
        clicks the add to favorites button
        and checks that the correct page has been navigated to
        User is not authorized
        """
        product_card = self.element_is_visible(self.locators.PRODUCT_CARD)
        self.action_move_to_element(product_card)
        button = self.element_is_visible(self.locators.PRODUCT_CARD_BUTTONS["add_to_wish_list"])
        self.action_move_to_element(button)
        button.click()
        error_message = self.get_error_message()
        return error_message.text

    @allure.step("Check the error message")
    def get_error_message(self):
        """
        This method check error message
        """
        error_message = self.element_is_visible(self.locators.ERROR_MESSAGE, 15)
        return error_message

    @allure.step("Check the transition to the page my desires when clicking on the button. User is not authorized")
    def check_the_transition_to_the_page_my_wish_after_click_on_the_button_user_authorized(self):
        """
        This method hovers the mouse over the product card,
        clicks the add to favorites button
        and checks that the correct page has been navigated to
        User is not authorized
        """
        card_title = self.element_is_visible(self.locators.CARD_TITLE).text
        product_card = self.element_is_visible(self.locators.PRODUCT_CARD)
        self.action_move_to_element(product_card)
        button = self.element_is_present(self.locators.PRODUCT_CARD_BUTTONS["add_to_wish_list"])
        # self.action_move_to_element(button)
        self.driver.execute_script("arguments[0].click();", button)
        # button.click()
        text = self.get_successful_message()
        # self.delete_my_wish_list()
        return text, card_title

    @allure.step("Check the error message")
    def get_successful_message(self):
        """
        This method check successful message
        """
        text = self.element_is_visible(self.locators.SUCCESSFUL_MESSAGE)
        return text.text


class PromoBlock(BasePage):
    locators = MainPageLocators
    locators1 = YogaCollectionPageLocators
    locators2 = PantsPromoPageLocators
    locators3 = TeesPromoPageLocators
    locators4 = ErinRecommendsPromoPageLocators
    locators5 = PerformanceFabricsPromoPageLocators
    locators6 = EcoFriendlyPromoPageLocators

    @allure.step("Getting of URL of the current page")
    def get_actual_url(self, driver):
        """This method allows to get URL of the current page"""
        actual_url = driver.current_url
        return actual_url

    @allure.step("Check Promo Block is present in the DOM tree")
    def check_promo_block_is_present(self):
        """Checks promo block is present in the DOM tree"""
        return self.element_is_present(self.locators.PROMO_BLOCK)

    @allure.step("Check section 1 in the Promo Block is present in the DOM tree")
    def check_section1_is_present(self):
        """Checks section 1 in the promo block is present in the DOM tree"""
        return self.element_is_present(self.locators.SECTION_1)

    @allure.step("Check section 2 in the Promo Block is present in the DOM tree")
    def check_section2_is_present(self):
        """Checks section 2 in the promo block is present in the DOM tree"""
        return self.element_is_present(self.locators.SECTION_2)

    @allure.step("Check block 1 'home-pants' in section 2 of the Promo Block is present in the DOM tree")
    def check_block1_section2_is_present(self):
        """Checks block 1 'home-pants' in section 2 of the promo block is present in the DOM tree"""
        return self.element_is_present(self.locators.SECTION_2_BLOCK_1)

    @allure.step("Check block 2 'home-t-shirts' in section 2 of the Promo Block is present in the DOM tree")
    def check_block2_section2_is_present(self):
        """Checks block 2 'home-t-shirts' in section 2 of the promo block is present in the DOM tree"""
        return self.element_is_present(self.locators.SECTION_2_BLOCK_2)

    @allure.step("Check block 3 'home-erin' in section 2 of the Promo Block is present in the DOM tree")
    def check_block3_section2_is_present(self):
        """Checks block 3 'home-erin' in section 2 of the promo block is present in the DOM tree"""
        return self.element_is_present(self.locators.SECTION_2_BLOCK_3)

    @allure.step("Check block 4 'home-performance' in section 2 of the Promo Block is present in the DOM tree")
    def check_block4_section2_is_present(self):
        """Checks block 4 'home-performance' in section 2 of the promo block is present in the DOM tree"""
        return self.element_is_present(self.locators.SECTION_2_BLOCK_4)

    @allure.step("Check block 5 'home-eco' in section 2 of the Promo Block is present in the DOM tree")
    def check_block5_section2_is_present(self):
        """Checks block 5 'home-eco' in section 2 of the promo block is present in the DOM tree"""
        return self.element_is_present(self.locators.SECTION_2_BLOCK_5)

    @allure.step("Check Promo Block display")
    def check_promo_block_display(self):
        """Checks promo block display"""
        promo_block = self.element_is_visible(self.locators.PROMO_BLOCK)
        return promo_block.is_displayed()

    @allure.step("Check the image in section 1 in the Promo Block is correct")
    def check_image_in_section1(self):
        """Checks the image in section 1 'home-main'"""
        element = self.element_is_visible(self.locators.SECTION_1_IMAGE)
        section1_image = element.get_attribute("src")
        return section1_image

    @allure.step("Check the text in section 1 in the Promo Block is correct")
    def check_info_block_text_in_section1(self):
        """Checks the text of info-block in section 1 'home-main'"""
        element = self.element_is_visible(self.locators.SECTION_1_INFO_BLOCK_TEXT)
        info_block_text = element.text
        return info_block_text

    @allure.step("Check the title in section 1 in the Promo Block is correct")
    def check_info_block_title_in_section1(self):
        """Checks the title of info-block in section 1 'home-main'"""
        element = self.element_is_visible(self.locators.SECTION_1_INFO_BLOCK_TITLE)
        info_block_title = element.text
        return info_block_title

    @allure.step("Check the section 1 display in the Promo Block")
    def check_section1_display(self):
        """Checks section 1 display"""
        section1 = self.element_is_visible(self.locators.SECTION_1)
        return section1

    @allure.step("Check the section 2 display in the Promo Block")
    def check_section2_display(self):
        """Checks section 2 display"""
        section2 = self.element_is_visible(self.locators.SECTION_2)
        return section2

    @allure.step("Check the section 2 block 1 'home-pants' display in the Promo Block")
    def check_section2_block1_display(self):
        """Checks section 2 block 1 'home-pants' display"""
        section2_block1 = self.element_is_visible(self.locators.SECTION_2_BLOCK_1)
        return section2_block1.is_displayed()

    @allure.step("Check the section 2 block 2 'home-t-shirts' display in the Promo Block")
    def check_section2_block2_display(self):
        """Checks section 2 block 2 'home-t-shirts' display"""
        section2_block2 = self.element_is_visible(self.locators.SECTION_2_BLOCK_2)
        return section2_block2.is_displayed()

    @allure.step("Check the section 2 block 3 'home-erin' display in the Promo Block")
    def check_section2_block3_display(self):
        """Checks section 2 block 3 'home-erin' display"""
        section2_block3 = self.element_is_visible(self.locators.SECTION_2_BLOCK_3)
        return section2_block3.is_displayed()

    @allure.step("Check the section 2 block 4 'home-performance' display in the Promo Block")
    def check_section2_block4_display(self):
        """Checks section 2 block 4 'home-performance' display"""
        section2_block4 = self.element_is_visible(self.locators.SECTION_2_BLOCK_4)
        return section2_block4.is_displayed()

    @allure.step("Check the section 2 block 5 'home-eco' display in the Promo Block")
    def check_section2_block5_display(self):
        """Checks section 2 block 5 'home-eco' display"""
        section2_block5 = self.element_is_visible(self.locators.SECTION_2_BLOCK_5)
        return section2_block5.is_displayed()

    @allure.step("Check the image in section 2 block 1 'home-pants' is correct in the Promo Block")
    def check_image_in_section2_block1(self):
        """Checks the image in block 1 'home-pants'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_1_IMAGE)
        block1_image = element.get_attribute("src")
        return block1_image

    @allure.step("Check the image in section 2 block 2 'home-t-shirts' is correct in the Promo Block")
    def check_image_in_section2_block2(self):
        """Checks the image in block 2 'home-t-shirts'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_2_IMAGE)
        block2_image = element.get_attribute("src")
        return block2_image

    @allure.step("Check the image in section 2 block 3 'home-erin' is correct in the Promo Block")
    def check_image_in_section2_block3(self):
        """Checks the image in block 3 'home-erin'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_3_IMAGE)
        block3_image = element.get_attribute("src")
        return block3_image

    @allure.step("Check the image in section 2 block 4 'home-performance' is correct in the Promo Block")
    def check_image_in_section2_block4(self):
        """Checks the image in block 4 'home-performance'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_4_IMAGE)
        block4_image = element.get_attribute("src")
        return block4_image

    @allure.step("Check the image in section 2 block 5 'home-eco' is correct in the Promo Block")
    def check_image_in_section2_block5(self):
        """Checks the image in block 5 'home-eco'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_5_IMAGE)
        block5_image = element.get_attribute("src")
        return block5_image

    @allure.step("Check display of info block in section 2 block 1 'home-pants' in the Promo Block")
    def check_info_block_display_in_section2_block1(self):
        """Checks the info block 1 'home-pants' display in section 2 of promo block under header"""
        info_block = self.element_is_visible(self.locators.SECTION_2_BLOCK_1_INFO_BLOCK)
        return info_block.is_displayed()

    @allure.step("Check display of info block in section 2 block 2 'home-t-shirts' in the Promo Block")
    def check_info_block_display_in_section2_block2(self):
        """Checks the info block 2 'home-t-shirts' display in section 2 of promo block under header"""
        info_block = self.element_is_visible(self.locators.SECTION_2_BLOCK_2_INFO_BLOCK)
        return info_block.is_displayed()

    @allure.step("Check display of info block in section 2 block 3 'home-erin' in the Promo Block")
    def check_info_block_display_in_section2_block3(self):
        """Checks the info block 3 'home-erin' display in section 2 of promo block under header"""
        info_block = self.element_is_visible(self.locators.SECTION_2_BLOCK_3_INFO_BLOCK)
        return info_block.is_displayed()

    @allure.step("Check display of info block in section 2 block 4 'home-performance' in the Promo Block")
    def check_info_block_display_in_section2_block4(self):
        """Checks the info block 4 'home-performance' display in section 2 of promo block under header"""
        info_block = self.element_is_visible(self.locators.SECTION_2_BLOCK_4_INFO_BLOCK)
        return info_block.is_displayed()

    @allure.step("Check display of info block in section 2 block 5 'home-eco' in the Promo Block")
    def check_info_block_display_in_section2_block5(self):
        """Checks the info block 5 'home-eco' display in section 2 of promo block under header"""
        info_block = self.element_is_visible(self.locators.SECTION_2_BLOCK_5_INFO_BLOCK)
        return info_block.is_displayed()

    @allure.step("Check the title of info block in section 2 block 1 'home-pants' in the Promo Block is correct")
    def check_info_block_title_in_section2_block1(self):
        """Checks the title of info-block in block 1 'home-pants'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_1_INFO_BLOCK_TITLE)
        info_block_title = element.text
        return info_block_title

    @allure.step("Check the title of info block in section 2 block 2 'home-t-shirts' in the Promo Block is correct")
    def check_info_block_title_in_section2_block2(self):
        """Checks the title of info-block in block 2 'home-t-shirts'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_2_INFO_BLOCK_TITLE)
        info_block_title = element.text
        return info_block_title

    @allure.step("Check the title of info block in section 2 block 3 'home-erin' in the Promo Block is correct")
    def check_info_block_title_in_section2_block3(self):
        """Checks the title of info-block in block 3 'home-erin'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_3_INFO_BLOCK_TITLE)
        info_block_title = element.text
        return info_block_title

    @allure.step("Check the title of info block in section 2 block 4 'home-performance' in the Promo Block is correct")
    def check_info_block_title_in_section2_block4(self):
        """Checks the title of info-block in block 4 'home-performance'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_4_INFO_BLOCK_TITLE)
        info_block_title = element.text
        return info_block_title

    @allure.step("Check the title of info block in section 2 block 5 'home-eco' in the Promo Block is correct")
    def check_info_block_title_in_section2_block5(self):
        """Checks the title of info-block in block 5 'home-eco'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_5_INFO_BLOCK_TITLE)
        info_block_title = element.text
        return info_block_title

    @allure.step("Check the text of info block in section 2 block 1 'home-pants' in the Promo Block is correct")
    def check_info_block_text_in_section2_block1(self):
        """Checks the text of info-block in block 1 'home-pants'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_1_INFO_BLOCK_TEXT)
        info_block_text = element.text
        return info_block_text

    @allure.step("Check the text of info block in section 2 block 2 'home-t-shirts' in the Promo Block is correct")
    def check_info_block_text_in_section2_block2(self):
        """Checks the text of info-block in block 2 'home-t-shirts'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_2_INFO_BLOCK_TEXT)
        info_block_text = element.text
        return info_block_text

    @allure.step("Check the text of info block in section 2 block 3 'home-erin' in the Promo Block is correct")
    def check_info_block_text_in_section2_block3(self):
        """Checks the text of info-block in block 3 'home-erin'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_3_INFO_BLOCK_TEXT)
        info_block_text = element.text
        return info_block_text

    @allure.step("Check the text of info block in section 2 block 4 'home-performance' in the Promo Block is correct")
    def check_info_block_text_in_section2_block4(self):
        """Checks the text of info-block in block 4 'home-performance'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_4_INFO_BLOCK_TEXT)
        info_block_text = element.text
        return info_block_text

    @allure.step("Check the text of info block in section 2 block 5 'home-eco' in the Promo Block is correct")
    def check_info_block_text_in_section2_block5(self):
        """Checks the text of info-block in block 5 'home-eco'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_5_INFO_BLOCK_TEXT)
        info_block_text = element.text
        return info_block_text

    @allure.step("Check the sign of info block in section 2 block 1 'home-pants' in the Promo Block is correct")
    def check_info_block_sign_in_section2_block1(self):
        """Checks the sign in info-block in block 1 'home-pants'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_1_INFO_BLOCK_SIGN)
        info_block_sign = element.text
        return info_block_sign

    @allure.step("Check the sign of info block in section 2 block 2 'home-t-shirts' in the Promo Block is correct")
    def check_info_block_sign_in_section2_block2(self):
        """Checks the sign in info-block in block 2 'home-t-shirts'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_2_INFO_BLOCK_SIGN)
        info_block_sign = element.text
        return info_block_sign

    @allure.step("Check the sign of info block in section 2 block 3 'home-erin' in the Promo Block is correct")
    def check_info_block_sign_in_section2_block3(self):
        """Checks the sign in info-block in block 3 'home-erin'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_3_INFO_BLOCK_SIGN)
        info_block_sign = element.text
        return info_block_sign

    @allure.step("Check the sign of info block in section 2 block 4 'home-performance' in the Promo Block is correct")
    def check_info_block_sign_in_section2_block4(self):
        """Checks the sign in info-block in block 4 'home-performance'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_4_INFO_BLOCK_SIGN)
        info_block_sign = element.text
        return info_block_sign

    @allure.step("Check the sign of info block in section 2 block 5 'home-eco' in the Promo Block is correct")
    def check_info_block_sign_in_section2_block5(self):
        """Checks the sign in info-block in block 5 'home-eco'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_5_INFO_BLOCK_SIGN)
        info_block_sign = element.text
        return info_block_sign

    @allure.step("Check the link in section 1 in the Promo Block leads to the correct page")
    def check_section1_link(self):
        """Checks the link in section 1 leads to the correct page"""
        section1 = self.element_is_visible(self.locators.SECTION_1)
        link = section1.click()
        return link

    @allure.step("Check the title of opened page New Luma Yoga Collection is displayed")
    def check_page1_title_display(self):
        """Checks the title of opened page New Luma Yoga Collection is displayed"""
        element = self.element_is_visible(self.locators1.NEW_LUMA_YOGA_COLLECTION_TITLE)
        page_title = element.text
        return page_title

    @allure.step("Check the link in section 2 block 1 'home-pants' in the Promo Block leads to the correct page")
    def check_section2_block1_link(self):
        """Checks the link in section 2 block 1 'home-pants' leads to the correct page"""
        section2_block1 = self.element_is_visible(self.locators.SECTION_2_BLOCK_1)
        link = section2_block1.click()
        return link

    @allure.step("Check the title of opened page Pants is displayed")
    def check_page2_title_display(self):
        """Checks the title of opened page Pants is displayed"""
        element = self.element_is_visible(self.locators2.PANTS_PROMO_TITLE)
        page_title = element.text
        return page_title

    @allure.step("Check the link in section 2 block 2 'home-t-shirts' in the Promo Block leads to the correct page")
    def check_section2_block2_link(self):
        """Checks the link in section 2 block 2 'home-t-shirts' leads to the correct page"""
        section2_block2 = self.element_is_visible(self.locators.SECTION_2_BLOCK_2)
        link = section2_block2.click()
        return link

    @allure.step("Check the title of opened page Tees is displayed")
    def check_page3_title_display(self):
        """Checks the title of opened page Tees is displayed"""
        element = self.element_is_visible(self.locators3.TEES_PROMO_TITLE)
        page_title = element.text
        return page_title

    @allure.step("Check the link in section 2 block 3 'home-erin' in the Promo Block leads to the correct page")
    def check_section2_block3_link(self):
        """Checks the link in section 2 block 3 'home-erin' leads to the correct page"""
        section2_block3 = self.element_is_visible(self.locators.SECTION_2_BLOCK_3)
        link = section2_block3.click()
        return link

    @allure.step("Check the title of opened page Erin Recommends is displayed")
    def check_page4_title_display(self):
        """Checks the title of opened page Erin Recommends is displayed"""
        element = self.element_is_visible(self.locators4.ERIN_RECOMMENDS_PROMO_TITLE)
        page_title = element.text
        return page_title

    @allure.step("Check the link in section 2 block 4 'home-performance' in the Promo Block leads to the correct page")
    def check_section2_block4_link(self):
        """Checks the link in section 2 block 4 'home-performance' leads to the correct page"""
        section2_block4 = self.element_is_visible(self.locators.SECTION_2_BLOCK_4)
        link = section2_block4.click()
        return link

    @allure.step("Check the title of opened page Performance Fabrics is displayed")
    def check_page5_title_display(self):
        """Checks the title of opened page Performance Fabrics is displayed"""
        element = self.element_is_visible(self.locators5.PERFORMANCE_FABRICS_PROMO_TITLE)
        page_title = element.text
        return page_title

    @allure.step("Check the link in section 2 block 5 'home-eco' in the Promo Block leads to the correct page")
    def check_section2_block5_link(self):
        """Checks the link in section 2 block 5 'home-eco' leads to the correct page"""
        section2_block5 = self.element_is_visible(self.locators.SECTION_2_BLOCK_5)
        link = section2_block5.click()
        return link

    @allure.step("Check the title of opened page Eco Friendly is displayed")
    def check_page6_title_display(self):
        """Checks the title of opened page Eco Friendly is displayed"""
        element = self.element_is_visible(self.locators6.ECO_FRIENDLY_PROMO_TITLE)
        page_title = element.text
        return page_title
