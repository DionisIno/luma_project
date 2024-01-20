import allure
import pytest

from data.data_urls import VIDEO_DOWNLOAD_PAGE_URL
from pages.training_video_download_page import TrainingVideoDownloadPage


@allure.epic('Test Training Video')
class TestTrainingVideoDownload:

    @allure.title('TC 18.01.01 subtitle is displayed text compare products')
    def test_tc_18_01_01_subtitle_is_displayed_text_compare_products(self, driver):
        """Verify the 'Compare Products' subtitle is visible"""
        page = TrainingVideoDownloadPage(driver, VIDEO_DOWNLOAD_PAGE_URL)
        page.open()
        text = page.subtitle_is_displayed_text_compare_products()
        assert text == "Compare Products", "The 'Compare Products' subtitle is not visible or contains incorrect text"

    @allure.title('TC 18.01.02 subtitle is displayed text My Wish List')
    def test_tc_18_01_02_subtitle_is_displayed_text_my_wish_list(self, driver):
        """Verify the 'My Wish List' subtitle is visible"""
        page = TrainingVideoDownloadPage(driver, VIDEO_DOWNLOAD_PAGE_URL)
        page.open()
        text = page.subtitle_is_displayed_text_my_wish_list()
        assert text == "My Wish List", "The 'My Wish List' subtitle is not visible or contains incorrect text"

    @allure.title('TC 18.01.03 message "You have no items to compare." is displayed')
    def test_tc_18_01_03_message_no_items_to_compare_is_displayed(self, driver):
        """Verify message 'You have no items to compare.' is visible"""
        page = TrainingVideoDownloadPage(driver, VIDEO_DOWNLOAD_PAGE_URL)
        page.open()
        text = page.message_no_items_to_compare_is_displayed()
        assert text == "You have no items to compare.", "The compare message is not visible or contains incorrect text"

    @allure.title('TC 18.01.04 message no items to compare is displayed')
    def test_tc_18_01_04_message_no_items_in_your_with_list_is_displayed(self, driver):
        """Verify the message 'You have no items in your wish list.' is visible"""
        page = TrainingVideoDownloadPage(driver, VIDEO_DOWNLOAD_PAGE_URL)
        page.open()
        text = page.message_no_items_in_your_with_list_is_displayed()
        assert text == "You have no items in your wish list.", "The compare message is not visible or contains " \
                                                               "incorrect text"

    @allure.title('TC 18.02.01 title "Video Download" is visible')
    def test_tc_18_02_01_title_video_download_is_displayed(self, driver):
        """Verify title 'Video Download' is visible"""
        page = TrainingVideoDownloadPage(driver, VIDEO_DOWNLOAD_PAGE_URL)
        page.open()
        text = page.title_video_download_is_displayed()
        assert text == "Video Download", "The title 'Video Download' is not visible or contains incorrect text"

    @allure.title('TC 18.02.02 Verify message "We can not find products matching the selection." is visible')
    def test_tc_18_02_02_title_video_download_is_displayed(self, driver):
        """Verify message "We can not find products matching the selection." is visible"""
        page = TrainingVideoDownloadPage(driver, VIDEO_DOWNLOAD_PAGE_URL)
        page.open()
        text = page.message_we_can_not_find_products_is_displayed()
        assert text == "We can't find products matching the selection.", "The title 'Video Download' is not visible" \
                                                                         " or contains incorrect text"
