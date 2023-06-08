"""This section contain training-video locators"""

from selenium.webdriver.common.by import By


class TrainingVideoPageLocators:

    HEAD_TEXT = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
