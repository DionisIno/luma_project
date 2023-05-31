"""This section contain Sign In page locators"""

from selenium.webdriver.common.by import By


class SingInPageLocators:
    # SignIn form > Registered Customers
    PAGE_HEADER = (By.CSS_SELECTOR, "h1")
    REGISTERED_CUSTOMERS_HEADER = (By.CSS_SELECTOR, "#block-customer-login-heading")

    # SignIn form > New Customers
