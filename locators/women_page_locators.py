"""This section contain Women page locators"""

from selenium.webdriver.common.by import By


class WomenPageLocators:
    # Side panel | Shop By
    SHOP_BY = (By.XPATH, '//div[4]/div[2]/div[1]/div[1]/strong')
    WOMEN_HEAD_TEXT = (By.XPATH, '//*[@id="page-title-heading"]/span')
    CATEGORY_TITLE = (By.XPATH, '//div[4]/div[2]/div[1]/div[2]/dl/dt')
