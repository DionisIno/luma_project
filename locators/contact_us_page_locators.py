"""This section contains locators for Contact Us page"""

from selenium.webdriver.common.by import By


class ContactUsPageLocators:
    CONTACT_US_TITLE = (By.CSS_SELECTOR, '.page-title .base')
