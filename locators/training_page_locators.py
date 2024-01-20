"""This section contains training locators"""

from selenium.webdriver.common.by import By


class TrainingPageLocators:

    HEAD_TEXT = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')

    # Sidebar panel section
    SHOP_BY = (By.XPATH, '//div[4]/div[2]/div[1]/div[1]/strong')
    CATEGORY = (By.XPATH, '//*[@id="narrow-by-list2"]/dt')
    VIDEO_DOWNLOAD = (By.XPATH, '//*[@id="narrow-by-list2"]/dd/ol/li/a')
    COMPARE_PRODUCTS = (By.XPATH, '//*[@id="block-compare-heading"]')
    MY_WISH_LIST = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[3]/div[2]/div[1]/strong')

    # Training promo-blocks
    BLOCK_1_MAIN = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/a[1]/img')
    BLOCK_2_ERIN = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/a[2]/img')
    BLOCK_3_ON_DEMAND = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[1]/a[3]')
    TOP_VIDEOS = (By.XPATH, '//*[@id="maincontent"]/div[4]/div[1]/div[1]/div[2]/h2')
