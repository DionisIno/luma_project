"""This section contain main page locators"""
from random import randint

from selenium.webdriver.common.by import By


class MainPageLocators:
    # Hot Seller section
    CARD_TITLE = (By.CSS_SELECTOR, f"strong[class='product-item-name']:nth-child({randint(1, 6)})")
