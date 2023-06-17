from data.data_urls import VIDEO_DOWNLOAD_PAGE_URL
from pages.training_video_download_page import TrainingVideoDownloadPage
import allure


@allure.epic('Test Training Video')
class TestTrainingVideoDownload:

    @allure.title('Tc 18.01.01 subtitle is displayed text compare products')
    def test_tc_18_01_01_subtitle_is_displayed_text_compare_products(self, driver):
        """Verify the 'Compare Products' subtitle is visible"""
        page = TrainingVideoDownloadPage(driver, VIDEO_DOWNLOAD_PAGE_URL)
        page.open()
        text = page.subtitle_is_displayed_text_compare_products()
        assert text == "Compare Products", "The 'Compare Products' subtitle is not visible or contains incorrect text"

    @allure.title('Tc 18.01.02 subtitle is displayed text My Wish List')
    def test_tc_18_01_02_subtitle_is_displayed_text_my_wish_list(self, driver):
        """Verify the 'My Wish List' subtitle is visible"""
        page = TrainingVideoDownloadPage(driver, VIDEO_DOWNLOAD_PAGE_URL)
        page.open()
        text = page.subtitle_is_displayed_text_my_wish_list()
        assert text == "My Wish List", "The 'My Wish List' subtitle is not visible or contains incorrect text"
