from selenium.webdriver.support.wait import WebDriverWait as wait, WebDriverWait
from data.data_urls import MEN_TOPS_URL, MEN_BOTTOMS_URL, MEN_JACKETS_URL, MEN_TEES_URL, MEN_TANKS_URL
from locators.men_page_locators import MenPageLocators
from pages.base_page import BasePage
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

    @allure.step('Correct redirection of the link "Bottoms" on Men page')
    def verify_bottoms_redirects_to_a_correct_page(self):
        """This method finds 'Bottoms' link and verifies it is correctly redirects to a new page"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_BOTTOMS)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.side_bar_locators.MEN_SUBHEAD_TEXT_BOTTOMS)
        return url == MEN_BOTTOMS_URL and text == "Bottoms"

    @allure.step('Verify subhead "TOPS" on Men page')
    def verify_subhead_tops_is_visible(self):
        """This method finds subhead 'TOPS' and verifies it is correctly displayed"""
        subhead_title = self.element_is_visible(self.side_bar_locators.SIDE_BAR_SUBHEAD_TOPS)
        text_title = subhead_title.text
        return text_title

    @allure.step("Find clickable elements link 'Jackets' on Men page")
    def verify_jackets_link_is_visible_and_clickable(self):
        """This method finds 'Jackets' link and verifies it is clickable"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_JACKETS)
        wait(self.driver, 15)
        element.click()
        return element

    @allure.step('Verify header "Men" on Men page')
    def verify_header_men_is_visible(self):
        """This method finds header 'Men' and verifies it is correctly displayed"""
        subhead_title = self.element_is_visible(self.side_bar_locators.SIDE_BAR_HEADER_MEN)
        text_title = subhead_title.text
        return text_title

    @allure.step('Correct redirection of the link "Jackets" on Men page')
    def verify_jackets_redirects_to_a_correct_page(self):
        """This method finds 'Jackets' link and verifies it is correctly redirects to a new page"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_JACKETS)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.side_bar_locators.MEN_SUBHEAD_TEXT_JACKETS)
        return url == MEN_JACKETS_URL and text == "Jackets"

    @allure.step("Find clickable elements link 'Tees' on Men page")
    def verify_tees_link_is_visible_and_clickable(self):
        """This method finds 'Tees' link and verifies it is clickable"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_TEES)
        wait(self.driver, 15)
        element.click()
        return element

    @allure.step('Correct redirection of the link "Tees" on Men page')
    def verify_tees_redirects_to_a_correct_page(self):
        """This method finds 'Tees' link and verifies it is correctly redirects to a new page"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_TEES)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.side_bar_locators.MEN_SUBHEAD_TEXT_TEES)
        return url == MEN_TEES_URL and text == "Tees"

    @allure.step("Find clickable elements link 'Tanks' on Men page")
    def verify_tanks_link_is_visible_and_clickable(self):
        """This method finds 'Tanks' link and verifies it is clickable"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_TANKS)
        wait(self.driver, 15)
        element.click()
        return element

    @allure.step('Correct redirection of the link "Tanks" on Men page')
    def verify_tanks_redirects_to_a_correct_page(self):
        """This method finds 'Tanks' link and verifies it is correctly redirects to a new page"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_TANKS)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.side_bar_locators.MEN_SUBHEAD_TEXT_TANKS)
        return url == MEN_TANKS_URL and text == "Tanks"

    @allure.step("Find clickable elements link 'Hoodies&Sweatshirts' on Men page")
    def verify_hoodies_link_is_visible_and_clickable(self):
        """This method finds 'Hoodies&Sweatshirts' link and verifies it is clickable"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_HOODIES)
        wait(self.driver, 15)
        element.click()
        return element
