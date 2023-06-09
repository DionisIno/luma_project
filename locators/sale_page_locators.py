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
    # Title
    HEAD_TEXT = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
    # Block-promo sale-main, Women's deal
    SALE_WOMEN_IMG = (By.CSS_SELECTOR, '.sale-main img')
    SALE_WOMEN_TITLE = (By.CSS_SELECTOR, '.sale-main .info')
    SALE_WOMEN_CONTENT = (By.CSS_SELECTOR, '.sale-main .title')
    SALE_WOMEN_BUTTON = (By.CSS_SELECTOR, '.sale-main .more')
    # Block-promo-2columns, Men's Deals
    SALE_MEN_IMG = (By.CSS_SELECTOR, '.sale-mens img')
    SALE_MEN_TITLE = (By.CSS_SELECTOR, '.sale-mens .title')
    SALE_MEN_CONTENT = (By.CSS_SELECTOR, '.sale-mens .info')
    SALE_MEN_BUTTON = (By.CSS_SELECTOR, '.sale-mens .more')
    # Block-promo-2columns, Gear Deals
    SALE_GEAR_IMG = (By.CSS_SELECTOR, '.sale-women img')
    SALE_GEAR_TITLE = (By.CSS_SELECTOR, '.sale-women .title')
    SALE_GEAR_CONTENT = (By.CSS_SELECTOR, '.sale-women .info')
    SALE_GEAR_BUTTON = (By.CSS_SELECTOR, '.sale-women .more')
    MAIN_AND_2COLUMNS_BLOCKS_BUTTONS = {
        "sale_women_button": (By.CSS_SELECTOR, '.sale-main .more'),
        "sale_men_button": (By.CSS_SELECTOR, '.sale-mens .more'),
        "sale_gear_button": (By.CSS_SELECTOR, '.sale-women .more')
    }
    # Block - Deals 3 columns, 1st column - sale-20-off
    FIRST_COLUMN_IMG = (By.CSS_SELECTOR, '.sale-20-off .image img')
    FIRST_COLUMN_TITLE = (By.CSS_SELECTOR, '.sale-20-off .content .title')
    FIRST_COLUMN_CONTENT = (By.CSS_SELECTOR, '.sale-20-off .content .info')
    # Block - Deals 3 columns, 2nd column - sale-free-shipping
    SECOND_COLUMN_IMG = (By.CSS_SELECTOR, '.sale-free-shipping img')
    SECOND_COLUMN_TITLE = (By.CSS_SELECTOR, '.sale-free-shipping .title')
    SECOND_COLUMN_CONTENT = (By.CSS_SELECTOR, '.sale-free-shipping .info')
    # Block - Deals 3 columns, 3rd column - sale-women-t-shirts
    THIRD_COLUMN_IMG = (By.CSS_SELECTOR, '.sale-womens-t-shirts .image img')
    THIRD_COLUMN_TITLE = (By.CSS_SELECTOR, '.sale-womens-t-shirts .content .title')
    THIRD_COLUMN_CONTENT = (By.CSS_SELECTOR, '.sale-womens-t-shirts .content .info')
