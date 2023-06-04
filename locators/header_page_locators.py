"""This section contain header locators"""

from selenium.webdriver.common.by import By


class HeaderPageLocators:
    # Panel Wrapper
    SIGN_IN = (By.XPATH, "(//a[contains(text(),'Sign In')])[1]")
    CREATE_AN_ACCOUNT = (By.XPATH, "(//a[normalize-space()='Create an Account'])[1]")
    GREETING_MESSAGE = (By.XPATH, "(//span[@class='not-logged-in'])[1]")

    # Header Content
    LOGO = (By.XPATH, "//a[@aria-label='store logo']//img")
    CART_ICON = (By.XPATH, "//a[@class='action showcart']")
    CART_BUTTON_MESSAGE = (By.XPATH, "//strong[@class='subtitle empty']")

    # Top menu navigation
    SALE = (By.ID, 'ui-id-8')

