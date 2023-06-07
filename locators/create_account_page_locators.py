"""This section contain create account page locators"""

from selenium.webdriver.common.by import By


class CreateAccountPageLocators:
    # Page-title Wrapper
    CREATE_AN_ACCOUNT_HEADER = (By.CSS_SELECTOR, "h1")
    PERSONAL_INFORMATION_LEGEND = (By.CSS_SELECTOR, ".fieldset.create.info")
    CREATE_AN_ACCOUNT_FIRSTNAME_LABEL = (By.CSS_SELECTOR, "label[for='firstname']")
    CREATE_AN_ACCOUNT_FIRSTNAME = (By.CSS_SELECTOR, "#firstname")
    # &&&&&&&&&&
    CREATE_AN_ACCOUNT_FIRSTNAME_ASTERISK = (By.CSS_SELECTOR, "+ span.required")
    CREATE_AN_ACCOUNT_LASTNAME_LABEL = (By.CSS_SELECTOR, "label[for='lastname']")
    CREATE_AN_ACCOUNT_LASTNAME = (By.CSS_SELECTOR, "#lastname")
    CREATE_AN_ACCOUNT_SIGN_UP_CHECKBOX = (By.CSS_SELECTOR, "label[for='is_subscribed']")
    CREATE_AN_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[title='Create an Account']")
