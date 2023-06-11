"""This section contains "Orders and returns" page locators"""

from selenium.webdriver.common.by import By


class OrdersAndReturnsLocators:
    """A class for "Orders and returns" form locators"""

    PAGE_HEADER = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
