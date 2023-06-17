"""This section contains Pants page locators"""

from selenium.webdriver.common.by import By


class PantsPageLocators:
    PANTS = (By.CSS_SELECTOR, '#page-title-heading .base')
