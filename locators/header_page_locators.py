"""This section contain header locators"""

from selenium.webdriver.common.by import By


class HeaderPageLocators:
    # Panel Wrapper
    SIGN_IN = (By.XPATH, "(//a[contains(text(),'Sign In')])[1]")
    CREATE_AN_ACCOUNT = (By.XPATH, "(//a[normalize-space()='Create an Account'])[1]")
    GREETING_MESSAGE = (By.XPATH, "(//span[@class='not-logged-in'])[1]")
    LOGO = (By.XPATH, "//a[@aria-label='store logo']//img")

