"""This section contains locators for Pants promo page"""

from selenium.webdriver.common.by import By


class PantsPromoPageLocators:
    PANTS_PROMO_TITLE = (By.CSS_SELECTOR, '#page-title-heading .base')
    SHOPPING_OPTIONS = (By.XPATH, "//strong[text()='Shopping Options']")
    STYLE = (By.XPATH, "//div[text()='Style']")
