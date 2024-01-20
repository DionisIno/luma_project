"""This section contains Men page locators"""

from selenium.webdriver.common.by import By


class MenPageLocators:
    SIDE_BAR_HEADER_MEN = (By.CSS_SELECTOR, '#page-title-heading > span')
    # Category sidebar links locators
    SIDE_BAR_TOPS = (By.CSS_SELECTOR, '#narrow-by-list2 a:first-child')
    SIDE_BAR_BOTTOMS = (By.CSS_SELECTOR, '#narrow-by-list2 > dd > ol > li:nth-child(2) > a')
    # Sidebar TOPS locators
    MEN_SUBHEAD_TEXT_TOPS = (By.CSS_SELECTOR, '#page-title-heading')
    SIDE_BAR_HOODIES = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[1]/li[1]/a')
    SIDE_BAR_JACKETS = (By.CSS_SELECTOR, '.sidebar-main .block-static-block ul li:nth-child(2) a')
    SIDE_BAR_TEES = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[1]/li[3]/a')
    SIDE_BAR_TANKS = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[1]/li[4]/a')
    SIDE_BAR_SUBHEAD_TOPS = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/strong/span')
    MEN_SUBHEAD_TEXT_JACKETS = (By.CSS_SELECTOR, '#page-title-heading > span')
    MEN_SUBHEAD_TEXT_TEES = (By.XPATH, '//*[@id="page-title-heading"]/span')
    MEN_SUBHEAD_TEXT_TANKS = (By.XPATH, '//*[@id="page-title-heading"]/span')
    MEN_SUBHEAD_TEXT_HOODIES = (By.XPATH, '//*[@id="page-title-heading"]/span')
    # Sidebar BOTTOMS locators
    MEN_SUBHEAD_TEXT_BOTTOMS = (By.CSS_SELECTOR, '#page-title-heading > span')
    SIDE_BAR_SUBHEAD_BOTTOMS = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/strong[2]/span')
    SIDE_BAR_PANTS = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[2]/li[1]/a')
    SIDE_BAR_SHORTS = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[2]/div[2]/div/ul[2]/li[2]/a')
    MEN_SUBHEAD_TEXT_PANTS = (By.XPATH, '//*[@id="page-title-heading"]/span')
    MEN_SUBHEAD_TEXT_SHORTS = (By.XPATH, '//*[@id="page-title-heading"]/span')


    # Promo blocks locators

class MenPagePromoLocators:
    # Luma shorts block locators
    LUMA_SHORTS_BLOCK = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[1]')
    LUMA_SHORTS_BLOCK_IMG = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[1]/span[2]/img')
    LUMA_SHORTS_TITLE = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[1]/span[1]/strong')
    LUMA_SHORTS_TITLE_2 = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[1]/span[1]/span[1]')
    LUMA_SHORTS_TITLE_3 = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[1]/span[1]/span[2]')
    LUMA_TEES_BLOCK = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[2]')
    LUMA_TEES_BLOCK_IMG = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[2]/span[2]/img')
    LUMA_TEES_TITLE = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[2]/span[1]/strong')
    LUMA_TEES_TITLE_2 = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[2]/span[1]/span[1]')
    LUMA_TEES_TITLE_3 = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[2]/span[1]/span[2]')
    LUMA_HOODIES_BLOCK = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[3]')
    LUMA_HOODIES_BLOCK_IMG = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[3]/span[2]/img')
    LUMA_HOODIES_TITLE = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[3]/span[1]/strong')
    LUMA_HOODIES_TITLE_2 = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[3]/span[1]/span[1]')
    LUMA_HOODIES_TITLE_3 = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[2]/a[3]/span[1]/span[2]')
    LUMA_LAST_CHANCE_BLOCK = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[1]/a[2]')
    LUMA_LAST_CHANCE_BLOCK_BLOCK_IMG = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[1]/a[2]/img')
    LUMA_LAST_CHANCE_TITLE = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[1]/a[2]/span/strong')
    LUMA_LAST_CHANCE_TITLE_2 = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[1]/a[2]/span/span[1]')
    LUMA_LAST_CHANCE_TITLE_3 = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[1]/a[2]/span/span[2]')
    LUMA_SAVE_BLOCK = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[1]/a[1]')
    LUMA_SAVE_BLOCK_BLOCK_IMG = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[1]/a[1]/span/img')
    LUMA_SAVE_TITLE = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[1]/a[1]/span/strong')
    LUMA_SAVE_TITLE_2 = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[1]/a[1]/span/span[1]')
    LUMA_SAVE_TITLE_3 = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/div[1]/a[1]/span/span[2]')