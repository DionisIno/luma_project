"""This section contains main page locators"""
import random

from selenium.webdriver.common.by import By


class MainPageLocators:
    elem = random.randint(1, 6)

    # Hot Seller section
    CARD_TITLE = (By.CSS_SELECTOR, f"li[class='product-item']:nth-child({elem})  strong[class='product-item-name']")
    PRODUCT_CARD = (By.CSS_SELECTOR, f"li[class='product-item']:nth-child({elem}) div[class='product-item-info']")
    CARD_IMG = (By.CSS_SELECTOR, f"li[class='product-item']:nth-child({elem}) img[class='product-image-photo']")
    H1_TITLE = (By.CSS_SELECTOR, "h1[class='page-title']")
    CARD_PRICE = (By.CSS_SELECTOR, f"li[class='product-item']:nth-child({elem}) span[class='price']")
    PRODUCT_CARD_BUTTONS = {"add_to_card": (By.CSS_SELECTOR, f"li[class='product-item']:nth-child({elem}) button["
                                                             f"class='action tocart primary']"),
                            "add_to_wish_list": (By.CSS_SELECTOR, f"li[class='product-item']:nth-child({elem}) a["
                                                                  f"data-action='add-to-wishlist']"),
                            "add_to_compare": (By.CSS_SELECTOR, f"li[class='product-item']:nth-child({elem}) a["
                                                                f"class='action tocompare']")}
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div[class='message-error error message']")
    SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, "div[data-ui-id='message-success']")

    # Promo Block
    PROMO_BLOCK = (By.CSS_SELECTOR, ".blocks-promo")
    SECTION_1_IMAGE = (By.CSS_SELECTOR, '.home-main img')
    SECTION_1_INFO_BLOCK_TEXT = (By.CSS_SELECTOR, '.home-main .info')
    SECTION_1_INFO_BLOCK_TITLE = (By.CSS_SELECTOR, '.home-main .title')
    SECTION_2 = (By.CSS_SELECTOR, '.blocks-promo > div')
    SECTION_2_BLOCK_1 = (By.CSS_SELECTOR, '.home-pants')
    SECTION_2_BLOCK_1_IMAGE = (By.CSS_SELECTOR, ".home-pants img")
    SECTION_2_BLOCK_1_INFO_BLOCK = (By.CSS_SELECTOR, ".home-pants .content")
    SECTION_2_BLOCK_1_INFO_BLOCK_SIGN = (By.CSS_SELECTOR, ".home-pants .content .icon")
    SECTION_2_BLOCK_1_INFO_BLOCK_TEXT = (By.CSS_SELECTOR, ".home-pants .content .info")
    SECTION_2_BLOCK_1_INFO_BLOCK_TITLE = (By.CSS_SELECTOR, ".home-pants .content .title")
    SECTION_2_BLOCK_2_IMAGE = (By.CSS_SELECTOR, '.home-t-shirts img')
    SECTION_2_BLOCK_3_IMAGE = (By.CSS_SELECTOR, '.home-erin img')
    SECTION_2_BLOCK_4_IMAGE = (By.CSS_SELECTOR, '.home-performance img')
    SECTION_2_BLOCK_5_IMAGE = (By.CSS_SELECTOR, '.home-eco img')
