"""This section contains Promotions_pants page locators"""

from selenium.webdriver.common.by import By


class PantsLocators:
    """A class for sidebar locators"""
    # Shopping Options section
    SHOPPING_OPTIONS = (By.XPATH, "//strong[text()='Shopping Options']")
    STYLE = (By.XPATH, "//div[text()='Style']")
