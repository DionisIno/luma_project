"""This section contain Forgot Your Password page locators"""

from selenium.webdriver.common.by import By

class ForgotYourPasswordPageLocators:
    PAGE_HEADER = (By.CSS_SELECTOR, "h1.page-title > span.base")
    FORGOT_YOUR_PASSWORD_NOTE = (By.CSS_SELECTOR, "div.field.note")
