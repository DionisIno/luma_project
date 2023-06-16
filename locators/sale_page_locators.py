"""This section contains Sale page locators"""

from selenium.webdriver.common.by import By


class SideBarLocators:
    """A class for sidebar locators"""
    # WOMEN'S DEALS section
    WOMEN_DEALS_TITLE = (By.CSS_SELECTOR, '.categories-menu > strong:nth-child(1) > span')
    WOMEN_DEALS_ELEMENTS = {
        "hoodies_and_sweatshirts_w": (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(2) > li:nth-child(1) > a'),
        "jackets_w": (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(2) > li:nth-child(2) > a'),
        "tees_w": (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(2) > li:nth-child(3) > a'),
        "bras_and_tanks": (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(2) > li:nth-child(4) > a'),
        "pants_w": (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(2) > li:nth-child(5) > a'),
        "shorts_w": (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(2) > li:nth-child(6) > a')
    }
    # MEN'S DEALS section
    MEN_DEALS_TITLE = (By.CSS_SELECTOR, '.categories-menu > strong:nth-child(3) > span')
    MEN_DEALS_ELEMENTS = {
        "hoodies_and_sweatshirts_m": (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(4) > li:nth-child(1) > a'),
        "jackets_m": (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(4) > li:nth-child(2) > a'),
        "tees_m": (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(4) > li:nth-child(3) > a'),
        "pants_m": (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(4) > li:nth-child(4) > a'),
        "shorts_m": (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(4) > li:nth-child(5) > a')
    }
    # GEAR DEALS section
    GEAR_DEALS_TITLE = (By.CSS_SELECTOR, '.categories-menu > strong:nth-child(5) > span')
    GEAR_DEALS_ELEMENTS = {
        "bags": (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(6) > li:nth-child(1) > a'),
        "fitness_equipment": (By.CSS_SELECTOR, '.categories-menu > ul:nth-child(6) > li:nth-child(2) > a'),
    }


class MainContentPromoBlocks:
    """A class for Main Content Promo Blocks locators"""
    HEAD_TEXT = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
