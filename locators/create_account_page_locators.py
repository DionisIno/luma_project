"""This section contain create account page locators"""

from selenium.webdriver.common.by import By


class CreateAccountPageLocators:
    # Page-title Wrapper
    CREATE_NEW_CUSTOMER_ACCOUNT_HEADER = (By.CSS_SELECTOR, "h1")
    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME = (By.ID, 'lastname')
    EMAIL = (By.ID, 'email_address')
    PASSWORD = (By.CSS_SELECTOR, '[id="password"]')
    PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, '[id="password-confirmation"]')
    CREATE_AN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'button[title="Create an Account"]')
    MASSAGE_REGISTERED_EMAIL = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
