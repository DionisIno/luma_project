"""This section contain training-video download locators"""

from selenium.webdriver.common.by import By


class TrainingVideoDownloadPageLocators:

    HEAD_TEXT = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
    COMPARE_PRODUCTS = (By.ID, 'block-compare-heading')
    MY_WISH_LIST = (By.CSS_SELECTOR, '.block.block-wishlist .block-title')
