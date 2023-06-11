"""This section contain header locators"""

from selenium.webdriver.common.by import By


class HeaderPageLocators:
    # Panel Wrapper
    SIGN_IN = By.XPATH, "(//a[contains(text(),'Sign In')])[1]"
    CREATE_AN_ACCOUNT = By.XPATH, "(//a[normalize-space()='Create an Account'])[1]"
    GREETING_MESSAGE = By.XPATH, "(//span[@class='not-logged-in'])[1]"

    # Header Content
    LOGO = By.XPATH, "//a[@aria-label='store logo']//img"
    CART_ICON = By.XPATH, "//a[@class='action showcart']"
    CART_BUTTON_MESSAGE = By.XPATH, "//strong[@class='subtitle empty']"
    SEARCH_FIELD = By.XPATH, "//input[@id = 'search']"
    SEARCH_DROPDOWN = By.XPATH, "//*[@id='search_autocomplete']"

    # Top menu navigation
    SALE = (By.ID, 'ui-id-8')
    TRAINING = (By.ID, 'ui-id-7')
    VIDEO_DOWNLOAD = (By.ID, 'ui-id-28')
    WHAT_IS_NEW = (By.ID, 'ui-id-3')
    WOMEN = (By.ID, 'ui-id-4')
    GEAR = (By.ID, 'ui-id-6')
    BAGS = (By.ID, 'ui-id-25')
    FITNESS_EQUIPMENT = (By.ID, 'ui-id-26')
    WATCHES = (By.ID, 'ui-id-27')
    # Men Section
    MEN_SECTION = (By.ID, 'ui-id-5')
    BOTTOMS_SUBSECTION = By.XPATH, '//*[@id="ui-id-2"]/li[3]/ul/li[2]'
    PANTS_SHORTS_SUBSECTION = By.XPATH, "(//ul[@role='menu'])[7]"
    PANTS = By.XPATH, '//*[@id="ui-id-2"]/li[3]/ul/li[2]/ul/li[1]'
    SHORTS = By.XPATH, '//*[@id="ui-id-2"]/li[3]/ul/li[2]/ul/li[2]'

