"""This section contain Men page locators"""

from selenium.webdriver.common.by import By


class MenPageLocators:
    SIDE_BAR_TOPS = (By.CSS_SELECTOR, '#narrow-by-list2 a:first-child')
    MEN_SUBHEAD_TEXT_TOPS = (By.CSS_SELECTOR, '#page-title-heading')
    SIDE_BAR_BOTTOMS = (By.CSS_SELECTOR, '#narrow-by-list2 > dd > ol > li:nth-child(2) > a')
    MEN_SUBHEAD_TEXT_BOTTOMS = (By.CSS_SELECTOR, '#page-title-heading > span')
    SIDE_BAR_SUBHEAD_TOPS = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/strong/span')
    SIDE_BAR_SUBHEAD_BOTTOMS = (By.CSS_SELECTOR, '#maincontent > div.sidebar > div.widget > div > strong:nth-child(3)')
    SIDE_BAR_HOODIES = (By.CSS_SELECTOR, 'div.sidebar-main ul.block-static-block li a')
    SIDE_BAR_JACKETS = (By.CSS_SELECTOR, '.widget.block.block-static-block ul li.item-2 a')
    MEN_SUBHEAD_TEXT_JACKETS = (By.CSS_SELECTOR, '#page-title-heading > span')
    SIDE_BAR_HEADER_MEN = (By.CSS_SELECTOR, '#page-title-heading > span')
