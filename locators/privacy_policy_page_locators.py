"""This section contains locators for Privacy Policy page"""

from selenium.webdriver.common.by import By


class PrivacyPolicyPageLocators:
    PRIVACY_POLICY_TITLE = (By.CSS_SELECTOR, '.page-title .base')
