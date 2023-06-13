from selenium.webdriver.support import expected_conditions as EC
from locators.reviews_page_locators import ReviewsPageLocators

from selenium.webdriver.support.wait import WebDriverWait

from pages.reviews_page import ReviewsPage
from data.data_urls import REVIEWS_URL, REVIEWS_URL_GENERAL


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

        """Steps"""
        page = ReviewsPage(driver, REVIEWS_URL_GENERAL)
        page.open()

        page.open_review_menu()
        page.one_star_review_correct()
        page.nickname_input_review_correct()
        page.summary_input_review_correct()
        page.review_input_review_correct()

        """Клик по кнопке"""
        page.send_review_correct()

        page.see_all_opened_windows()
        page.switch_between_opened_windows_to_base_one()

        """Checking the success message"""
        review_successfully_submitted = page.review_have_been_send_correctly()

        if review_successfully_submitted == "You submitted your review for moderation.":
            print('review_successfully_submitted', ' "Успех" = Ревью успешно отправлено!')
            assert review_successfully_submitted == "You submitted your review for moderation.", "Leave a review failed"

        elif 'https://magento.softwaretestingboard.com/review/product/post/id' in current_url:
            print('review_successfully_submitted', ' "Успех" = Ревью успешно отправлено!')
            print('Отзыв записан по адресу и под номером: ', current_url)
            assert 'https://magento.softwaretestingboard.com/review/product/post/id' in current_url, "Leave a review failed"

        else:
            print('Оставить ревью НЕ получилось')
            assert review_successfully_submitted == "You submitted your review for moderation." or 'https://magento.softwaretestingboard.com/review/product/post/id' in current_url, "Leave a review failed"

