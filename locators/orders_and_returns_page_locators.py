"""This section contains "Orders and returns" page locators"""

from selenium.webdriver.common.by import By


class OrdersAndReturnsPageLocators:
    """The class for "Orders and returns" page locators"""
    ORDERS_AND_RETURNS_TITLE = (By.CSS_SELECTOR, '.page-title .base')


class OrdersAndReturnsLocators:
    """A class for "Orders and returns" form locators"""
    # Headers
    PAGE_HEADER = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
    FORM_HEADER = (By.CSS_SELECTOR, 'legend[class="legend"] span')

    # Form field labels
    ORDER_ID_LABEL = (By.CSS_SELECTOR, 'label[for="oar-order-id"] span')
    BILLING_LAST_NAME_LABEL = (By.CSS_SELECTOR, 'label[for="oar-order-id"] span')
    FIND_ORDER_BY_LABEL = (By.CSS_SELECTOR, 'label[for="oar-order-id"] span')
    EMAIL_LABEL = (By.CSS_SELECTOR, 'label[for="oar-order-id"] span')
    BILLING_ZIP_CODE_LABEL = (By.CSS_SELECTOR, 'label[for="oar-order-id"] span')

    # Form fields
    ORDER_ID_INPUT = (By.ID, 'oar-order-id')
    BILLING_LAST_NAME_INPUT = (By.ID, 'oar-billing-lastname')
    FIND_ORDER_BY_DROP_DOWN_LIST = (By.ID, 'quick-search-type-id')
    EMAIL_INPUT = (By.ID, 'oar_email')
    BILLING_ZIP_CODE_INPUT = (By.ID, 'oar_zip')

    # Button
    CONTINUE_BUTTON = (By.CSS_SELECTOR, 'button[title="Continue"]')
