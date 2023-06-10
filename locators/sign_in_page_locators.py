"""This section contain Sign In page locators"""

from selenium.webdriver.common.by import By


class SingInPageLocators:
    # SignIn form > Registered Customers
    PAGE_HEADER = (By.CSS_SELECTOR, "h1")
    REGISTERED_CUSTOMERS_HEADER = (By.CSS_SELECTOR, "#block-customer-login-heading")
    REGISTERED_CUSTOMERS_NOTE = (By.CSS_SELECTOR, "div.field.note")
    CUSTOMER_EMAIL_LABEL = (By.CSS_SELECTOR, "label[for='email'] span")
    CUSTOMER_EMAIL = (By.CSS_SELECTOR, "#email")
    CUSTOMER_EMAIL_ASTERISK = (By.CSS_SELECTOR, "+ span.required")
    CUSTOMER_PASSWORD_LABEL = (By.CSS_SELECTOR, "label[for ='pass'] span")
    CUSTOMER_PASSWORD = (By.CSS_SELECTOR, "#pass")
    SIGN_IN_BUTTON = (By.ID, 'send2')
    FORGOT_PASSWORD = (By.XPATH, '//*[@id="login-form"]/fieldset/div[4]/div[2]/a/span')
    EMAIL_ERROR = (By.CSS_SELECTOR, "#email-error")
    PASSWORD_ERROR = By.XPATH, "//div[@id='pass-error']"
    ERROR = By.CSS_SELECTOR, '.mage-error'
    ERROR_MESSAGE = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')

    # SignIn form > New Customers
    NEW_CUSTOMERS_HEADER = (By.CSS_SELECTOR, "#block-new-customer-heading")
    NEW_CUSTOMERS_NOTE = (By.CSS_SELECTOR, ".block-new-customer > div.block-content > p")
