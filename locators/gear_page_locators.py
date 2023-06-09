"""This section contains Gear page locators"""

from selenium.webdriver.common.by import By


class SideBarLocators:
    """A class for sidebar locators"""
    # SHOP BY CATEGORY section
    CATEGORY = (By.XPATH, "//dl[@id='narrow-by-list2']//dt[text()='Category']")
    BAGS = (By.XPATH, "//dl[@id='narrow-by-list2']//a[text()='Bags']")

