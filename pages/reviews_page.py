from pages.base_page import BasePage
from locators.reviews_page_locators import ReviewsPageLocators

from selenium.webdriver.common.by import By
from conftest import driver
import time


class ReviewsPage(BasePage):
    locators = ReviewsPageLocators

    def one_star_review_correct(self):
        self.click_and_return_element(self.locators.STAR_1)
        time.sleep(2)

    def nickname_input_review_correct(self):
        nickname_input_element = self.element_is_clickable(self.locators.NICKNAME_INPUT)
        nickname_input_element.click()
        nickname_input_element.clear()
        nickname_input_element.send_keys('Some Name')
        time.sleep(2)

    def summary_input_review_correct(self):
        summary_input_element = self.element_is_clickable(self.locators.SUMMARY_INPUT)
        summary_input_element.click()
        summary_input_element.clear()
        summary_input_element.send_keys('Some Summary Text')
        time.sleep(2)

    def review_input_review_correct(self):
        review_input_element = self.element_is_clickable(self.locators.REVIEW_INPUT)
        review_input_element.click()
        review_input_element.clear()
        review_input_element.send_keys('Some Review Text')
        time.sleep(2)

    def send_review_correct(self):
        review_input_element = self.element_is_visible(self.locators.SUBMIT_REVIEW_BUTTON)
        review_input_element.click()
        review_successfully_submitted = self.element_is_visible(self.locators.REVIEW_SUCCESSFULLY_SUBMITTED)
        print(review_successfully_submitted.text, ' = review_successfully_submitted.text')
        return review_successfully_submitted


