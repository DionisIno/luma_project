"""This section contain create account page locators"""

from selenium.webdriver.common.by import By


class CreateAccountPageLocators:
    # Page-title Wrapper
    CREATE_NEW_CUSTOMER_ACCOUNT_HEADER = (By.XPATH, "//span[@class='base']")

