"""This section contain footer locators"""

from selenium.webdriver.common.by import By


class FooterPageLocators:
    SEARCH_TERMS_LINK = (By.CSS_SELECTOR, "ul[class='footer links'] li:nth-child(1)")
    