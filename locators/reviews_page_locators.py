"""
This section contains locators for Reviews
https://magento.softwaretestingboard.com/meteor-workout-short.html#reviews
"""

from selenium.webdriver.common.by import By

class ReviewsPageLocators:

    STAR_1 = (By.CSS_SELECTOR, '#Rating_1_label')
    NICKNAME_INPUT = (By.CSS_SELECTOR, '#nickname_field')
    SUMMARY_INPUT = (By.CSS_SELECTOR, '#summary_field')
    REVIEW_INPUT = (By.CSS_SELECTOR, '#review_field')
    SUBMIT_REVIEW_BUTTON = (By.CSS_SELECTOR, '.submit')
    REVIEW_SUCCESSFULLY_SUBMITTED = (By.CSS_SELECTOR, '.message-success')
