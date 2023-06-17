from data.data_urls import VIDEO_DOWNLOAD_PAGE_URL
from pages.training_video_download_page import TrainingVideoDownloadPage
import allure


@allure.epic('Test Training Video')
class TestTrainingVideoDownload:

    @allure.title('Tc 18 01 01 subtitle is displayed text compare products')
    def test_tc_18_01_01_subtitle_is_displayed_text_compare_products(self, driver):
        """Verify the 'Compare Products' subtitle is visible"""
        page = TrainingVideoDownloadPage(driver, VIDEO_DOWNLOAD_PAGE_URL)
        page.open()
        text = page.subtitle_is_displayed_text_compare_products()
        assert text == "Compare Products", "The 'Compare Products' subtitle is not visible or contains incorrect text"
