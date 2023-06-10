from pages.base_page import BasePage
from locators.reviews_page_locators import ReviewsPageLocators
import time


class ReviewsPage(BasePage):
    locators = ReviewsPageLocators

    def one_star_review_correct(self):
        one_star_element = self.element_is_clickable(self.locators.STAR_1)
        time.sleep(1)
        one_star_element.click()
        time.sleep(1)

    def nickname_input_review_correct(self):
        nickname_input_element = self.element_is_clickable(self.locators.NICKNAME_INPUT)
        time.sleep(1)
        nickname_input_element.click()
        nickname_input_element.clear()
        nickname_input_element.send_keys('Some Name')
        time.sleep(1)

    def summary_input_review_correct(self):
        summary_input_element = self.element_is_clickable(self.locators.SUMMARY_INPUT)
        time.sleep(1)
        summary_input_element.click()
        summary_input_element.clear()
        summary_input_element.send_keys('Some Summary Text')
        time.sleep(1)

    def review_input_review_correct(self):
        review_input_element = self.element_is_clickable(self.locators.REVIEW_INPUT)
        time.sleep(1)
        review_input_element.click()
        review_input_element.clear()
        review_input_element.send_keys('Some Review Text')
        time.sleep(1)

    def send_review_correct(self):
        review_input_element = self.element_is_visible(self.locators.SUBMIT_REVIEW_BUTTON)
        time.sleep(1)
        review_input_element.click()
        time.sleep(1)
        review_successfully_submitted = self.element_is_present(self.locators.REVIEW_SUCCESSFULLY_SUBMITTED)
        time.sleep(1)
        return review_successfully_submitted


