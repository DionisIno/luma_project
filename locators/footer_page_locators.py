"""This section contains footer locators"""

from selenium.webdriver.common.by import By


class FooterPageLocators:
    ADVANCED_SEARCH_LINK = (By.CSS_SELECTOR, '.footer > :nth-child(3) > a')
    CONTACT_US_LINK = (By.CSS_SELECTOR, '.footer > :nth-child(5) > a')
    COPYRIGHT_SECTION = (By.CSS_SELECTOR, '.copyright')
    COPYRIGHT_TEXT = (By.CSS_SELECTOR, '.copyright > span')
    FOOTER_SECTION = (By.CSS_SELECTOR, '.page-footer')
    FOOTER_CONTENT = (By.CSS_SELECTOR, '.footer.content')
    ORDERS_AND_RETURNS_LINK = (By.CSS_SELECTOR, '.footer > :nth-child(4) > a')
    PRIVACY_AND_COOKIE_POLICY_LINK = (By.CSS_SELECTOR, '.footer > :nth-child(2) > a')
    SEARCH_TERMS_LINK = (By.CSS_SELECTOR, ".footer > :nth-child(1) > a")
    SUBSCRIBE_BUTTON = (By.CSS_SELECTOR, '.block.newsletter .actions')
    SUBSCRIBE_BUTTON_TEXT = (By.CSS_SELECTOR, '.block.newsletter .actions span')
    SUBSCRIBE_EMAIL_FIELD = (By.CSS_SELECTOR, '.field.newsletter')
    SUBSCRIBE_EMAIL_FIELD_ICON = (By.CSS_SELECTOR, 'div[class="control"]')
    SUBSCRIBE_SECTION = (By.CSS_SELECTOR, '.block.newsletter')
    WRITE_FOR_US_LINK = (By.CSS_SELECTOR, '.widget > ul > li > a')

    DATA_2 = [
        "ADVANCED_SEARCH_LINK = (By.CSS_SELECTOR, '.footer > :nth-child(3) > a')",
        " CONTACT_US_LINK = (By.CSS_SELECTOR, '.footer > :nth-child(5) > a')"
    ]
    