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
    BTN_ADD_TO_CART = (By.CSS_SELECTOR, 'button.action.tocart')

    # Promo Block
    PROMO_BLOCK = (By.CSS_SELECTOR, '.blocks-promo')
    SECTION_2_BLOCK_1_INFO_BLOCK_TITLE = (By.CSS_SELECTOR, '.home-pants .content .title')
