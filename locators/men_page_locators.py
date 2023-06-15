"""This section contain Men page locators"""

from selenium.webdriver.common.by import By


class MenPageLocators:
    SIDE_BAR_TOPS = (By.CSS_SELECTOR, '#narrow-by-list2 a:first-child')
    MEN_SUBHEAD_TEXT_TOPS = (By.CSS_SELECTOR, '#page-title-heading')
    SIDE_BAR_BOTTOMS = (By.CSS_SELECTOR, '#narrow-by-list2 > dd > ol > li:nth-child(2) > a')
