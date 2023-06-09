"""This section contain header locators"""

from selenium.webdriver.common.by import By


class HeaderPageLocators:
    # Panel Wrapper
    SIGN_IN = By.XPATH, "(//a[contains(text(),'Sign In')])[1]"
    CREATE_AN_ACCOUNT = By.XPATH, "(//a[normalize-space()='Create an Account'])[1]"
    GREETING_MESSAGE = By.XPATH, "(//span[@class='not-logged-in'])[1]"
    DROPDOWN_BUTTON = By.XPATH, "//div[@class='panel header']//button[@type='button']"
    HEADER_LIST = By.XPATH, "//div[@aria-hidden='false']//ul[@class='header links']"
    MY_ACCOUNT = By.XPATH, "(//a[normalize-space()='My Account'])[1]"
    MY_WISH_LIST = By.XPATH, "(//a[normalize-space()='My Wish List'])[1]"
    SIGN_OUT = By.XPATH, "(//a[normalize-space()='Sign Out'])[1]"

    # Header Content
    LOGO = By.XPATH, "//a[@aria-label='store logo']//img"
    CART_ICON = By.XPATH, "//a[@class='action showcart']"
    CART_BUTTON_MESSAGE = By.XPATH, "//strong[@class='subtitle empty']"
    SEARCH_FIELD = By.XPATH, "//input[@id='search']"
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
    TOPS_BOTTOMS_SUBSECTION = By.XPATH, '//*[@id="ui-id-2"]/li[3]/ul'
    TOPS_SUBSECTION = By.XPATH, '//*[@id="ui-id-2"]/li[3]/ul/li[1]'
    TOPS_SUBSECTIONS = By.XPATH, '//*[@id="ui-id-2"]/li[3]/ul/li[1]/ul'
    JACKETS_SUBSECTION = By.XPATH, '//a[@id="ui-id-19"]'
    HOODIES_SWEATSHIRTS_SUBSECTION = By.XPATH, '//a[@id="ui-id-20"]'
    TEES_SUBSECTION = By.XPATH, '//a[@id="ui-id-21"]'
    TANKS_SUBSECTION = By.XPATH, '//a[@id="ui-id-22"]'
    BOTTOMS_SUBSECTION = By.XPATH, '//*[@id="ui-id-2"]/li[3]/ul/li[2]'
    BOTTOMS_SUBSECTIONS = By.XPATH, "(//ul[@role='menu'])[7]"
    PANTS = By.XPATH, '//*[@id="ui-id-2"]/li[3]/ul/li[2]/ul/li[1]'
    SHORTS = By.XPATH, '//*[@id="ui-id-2"]/li[3]/ul/li[2]/ul/li[2]'
    TOPS_BOTTOMS_SUBSECTION = By.ID, 'ui-id-17'

    # Women Section
    WOMEN_SECTION = By.XPATH, "(//a[@id='ui-id-4'])[1]"
    TOPS_BOTTOMS_SUBSECTION_WOMEN = By.XPATH, '//*[@id="ui-id-2"]/li[2]/ul'
    TOPS_SUBSECTION_WOMEN = By.XPATH, '//*[@id="ui-id-2"]/li[2]/ul/li[1]'
    TOPS_SUBSECTIONS_WOMEN = By.XPATH, '(//ul[@role="menu"])[3]'
    JACKETS_SUBSECTION_WOMEN = By.XPATH, '//a[@id="ui-id-11"]'
    HOODIES_SWEATSHIRTS_SUBSECTION_WOMEN = By.XPATH, '//a[@id="ui-id-12"]'
    TEES_SUBSECTION_WOMEN = By.XPATH, '//a[@id="ui-id-13"]'
    BRAS_TANKS_SUBSECTION_WOMEN = By.XPATH, '//a[@id="ui-id-14"]'
    BOTTOMS_SUBSECTION_WOMEN = By.XPATH, '//*[@id="ui-id-2"]/li[2]/ul/li[2]'
    BOTTOMS_SUBSECTIONS_WOMEN = By.XPATH, "(//ul[@role='menu'])[4]"
    PANTS_WOMEN = By.XPATH, '//*[@id="ui-id-2"]/li[2]/ul/li[2]/ul/li[1]'
    SHORTS_WOMEN = By.XPATH, '//*[@id="ui-id-2"]/li[2]/ul/li[2]/ul/li[2]'

