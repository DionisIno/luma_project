from pages.base_page import BasePage
import allure
from locators.training_video_download_page_locators import TrainingVideoDownloadPageLocators


@allure.epic('Training Video Download Page')
class TrainingVideoDownloadPage(BasePage):
    training_video_download_locators = TrainingVideoDownloadPageLocators

    @allure.step('Subtitle is displayed text compare products')
    def subtitle_is_displayed_text_compare_products(self):
        text = self.element_is_visible(self.training_video_download_locators.COMPARE_PRODUCTS)
        return text.text if text else None

    @allure.step('Subtitle is displayed text my wish list')
    def subtitle_is_displayed_text_my_wish_list(self):
        text = self.element_is_visible(self.training_video_download_locators.MY_WISH_LIST)
        return text.text if text else None

    @allure.step('Message no item is displayed')
    def message_no_items_to_compare_is_displayed(self):
        text = self.element_is_visible(self.training_video_download_locators.COMPARE_MESSAGE)
        return text.text if text else None

    @allure.step('Message no items in your with list is displayed')
    def message_no_items_in_your_with_list_is_displayed(self):
        text = self.element_is_visible(self.training_video_download_locators.MY_WISH_LIST_MESSAGE)
        return text.text if text else None
