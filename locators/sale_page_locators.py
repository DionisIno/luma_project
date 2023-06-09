"""This section contains Sale page locators"""

from selenium.webdriver.common.by import By


class SideBarLocators:
    """A class for sidebar locators"""
    # WOMEN'S DEALS section
    WOMEN_DEALS_TITLE = (By.CSS_SELECTOR, '.categories-menu > strong:nth-child(1) > span')
    HOODIES_AND_SWEATSHIRTS_W = (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(2) > li:nth-child(1) > a')
    # MEN'S DEALS section

    # Gear Deals section


class MainContentPromoBlocks:
    """A class for Main Content Promo Blocks locators"""
    HEAD_TEXT = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
