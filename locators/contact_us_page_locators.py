"""This section contains locators for Contact Us page
Page has been modified (status on 25 July 2023) so selectors have been updated"""

from selenium.webdriver.common.by import By


class ContactUsPageLocators:
    CONTACT_US_TITLE = (By.CSS_SELECTOR, '.page-title .base')           # css-selector for old page
    CONTACT_TITLE = (By.CSS_SELECTOR, '.elementor-element-94d10e2 > div h2')  # updated 01.20.2024
