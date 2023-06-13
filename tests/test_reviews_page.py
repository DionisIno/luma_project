from selenium.webdriver.support import expected_conditions as EC
from locators.reviews_page_locators import ReviewsPageLocators

from selenium.webdriver.support.wait import WebDriverWait

from pages.reviews_page import ReviewsPage
from data.data_urls import REVIEWS_URL


class TestReviews:
    locators = ReviewsPageLocators

    def test_tc_01_15_01_check_that_it_is_possible_to_vote_for_1_star(self, driver):
        """
        The user is NOT logged in, located in the product card, section "Reviews"
        1. All required fields are filled with correct data
        2. Pressed 1 star
        3.The "Submit Review" button is pressed
        Result: Present in the DOM and visible on the page the message: "You submitted your review for moderation."
        """
        page = ReviewsPage(driver, REVIEWS_URL)
        page.open()
        page.one_star_review_correct()
        page.nickname_input_review_correct()
        page.summary_input_review_correct()
        page.review_input_review_correct()

        page.send_review_correct()

        """Wait for an element to appear"""
        # WebDriverWait(driver, 40).until(
        #     EC.visibility_of_element_located(self.locators.REVIEW_SUCCESSFULLY_SUBMITTED))
        """Checking the success message"""
        review_successfully_submitted = page.review_have_been_send_correctly()

        # page.click_submit_review()
        # page.review_have_been_send_correctly()

        # review_successfully_submitted = page.send_review_correct()

        # assert review_successfully_submitted, "Leave a review failed"
        # assert review_successfully_submitted.text == "You submitted your review for moderation.", "Leave a review failed"



