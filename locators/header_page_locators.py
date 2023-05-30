"""This section contain header locators"""

from selenium.webdriver.common.by import By


class HeaderPageLocators:
    # Panel Wrapper
    CREATE_AN_ACCOUNT = (By.CSS_SELECTOR, "div[class='panel header'] ul li:nth-child(3)")
