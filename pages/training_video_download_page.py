from pages.base_page import BasePage
import allure
from locators.training_video_page_download_locators import TrainingVideoDownloadPageLocators


@allure.epic('Training Video Download Page')
class TrainingVideoDownloadPage(BasePage):
    training_video_download_locators = TrainingVideoDownloadPageLocators

    @allure.step('Subtitle is displayed text_compare products')
    def subtitle_is_displayed_text_compare_products(self):
        text = self.element_is_visible(self.training_video_download_locators.COMPARE_PRODUCTS)
        return text.text if text else None
