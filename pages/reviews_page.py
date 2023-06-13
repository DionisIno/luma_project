import allure
from selenium.common import TimeoutException

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

    @allure.feature('tc_01_15_01 - Just some wait')
    def some_wait(self):
        """Just some wait"""
        time.sleep(5)

    @allure.feature('tc_01_15_01 - Checking if a message about the successful submission for moderation of the review appears')
    def review_have_been_send_correctly(self):
        """
        Checking if a message about the successful submission for moderation of the review appears
        Validates text within a message
        """
        time.sleep(2)
        try:
            review_successfully_submitted = self.get_text(self.locators.REVIEW_SUCCESSFULLY_SUBMITTED)
            return review_successfully_submitted
        except TimeoutException as ex:
            print("TimeoutException, и будет проба проверить на ошибку заполненных полей")
            print("Exception has been thrown. " + str(ex))
            pass

    @allure.feature('tc_01_15_01 - Checking if a message about the successful submission for moderation of the review appears')
    def review_have_been_send_not_correctly(self):
        """Checking if a message about NOT successful submission for moderation of the review appears"""
        time.sleep(2)
        try:
            print("Something went wrong: One of the 3 fields is not filled or the star is not pressed")
            review_not_successfully_submitted = self.get_text(self.locators.MESSAGE_ERROR)
            return review_not_successfully_submitted
        except:
            print("Something went wrong: One of the 3 fields is not filled or the star is not pressed")
