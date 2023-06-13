import allure

from pages.base_page import BasePage
from locators.reviews_page_locators import ReviewsPageLocators
import time


class ReviewsPage(BasePage):
    locators = ReviewsPageLocators
    @allure.feature('tc_01_15_01 - Click on element 1 star')
    def one_star_review_correct(self):
        """Click on element 1 star"""
        one_star_element = self.element_is_clickable(self.locators.STAR_1)
        time.sleep(1)
        one_star_element.click()
        time.sleep(1)

    @allure.feature('tc_01_15_01 - Entering data into the nickname input')
    def nickname_input_review_correct(self):
        """Entering data into the nickname input"""
        nickname_input_element = self.element_is_clickable(self.locators.NICKNAME_INPUT)
        time.sleep(2)
        nickname_input_element.click()
        nickname_input_element.clear()
        nickname_input_element.send_keys('Some Name')
        time.sleep(2)

    @allure.feature('tc_01_15_01 - Entering data into input summary')
    def summary_input_review_correct(self):
        """Entering data into input summary"""
        summary_input_element = self.element_is_clickable(self.locators.SUMMARY_INPUT)
        time.sleep(2)
        summary_input_element.click()
        summary_input_element.clear()
        summary_input_element.send_keys('Some Summary Text')
        time.sleep(2)

    @allure.feature('tc_01_15_01 - Entering data into input review')
    def review_input_review_correct(self):
        """Entering data into input review"""
        review_input_element = self.element_is_clickable(self.locators.REVIEW_INPUT)
        time.sleep(2)
        review_input_element.click()
        review_input_element.clear()
        review_input_element.send_keys('Some Review Text')
        time.sleep(2)

    @allure.feature('tc_01_15_01 - Click on the send feedback button')
    def send_review_correct(self):
        """Click on the send feedback button"""
        button_element = self.element_is_clickable(self.locators.SUBMIT_REVIEW_BUTTON)
        time.sleep(2)
        button_element.click()
        time.sleep(2)

    def some_wait(self):
        time.sleep(5)

    def review_have_been_send_correctly(self):
        """Checking if a message about the successful submission for moderation of the review appears"""
        review_successfully_submitted = self.get_text(self.locators.REVIEW_SUCCESSFULLY_SUBMITTED)
        time.sleep(10)
        return review_successfully_submitted

    #
    # @allure.feature('tc_01_15_01 - Checking if a message about the successful submission for moderation of the review appears')
    # def get_review_successfully_submitted_confirmation(self):
    #     """Checking if a message about the successful submission for moderation of the review appears"""
    #     review_successfully_submitted = self.element_is_present(self.locators.REVIEW_SUCCESSFULLY_SUBMITTED, timeout=15)
    #     return review_successfully_submitted

    # def click_submit_review(self):
    #     review_input_element = self.element_is_present(self.locators.SUBMIT_REVIEW_BUTTON)
    #     review_input_element.click()
    #     return review_input_element

    # def send_review_correct(self):
    #     # review_input_element = self.element_is_present(self.locators.SUBMIT_REVIEW_BUTTON)
    #     # review_input_element.click()
    #     review_successfully_submitted = self.element_is_present(self.locators.REVIEW_SUCCESSFULLY_SUBMITTED)
    #     return review_successfully_submitted

#
# —- работает
# если
# клик
# вынести
# в
# отдельный
# метод, и
# после
# него
# дополнительный
# wait, тогда
# тест
# pass