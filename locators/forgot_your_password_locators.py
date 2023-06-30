"""This section contain Forgot Your Password page locators"""

from selenium.webdriver.common.by import By

class ForgotYourPasswordPageLocators:
    PAGE_HEADER = (By.CSS_SELECTOR, 'h1.page-title > span.base')
    FORGOT_YOUR_PASSWORD_NOTE = (By.CSS_SELECTOR, 'div.field.note')
    EMAIL = (By.CSS_SELECTOR, '#email_address')
    EMAIL_LABEL = (By.CSS_SELECTOR, "label[for='email_address'] span")
    FORGOT_YOUR_PASSWORD_CAPTCHA = (By.CSS_SELECTOR, '#captcha_user_forgotpassword')
    FORGOT_YOUR_PASSWORD_CAPTCHA_LABEL = (By.CSS_SELECTOR, '.captcha.required > label > span')
