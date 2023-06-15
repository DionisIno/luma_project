from pages.base_page import BasePage
from locators.training_page_locators import TrainingPageLocators
import allure


@allure.epic('Training Page')
class TrainingPage(BasePage):
    locators = TrainingPageLocators

    @allure.step('Check the Sidebar Shop By title is visible and contains text "Shop By"')
    def check_sidebar_panel_shop_by(self):
        shop_by = self.element_is_visible(self.locators.SHOP_BY)
        return shop_by.text

    @allure.step('Check the Sidebar Category title is visible and contains text "Category"')
    def check_sidebar_panel_category(self):
        category = self.element_is_visible(self.locators.CATEGORY)
        return category.text

    @allure.step('Check the Sidebar Video Download is visible and contains text "Video Download"')
    def check_sidebar_panel_video_download(self):
        video_download = self.element_is_visible(self.locators.VIDEO_DOWNLOAD)
        return video_download.text

    @allure.step('Check the Sidebar Video Download is visible and contains URL')
    def check_sidebar_panel_video_download_href(self):
        video_download = self.element_is_visible(self.locators.VIDEO_DOWNLOAD)
        return video_download.get_attribute("href")

    @allure.step('Check the Sidebar Compare Products is visible and contains text "Compare Products"')
    def check_sidebar_panel_compare_products(self):
        compare_products = self.element_is_visible(self.locators.COMPARE_PRODUCTS)
        return compare_products.text

    @allure.step('Check the Sidebar My Wish List is visible and contains text "My Wish List"')
    def check_sidebar_panel_my_wish_list(self):
        my_wish_list = self.element_is_visible(self.locators.MY_WISH_LIST)
        return my_wish_list.text
