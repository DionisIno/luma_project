from data.data_urls import MEN_TOPS_URL, MEN_BOTTOMS_URL
from locators.men_page_locators import MenPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MenPage(BasePage):
    side_bar_locators = MenPageLocators

    @allure.step('Find clickable elements')
    def verify_tops_link_is_visible_and_clickable(self):
        """This method finds 'Tops' link and verifies it is clickable"""
        self.element_is_clickable(self.side_bar_locators.SIDE_BAR_TOPS)
        return wait(self.driver, 5).until(EC.element_to_be_clickable(self.side_bar_locators.SIDE_BAR_TOPS))

    @allure.step('Correct redirection of the link "Tops"')
    def verify_tops_link_redirects_to_a_correct_page(self):
        """This method finds 'Tops' link and verifies it is correctly redirects to a new page"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_TOPS)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.side_bar_locators.MEN_SUBHEAD_TEXT_TOPS)
        return url == MEN_TOPS_URL and text == "Tops"

    @allure.step("Find clickable elements link 'Bottoms' on Men page")
    def verify_bottoms_link_is_visible_and_clickable(self):
        """This method finds 'Bottoms' link and verifies it is clickable"""
        self.element_is_clickable(self.side_bar_locators.SIDE_BAR_BOTTOMS)
        return wait(self.driver, 5).until(EC.element_to_be_clickable(self.side_bar_locators.SIDE_BAR_BOTTOMS))

    @allure.step('Correct redirection of the link "Bottoms" on Men page')
    def verify_tops_bottoms_redirects_to_a_correct_page(self):
        """This method finds 'Bottoms' link and verifies it is correctly redirects to a new page"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_BOTTOMS)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.side_bar_locators.MEN_SUBHEAD_TEXT_BOTTOMS)
        return url == MEN_BOTTOMS_URL and text == "Bottoms"
