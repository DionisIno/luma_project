"""This section contain main page locators"""
import random

from selenium.webdriver.common.by import By


class MainPageLocators:

    # Hot Seller section
    CARD_TITLE = (By.CSS_SELECTOR, f"strong[class='product-item-name']:nth-child({random.randint(1, 6)})")
    PRODUCT_CARD = (By.CSS_SELECTOR,
                    f"li[class='product-item']:nth-child({random.randint(1, 6)}) div[class='product-item-info']")
