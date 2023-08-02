"""This section contains locators for related outside pages for checking of correct transfer to them"""

from selenium.webdriver.common.by import By


class WriteForUsPageLocators:
    WRITE_FOR_US_MENU_ITEM = (By.CSS_SELECTOR, '#menu-item-7639 > a')


class SubscribePageLocators:
    SUBSCRIBE_TITLE = (By.CSS_SELECTOR, '#mc_embed_signup_scroll > h2')
