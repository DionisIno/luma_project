"""This section contains locators for Shopping Cart page"""

from selenium.webdriver.common.by import By


class ShoppingCartPageLocators:
    TITLE = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
    IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, 'div.cart-empty > p:nth-child(1)')
    HERE_LINK = (By.CSS_SELECTOR, 'div.cart-empty > p:nth-child(2) > a')

    
