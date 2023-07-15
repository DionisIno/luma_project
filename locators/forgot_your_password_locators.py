"""This section contain Forgot Your Password page locators"""

from selenium.webdriver.common.by import By

class ForgotYourPasswordPageLocators:
    PAGE_HEADER = (By.CSS_SELECTOR, 'h1.page-title > span.base')
    FORGOT_YOUR_PASSWORD_NOTE = (By.CSS_SELECTOR, 'div.field.note')
    EMAIL = (By.CSS_SELECTOR, '#email_address')
    EMAIL_LABEL = (By.CSS_SELECTOR, "label[for='email_address'] span")
    FORGOT_YOUR_PASSWORD_CAPTCHA = (By.CSS_SELECTOR, '#captcha_user_forgotpassword')
    FORGOT_YOUR_PASSWORD_CAPTCHA_LABEL = (By.CSS_SELECTOR, '.captcha.required > label > span')
    RELOAD_CAPTCHA_BUTTON = (By.CSS_SELECTOR, 'button[title = "Reload captcha"]')
    RELOAD_CAPTCHA_IMAGE = (By.XPATH, '//img[@class="captcha-img"]')
    RESET_MY_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'button[class="action submit primary"]')
    RESET_MY_PASSWORD_EMAIL_ERROR = (By.CSS_SELECTOR, '#email_address-error')
    RESET_MY_PASSWORD_CAPTCHA_ERROR = (By.CSS_SELECTOR, '#captcha_user_forgotpassword-error')
    ERROR_MESSAGE = (By.XPATH, '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]')
