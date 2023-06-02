"""This section contain Sign In page locators"""

from selenium.webdriver.common.by import By


class SingInPageLocators:
    # SignIn form > Registered Customers
    PAGE_HEADER = (By.CSS_SELECTOR, "h1")
    REGISTERED_CUSTOMERS_HEADER = (By.CSS_SELECTOR, "#block-customer-login-heading")
    REGISTERED_CUSTOMERS_NOTE = (By.CSS_SELECTOR, "div.field.note")
    CUSTOMER_EMAIL_LABEL = (By.CSS_SELECTOR, "label[for='email'] span")
    CUSTOMER_EMAIL = (By.CSS_SELECTOR, "#customer-email")
    CUSTOMER_EMAIL_ASTERISK = (By.CSS_SELECTOR, "+ span.required")

    # SignIn form > New Customers
