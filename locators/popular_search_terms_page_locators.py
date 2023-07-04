"""This section contains locators for Popular Search Terms page"""

from selenium.webdriver.common.by import By


class PopularSearchTermsPageLocators:
    POPULAR_SEARCH_TERMS_TITLE = (By.CSS_SELECTOR, '.page-title .base')
