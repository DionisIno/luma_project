import allure
from selenium.common import TimeoutException

from pages.base_page import BasePage
from locators.reviews_page_locators import ReviewsPageLocators
import time


class ReviewsPage(BasePage):
    locators = ReviewsPageLocators

    def open_review_menu(self):
        """Click on review menu"""
        review_menu = self.element_is_clickable(self.locators.REVIEW_MENU)
        review_menu.click()

    @allure.feature('tc_01_15_01 - Click on element 1 star')
    def one_star_review_correct(self):
        """Click on element 1 star"""
        one_star_element = self.element_is_clickable(self.locators.STAR_1)
        one_star_element.click()

    @allure.feature('tc_01_15_01 - Entering data into the nickname input')
    def nickname_input_review_correct(self):
        """Entering data into the nickname input"""
        nickname_input_element = self.element_is_clickable(self.locators.NICKNAME_INPUT)
        nickname_input_element.click()
        nickname_input_element.clear()
        nickname_input_element.send_keys('Some Name')

    @allure.feature('tc_01_15_01 - Entering data into input summary')
    def summary_input_review_correct(self):
        """Entering data into input summary"""
        summary_input_element = self.element_is_clickable(self.locators.SUMMARY_INPUT)
        summary_input_element.click()
        summary_input_element.clear()
        summary_input_element.send_keys('Some Summary Text')

    @allure.feature('tc_01_15_01 - Entering data into input review')
    def review_input_review_correct(self):
        """Entering data into input review"""
        review_input_element = self.element_is_clickable(self.locators.REVIEW_INPUT)
        review_input_element.click()
        review_input_element.clear()
        review_input_element.send_keys('Some Review Text')

    def record_screen_on_demand_function(self):
        self.record_screen_on_demand()

    @allure.feature('tc_01_15_01 - Click on the send feedback button')
    def send_review_correct(self):
        """Click on the send feedback button"""
        self.action_move_to_element_click_no_new_window(self.locators.SUBMIT_REVIEW_BUTTON)

    @allure.feature('tc_01_15_01 - Just some wait')
    def some_wait(self):
        """Just some wait"""

    def see_all_opened_windows(self):
        self.show_all_opened_windows()

    def switch_between_opened_windows_to_base_one(self):
        self.switch_between_opened_windows()

    @allure.feature('tc_01_15_01 - Checking if a message about the successful submission for moderation of the review appears')
    def review_have_been_send_correctly(self):
        """
        Checking if a message about the successful submission for moderation of the review appears
        Validates text within a message
        """
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
        try:
            print("Something went wrong: One of the 3 fields is not filled or the star is not pressed")
            review_not_successfully_submitted = self.get_text(self.locators.MESSAGE_ERROR)
            return review_not_successfully_submitted
        except:
            print("Something went wrong: One of the 3 fields is not filled or the star is not pressed")
