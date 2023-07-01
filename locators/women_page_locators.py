"""This section contain Women page locators"""

from selenium.webdriver.common.by import By


class WomenPageLocators:
    # Side panel | Shop By
    SHOP_BY = (By.XPATH, '//div[4]/div[2]/div[1]/div[1]/strong')
    WOMEN_HEAD_TEXT = (By.XPATH, '//*[@id="page-title-heading"]/span')
    CATEGORY_TITLE = (By.XPATH, '//div[4]/div[2]/div[1]/div[2]/dl/dt')
    # Sidebar - additional
    COMPARE_PRODUCTS = (By.XPATH, "//strong[@id='block-compare-heading']")
    NOTE_1 = (By.XPATH, "// div[normalize-space() = 'You have no items to compare.']")
    MY_WISH_LIST = (By.XPATH, "//strong[normalize-space()='My Wish List']")
    NOTE_2 = (By.XPATH, "//div[normalize-space()='You have no items in your wish list.']")
    ITEMS = [(COMPARE_PRODUCTS, "Compare Products"),
             (NOTE_1, "You have no items to compare."),
             (MY_WISH_LIST, "My Wish List"),
             (NOTE_2, "You have no items in your wish list.")]
