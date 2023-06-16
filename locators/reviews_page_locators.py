"""
This section contains locators for Reviews
https://magento.softwaretestingboard.com/meteor-workout-short.html#reviews
"""

from selenium.webdriver.common.by import By

class ReviewsPageLocators:

    REVIEW_MENU = (By.CSS_SELECTOR, '#tab-label-reviews-title')
    STAR_1 = (By.CSS_SELECTOR, '#Rating_1_label')
    STAR_2 = (By.CSS_SELECTOR, '#Rating_2_label')
    STAR_3 = (By.CSS_SELECTOR, '#Rating_3_label')
    NICKNAME_INPUT = (By.CSS_SELECTOR, '#nickname_field')
    SUMMARY_INPUT = (By.CSS_SELECTOR, '#summary_field')
    REVIEW_INPUT = (By.CSS_SELECTOR, '#review_field')
    SUBMIT_REVIEW_BUTTON = (By.CSS_SELECTOR, '.submit')
    REVIEW_SUCCESSFULLY_SUBMITTED = (By.CSS_SELECTOR, '.message-success')
    MESSAGE_ERROR = (By.CSS_SELECTOR, '.mage-error')
    ALL_CSS_ELEMENTS_ON_PAGE = (By.CSS_SELECTOR, '*')

