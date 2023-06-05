"""This section contain main page locators"""
import random

from selenium.webdriver.common.by import By


class MainPageLocators:

    # Hot Seller section
    CARD_TITLE = (By.CSS_SELECTOR,
                  f"li[class='product-item']:nth-child({random.randint(1, 6)})  strong[class='product-item-name']")
    PRODUCT_CARD = (By.CSS_SELECTOR,
                    f"li[class='product-item']:nth-child({random.randint(1, 6)}) div[class='product-item-info']")
