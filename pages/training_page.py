from pages.base_page import BasePage
from locators.training_page_locators import TrainingPageLocators
import allure


@allure.epic('Training Page')
class TrainingPage(BasePage):
    locators = TrainingPageLocators

    @allure.step('Check the Sidebar Shop By title is visible')
    def check_sidebar_panel_name(self):
        shop_by_text = self.element_is_visible(self.locators.SHOP_BY)
        return shop_by_text.text

