"""This section contain create account page locators"""

from selenium.webdriver.common.by import By


class CreateAccountPageLocators:
    # # # Create an Account
    CREATE_AN_ACCOUNT_HEADER = (By.CSS_SELECTOR, "h1")
    PERSONAL_INFORMATION_LEGEND = (By.CSS_SELECTOR, ".fieldset.create.info legend")
    FIRST_NAME_LABEL = (By.CSS_SELECTOR, "label[for='firstname']")
    FIRST_NAME = (By.ID, 'firstname')
    LAST_NAME_LABEL = (By.CSS_SELECTOR, "label[for='lastname']")
    LAST_NAME = (By.ID, "lastname")
    SIGN_UP_CHECKBOX = (By.ID, "is_subscribed")
    SIGN_UP_CHECKBOX_LABEL = (By.CSS_SELECTOR, "label[for='is_subscribed']")
    EMAIL = (By.ID, 'email_address')
    PASSWORD = (By.CSS_SELECTOR, '[id="password"]')
    PASSWORD_CONFIRMATION = (By.CSS_SELECTOR, '[id="password-confirmation"]')
    CREATE_AN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, 'button[title="Create an Account"]')
    MESSAGE_ERROR = (By.CSS_SELECTOR, '.message-error.error.message > div')
    MESSAGE_SUCCESS = (By.CSS_SELECTOR, '.message-success.success.message > div')
    MESSAGE_FIRST_NAME_ERROR = (By.ID, 'firstname-error')
    MESSAGE_LAST_NAME_ERROR = (By.ID, 'lastname-error')
    MESSAGE_EMAIL_ERROR = (By.ID, 'email_address-error')
