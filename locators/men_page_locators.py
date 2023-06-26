"""This section contain Men page locators"""

from selenium.webdriver.common.by import By


class MenPageLocators:
    SIDE_BAR_TOPS = (By.CSS_SELECTOR, '#narrow-by-list2 a:first-child')
    MEN_SUBHEAD_TEXT_TOPS = (By.CSS_SELECTOR, '#page-title-heading')
    SIDE_BAR_BOTTOMS = (By.CSS_SELECTOR, '#narrow-by-list2 > dd > ol > li:nth-child(2) > a')
    MEN_SUBHEAD_TEXT_BOTTOMS = (By.CSS_SELECTOR, '#page-title-heading > span')
    SIDE_BAR_SUBHEAD_TOPS = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/strong/span')
    SIDE_BAR_SUBHEAD_BOTTOMS = (By.CSS_SELECTOR, '#maincontent > div.sidebar > div.widget > div > strong:nth-child(3)')
    SIDE_BAR_HOODIES = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[1]/li[1]/a')
    SIDE_BAR_JACKETS = (By.CSS_SELECTOR, '.sidebar-main .block-static-block ul li:nth-child(2) a')
    MEN_SUBHEAD_TEXT_JACKETS = (By.CSS_SELECTOR, '#page-title-heading > span')
    SIDE_BAR_HEADER_MEN = (By.CSS_SELECTOR, '#page-title-heading > span')
    MEN_SUBHEAD_TEXT_HOODIES = (By.XPATH, '//*[@id="page-title-heading"]/span')
    SIDE_BAR_TEES = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[1]/li[3]/a')
    MEN_SUBHEAD_TEXT_TEES = (By.XPATH, '//*[@id="page-title-heading"]/span')
    SIDE_BAR_TANKS = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[1]/li[4]/a')
    MEN_SUBHEAD_TEXT_TANKS = (By.XPATH, '//*[@id="page-title-heading"]/span')
    SIDE_BAR_PANTS = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[2]/li[1]/a')
    MEN_SUBHEAD_TEXT_PANTS = (By.XPATH, '//*[@id="page-title-heading"]/span')
    SIDE_BAR_SHORTS = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[2]/li[2]/a')
    MEN_SUBHEAD_TEXT_SHORTS = (By.XPATH, '//*[@id="page-title-heading"]/span')