"""This section contain training-video download locators"""

from selenium.webdriver.common.by import By


class TrainingVideoDownloadPageLocators:

    HEAD_TEXT = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
    COMPARE_PRODUCTS = (By.ID, 'block-compare-heading')
    MY_WISH_LIST = (By.CSS_SELECTOR, '.block.block-wishlist .block-title')
    COMPARE_MESSAGE = (By.CSS_SELECTOR, '.block.block-compare .empty')
    MY_WISH_LIST_MESSAGE = (By.CSS_SELECTOR, '.block.block-wishlist .empty')
    NO_PRODUCTS_MESSAGE = (By.CLASS_NAME, 'info')
