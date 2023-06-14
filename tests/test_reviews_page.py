from selenium.webdriver.support import expected_conditions as EC
from locators.reviews_page_locators import ReviewsPageLocators

from selenium.webdriver.support.wait import WebDriverWait

from pages.reviews_page import ReviewsPage
from data.data_urls import REVIEWS_URL_DIRECT_ANCHOR_LINK, REVIEWS_URL_GENERAL


class TestReviews:
    locators = ReviewsPageLocators

    def test_tc_01_15_01_check_that_it_is_possible_to_vote_for_1_star(self, driver):
        """
        The user is NOT logged in, located in the product card, section "Reviews"
        1. All required fields are filled with correct data
        2. Pressed 1 star
        3.The "Submit Review" button is pressed
        Result: Present in the DOM and visible on the page the message: "You submitted your review for moderation."
        This code works when run on Win, Mac, Ubuntu on a real laptop and has the features of working on GitHub Action.
        When interacting with the GitHub Action, it checks not for the text of the "Success" message, but for the "Success" URL"
        """

        """Steps"""
        page = ReviewsPage(driver, REVIEWS_URL_GENERAL)
        page.open()

        """Get the current URL and print it"""
        current_url = driver.current_url
        print("Current URL:", current_url)

        """Steps"""
        page.open_review_menu()
        page.star_1_review_correct()
        page.nickname_input_review_correct()
        page.summary_input_review_correct()
        page.review_input_review_correct()

        """Button click"""
        page.send_review_correct()

        """Check URL for CI GitHub Action"""
        page.see_all_opened_windows()
        page.switch_between_opened_windows_to_base_one()

        """Checking the success message"""
        review_successfully_submitted = page.review_have_been_send_correctly()

        """Get the current URL and print it
        The variable is requested first for comparison, now for use in an assertion for a GitHub Action"""
        current_url = driver.current_url
        print("Current URL:", current_url)

        if review_successfully_submitted == "You submitted your review for moderation.":
            print('review_successfully_submitted', ' "Success" = Review sent successfully!')
            assert review_successfully_submitted == "You submitted your review for moderation.", "Leave a review failed"

        elif 'https://magento.softwaretestingboard.com/review/product/post/id' in current_url:
            print('review_successfully_submitted', ' "Success" = Review sent successfully!')
            print('The review is recorded at the address and under the number: ', current_url)
            assert 'https://magento.softwaretestingboard.com/review/product/post/id' in current_url, "Leave a review failed"

        else:
            print('Leave a review failed')
            assert review_successfully_submitted == "You submitted your review for moderation." or 'https://magento.softwaretestingboard.com/review/product/post/id' in current_url, "Leave a review failed"

    def test_tc_01_15_02_check_that_it_is_possible_to_vote_for_2_star(self, driver):
        """
        The user is NOT logged in, located in the product card, section "Reviews"
        1. All required fields are filled with correct data
        2. Pressed 2 star
        3.The "Submit Review" button is pressed
        Result: Present in the DOM and visible on the page the message: "You submitted your review for moderation.
        This code works when run on Win, Mac, Ubuntu on a real laptop and has the features of working on GitHub Action.
        When interacting with the GitHub Action, it checks not for the text of the "Success" message, but for the "Success" URL"
        """

        """Steps"""
        page = ReviewsPage(driver, REVIEWS_URL_GENERAL)
        page.open()

        """Get the current URL and print it"""
        page.get_the_current_URL_and_print_it()

        """Steps"""
        page.open_review_menu()
        page.star_2_review_correct()
        page.nickname_input_review_correct()
        page.summary_input_review_correct()
        page.review_input_review_correct()

        """Button click"""
        page.send_review_correct()

        """Check URL for CI GitHub Action"""
        page.see_all_opened_windows()
        page.switch_between_opened_windows_to_base_one()

        """Checking the success message"""
        # Checking if there are empty fields or an unpressed star
        page.checking_for_blank_fields_or_an_unpressed_star()
        # Checking if the feedback was sent successfully
        review_successfully_submitted = page.review_have_been_send_correctly()

        """Get the current URL and print it
        The variable is requested first for comparison, now for use in an assertion for a GitHub Action"""
        result_CI_GitHub_Action_URL = page.get_the_current_URL_and_print_it()

        if review_successfully_submitted == "You submitted your review for moderation.":
            print('review_successfully_submitted', ' "Success" = Review sent successfully!')
            assert review_successfully_submitted == "You submitted your review for moderation.", "Leave a review failed"

        elif 'https://magento.softwaretestingboard.com/review/product/post/id' in result_CI_GitHub_Action_URL:
            print('review_successfully_submitted', ' "Success" = Review sent successfully!')
            print('The review is recorded at the address and under the number: ', result_CI_GitHub_Action_URL)
            assert 'https://magento.softwaretestingboard.com/review/product/post/id' in result_CI_GitHub_Action_URL, "Leave a review failed"

        else:
            print('Leave a review failed')
            assert review_successfully_submitted == "You submitted your review for moderation." or 'https://magento.softwaretestingboard.com/review/product/post/id' in result_CI_GitHub_Action_URL, "Leave a review failed"

