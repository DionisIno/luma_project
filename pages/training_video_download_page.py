from pages.base_page import BasePage
import allure
from locators.training_video_download_page_locators import TrainingVideoDownloadPageLocators


@allure.epic('Training Video Download Page')
class TrainingVideoDownloadPage(BasePage):
    """This class contains steps for testing Training Video Download Page"""
    training_video_download_locators = TrainingVideoDownloadPageLocators

    @allure.step('Subtitle is displayed text compare products')
    def subtitle_is_displayed_text_compare_products(self):
        """Verify subtitle is displayed text compare products"""
        text = self.element_is_visible(self.training_video_download_locators.COMPARE_PRODUCTS)
        return text.text if text else None

    @allure.step('Subtitle is displayed text my wish list')
    def subtitle_is_displayed_text_my_wish_list(self):
        """Verify subtitle is displayed text my wish list"""
        text = self.element_is_visible(self.training_video_download_locators.MY_WISH_LIST)
        return text.text if text else None

    @allure.step('Message no item is displayed')
    def message_no_items_to_compare_is_displayed(self):
        """Verify message no item is displayed """
        text = self.element_is_visible(self.training_video_download_locators.COMPARE_MESSAGE)
        return text.text if text else None

    @allure.step('Message no items in your with list is displayed')
    def message_no_items_in_your_with_list_is_displayed(self):
        """Verify message no items in your with list is displayed"""
        text = self.element_is_visible(self.training_video_download_locators.MY_WISH_LIST_MESSAGE)
        return text.text if text else None

    @allure.step('Verify title "Video Download" is visible')
    def title_video_download_is_displayed(self):
        """Verify title "Video Download" is visible"""
        text = self.element_is_visible(self.training_video_download_locators.HEAD_TEXT)
        return text.text if text else None

    @allure.step('Verify message "We can not find products matching the selection." is displayed')
    def message_we_can_not_find_products_is_displayed(self):
        """Verify message "We can not find products matching the selection." is visible"""
        text = self.element_is_visible(self.training_video_download_locators.NO_PRODUCTS_MESSAGE)
        return text.text if text else None
