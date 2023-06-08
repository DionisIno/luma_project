"""This section contains the basic steps for running homepage tests"""

from locators.main_page_locators import MainPageLocators
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
        btn_status = self.element_is_visible(self.locators.BTN_ADD_TO_CART)
        return btn_status


class PromoBlock(BasePage):
    locators = MainPageLocators

    def check_promo_block_display(self):
        """Checks promo block display"""
        promo_block = self.element_is_visible(self.locators.PROMO_BLOCK)
        return promo_block.is_displayed()

    def check_info_block_title(self):
        """Checks the title of info-block in block 1 'home-pants'"""
        element = self.element_is_visible(self.locators.SECTION_2_BLOCK_1_INFO_BLOCK_TITLE)
        info_block_title = element.text
        return info_block_title


