"""This section contain training locators"""

from selenium.webdriver.common.by import By


class TrainingPageLocators:

    HEAD_TEXT = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')

    # Sidebar panel section
    SHOP_BY = (By.XPATH, '//div[4]/div[2]/div[1]/div[1]/strong')
