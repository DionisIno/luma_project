from data.data_urls import SALE_PAGE_URL, WHAT_IS_NEW_PAGE_URL, GEAR_PAGE_URL, BAGS_PAGE_URL, WATCHES_PAGE_URL
from data.data_urls import TRAINING_PAGE_URL, VIDEO_DOWNLOAD_PAGE_URL, WOMEN_PAGE_URL, FITNESS_EQUIPMENT_PAGE_URL
from locators.common_locators import CommonLocators
from locators.header_page_locators import HeaderPageLocators
from locators.create_account_page_locators import CreateAccountPageLocators
from locators.sign_in_page_locators import SingInPageLocators
from pages.base_page import BasePage
from locators.training_page_locators import TrainingPageLocators
from locators.training_video_download_page_locators import TrainingVideoDownloadPageLocators
from locators.women_page_locators import WomenPageLocators
from locators.what_is_new_page_locators import WhatIsNewPageLocators
from locators.sale_page_locators import MainContentPromoBlocks
from locators.gear_page_locators import SideBarLocators
from locators.bags_page_locators import BagsPageLocators
from locators.fitness_equipment_page_locators import FitnessEquipmentPageLocators
from locators.watches_page_locators import WatchesPageLocators
import allure


@allure.epic('Header Page')
class HeaderPage(BasePage):
    header_locators = HeaderPageLocators
    create_account_locators = CreateAccountPageLocators
    sign_in_locators = SingInPageLocators
    training_locators = TrainingPageLocators
    training_video_locators = TrainingVideoDownloadPageLocators
    women_locators = WomenPageLocators
    what_is_new_locators = WhatIsNewPageLocators
    sale_locators = MainContentPromoBlocks
    gear_locators = SideBarLocators
    common_locators = CommonLocators
    bags_locators = BagsPageLocators
    fitness_equipment_locators = FitnessEquipmentPageLocators
    watches_locators = WatchesPageLocators

    @allure.step('Check greeting message in search field')
    def check_greeting_message(self):
        return self.element_is_visible(self.header_locators.GREETING_MESSAGE)

    @allure.step('Check h1 header is visible')
    def check_common_header(self):
        return self.element_is_visible(self.common_locators.HEADER_PAGE)

    @allure.step('Redirected the link "Sale"')
    def redirected_the_link_sale(self):
        """Verify correct redirection from the link 'Sale'"""
        element = self.element_is_visible(self.header_locators.SALE)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.sale_locators.HEAD_TEXT)
        return url == SALE_PAGE_URL and text == "Sale"

    @allure.step('Check message appears after clicking on an empty cart')
    def check_cart_message(self):
        return self.element_is_visible(self.header_locators.CART_BUTTON_MESSAGE).text

    @allure.step('Check "Search" field contains the placeholder')
    def check_search_field(self):
        return self.element_is_visible(self.header_locators.SEARCH_FIELD).get_attribute('placeholder')

    @allure.step('Check "Search" field dropdown')
    def enter_search_field_and_get_dropdown(self):
        """
        This method activates the field "Search", enters the term "T-shirt" in the field "Search"
        and returns the combo box that appears after you enter the search term.
        """
        search_field = self.click_and_return_element(self.header_locators.SEARCH_FIELD)
        search_field.send_keys("T-shirt")
        return self.elements_are_visible(self.header_locators.SEARCH_DROPDOWN)

    @allure.step('Check "Search" field activation style')
    def activate_search_field_and_check_style(self):
        """
        This method activates the field "Search" and checks if the style of the field changes upon activation.
        It returns the styles before and after activation for comparison.
        """
        initial_box_shadow = self.check_element_hover_style(self.header_locators.SEARCH_FIELD, 'box-shadow', 5)
        self.click_and_return_element(self.header_locators.SEARCH_FIELD)
        active_box_shadow = self.check_element_hover_style(self.header_locators.SEARCH_FIELD, 'box-shadow', 5)
        return initial_box_shadow, active_box_shadow

    @allure.step('Link "Sale" is visible and interactive')
    def link_sale_is_visible_and_interactive(self):
        """Verify the link 'Sale' is visible and interactive"""
        element = self.element_is_visible(self.header_locators.SALE)
        clickable = self.element_is_clickable(element)
        interactive = self.check_element_hover_style(self.header_locators.SALE, 'pointer', 1)
        return element, clickable, interactive

    @allure.step('Redirected the link "Training"')
    def redirected_the_link_training(self):
        """Verify correct redirection from the link 'Training'"""
        element = self.element_is_visible(self.header_locators.TRAINING)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.training_locators.HEAD_TEXT)
        return url == TRAINING_PAGE_URL and text == "Training"

    @allure.step('Redirected the link "Training - Video Download"')
    def redirected_the_link_training_video_download(self):
        """Verify correct redirection from the link 'Training - Video Download'"""
        self.element_is_visible(self.header_locators.TRAINING)
        self.check_element_hover_style(self.header_locators.TRAINING, 'pointer', 1)
        element = self.element_is_present(self.header_locators.VIDEO_DOWNLOAD)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.training_video_locators.HEAD_TEXT)
        return url == VIDEO_DOWNLOAD_PAGE_URL and text == "Video Download"

    @allure.step('Link "Training - Video Download" is visible and interactive')
    def link_training_is_visible_and_interactive(self):
        """Verify the link 'Training - Video Download' is visible and interactive"""
        self.element_is_visible(self.header_locators.TRAINING)
        interactive = self.check_element_hover_style(self.header_locators.TRAINING, 'pointer', 1)
        element = self.element_is_visible(self.header_locators.VIDEO_DOWNLOAD)
        return element, interactive

    @allure.step('Link "What is New" is visible and interactive')
    def link_what_is_new_is_visible_and_interactive(self):
        """Verify the link 'What is New' is visible and interactive"""
        element = self.element_is_visible(self.header_locators.WHAT_IS_NEW)
        clickable = self.element_is_clickable(element)
        interactive = self.check_element_hover_style(self.header_locators.WHAT_IS_NEW, 'pointer', 1)
        return element, clickable, interactive

    @allure.step('Redirection of the link "Women"')
    def redirection_of_the_link_women(self):
        element = self.element_is_visible(self.header_locators.WOMEN)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.women_locators.WOMEN_HEAD_TEXT)
        return url == WOMEN_PAGE_URL and text == "Women"

    @allure.step('Redirected the link "What is New"')
    def redirected_the_link_what_is_new(self):
        """Verify correct redirection from the link 'What is New'"""
        element = self.element_is_visible(self.header_locators.WHAT_IS_NEW)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.what_is_new_locators.HEAD_TEXT)
        return url == WHAT_IS_NEW_PAGE_URL and text == "What's New"

    @allure.step('Link "Gear" is visible and interactive')
    def link_gear_is_visible_and_interactive(self):
        """Verify the link 'Gear' is visible and interactive"""
        element = self.element_is_visible(self.header_locators.GEAR)
        clickable = self.element_is_clickable(element)
        interactive = self.check_element_hover_style(self.header_locators.GEAR, 'pointer', 1)
        element_bags = self.element_is_visible(self.header_locators.BAGS)
        element_fitness_equipment = self.element_is_visible(self.header_locators.FITNESS_EQUIPMENT)
        element_watches = self.element_is_visible(self.header_locators.WATCHES)
        return element, clickable, interactive, element_bags, element_fitness_equipment, element_watches

    @allure.step('Check "Bottom" subsection of "Men" section')
    def check_men_bottoms_subsection(self):
        """This method moves the cursor over the 'Men' section, then over the 'Bottoms' subsection
        and returns the 'Pants' and 'Shorts' subsections."""
        self.action_move_to_element(self.element_is_visible(self.header_locators.MEN_SECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.BOTTOMS_SUBSECTION))
        return self.element_is_visible(self.header_locators.BOTTOMS_SUBSECTIONS)

    @allure.step('Check the "Bottoms" link of the "Men" section')
    def check_men_bottoms_subsection_link(self):
        self.action_move_to_element(self.element_is_visible(self.header_locators.MEN_SECTION))
        self.click_and_return_element(self.header_locators.BOTTOMS_SUBSECTION)
        return self.element_is_visible(self.common_locators.HEADER_PAGE)

    @allure.step('Check the "Pants" link of the "Men" section')
    def check_men_pants_subsection_link(self):
        self.action_move_to_element(self.element_is_visible(self.header_locators.MEN_SECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.BOTTOMS_SUBSECTION))
        self.click_and_return_element(self.header_locators.PANTS)
        return self.element_is_visible(self.common_locators.HEADER_PAGE)

    @allure.step('Check the "Shorts" link of the "Men" section')
    def check_men_shorts_subsection_link(self):
        """Verify the link 'Shorts' is visible and interactive"""
        self.action_move_to_element(self.element_is_visible(self.header_locators.MEN_SECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.BOTTOMS_SUBSECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.PANTS))
        self.click_and_return_element(self.header_locators.SHORTS)
        return self.element_is_visible(self.common_locators.HEADER_PAGE)

    @allure.step('Check the "Men" section link')
    def check_men_section_link(self):
        """Verify the link 'Men' is visible and interactive"""
        self.action_move_to_element(self.element_is_visible(self.header_locators.MEN_SECTION))
        return self.element_is_visible(self.header_locators.TOPS_BOTTOMS_SUBSECTION)

    @allure.step('Redirected the link "Gear"')
    def redirected_the_link_gear(self):
        """Verify correct redirection from the link 'Gear'"""
        element = self.element_is_visible(self.header_locators.GEAR)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.gear_locators.HEAD_TEXT)
        return url == GEAR_PAGE_URL and text == "Gear"

    @allure.step('Redirected the link "Gear - Bags"')
    def redirected_the_link_gear_bags(self):
        """Verify correct redirection from the link 'Gear - Bags'"""
        self.element_is_visible(self.header_locators.GEAR)
        self.check_element_hover_style(self.header_locators.GEAR, 'pointer', 1)
        element = self.element_is_visible(self.header_locators.BAGS)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.bags_locators.HEAD_TEXT)
        return url == BAGS_PAGE_URL and text == "Bags"

    @allure.step('Redirected the link "Gear - Fitness - Equipment"')
    def redirected_the_link_gear_fitness_equipment(self):
        """Verify correct redirection from the link 'Gear - Fitness - Equipment'"""
        self.element_is_visible(self.header_locators.GEAR)
        self.check_element_hover_style(self.header_locators.GEAR, 'pointer', 1)
        element = self.element_is_visible(self.header_locators.FITNESS_EQUIPMENT)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.fitness_equipment_locators.HEAD_TEXT)
        return url == FITNESS_EQUIPMENT_PAGE_URL and text == "Fitness Equipment"

    @allure.step('Redirected the link "Gear - Watches"')
    def redirected_the_link_gear_watches(self):
        """Verify correct redirection from the link 'Gear - Watches'"""
        self.element_is_visible(self.header_locators.GEAR)
        self.check_element_hover_style(self.header_locators.GEAR, 'pointer', 1)
        element = self.element_is_visible(self.header_locators.WATCHES)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.watches_locators.HEAD_TEXT)
        return url == WATCHES_PAGE_URL and text == "Watches"

    @allure.step('Check redirection of the "Men" section link')
    def check_redirection_of_men_section_link(self):
        self.element_is_visible(self.header_locators.MEN_SECTION).click()
        return self.element_is_visible(self.common_locators.HEADER_PAGE)

    @allure.step('Check the "Tops" link of the "Men" section')
    def check_men_tops_subsection(self):
        """This method moves the cursor over the 'Men' section, then over the 'Tops' subsection
        and returns subsection contains 'Jackets', 'Shorts', 'Hoodies & Sweatshirts', 'Tees' and 'Tanks' subsections"""
        self.action_move_to_element(self.element_is_visible(self.header_locators.MEN_SECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.TOPS_SUBSECTION))
        return self.element_is_visible(self.header_locators.TOPS_SUBSECTIONS)

    @allure.step('User authorization')
    def user_authorization(self):
        """This method performs user authorization by entering the email and password,
        and clicking on the sign-in button. It returns True if the sign-in element becomes not visible"""
        self.element_is_visible(self.header_locators.SIGN_IN).click()
        self.element_is_visible(self.sign_in_locators.CUSTOMER_EMAIL).send_keys("qwerty@mail.com")
        self.element_is_visible(self.sign_in_locators.CUSTOMER_PASSWORD).send_keys("1234qwer!")
        self.element_is_visible(self.sign_in_locators.SIGN_IN_BUTTON).click()
        return self.element_is_not_visible(self.header_locators.SIGN_IN)

    @allure.step('Check redirection of the "Tops" subsection of "Men" section link')
    def check_redirection_of_tops_subsection_of_men_section_link(self):
        """This method checks the redirection of the 'Tops' subsection link of the 'Men' section.
        It moves the cursor over the 'Men' section, clicks on the 'Tops' subsection link,
        and returns the visibility of the header page element"""
        self.action_move_to_element(self.element_is_visible(self.header_locators.MEN_SECTION))
        self.element_is_visible(self.header_locators.TOPS_SUBSECTION).click()
        return self.element_is_visible(self.common_locators.HEADER_PAGE)

    @allure.step('Check redirection of the "Jackets" subsection of "Men" section link')
    def check_redirection_of_jackets_subsection_of_men_section_link(self):
        """This method checks the redirection of the 'Jackets' subsection link of the 'Men' section.
        It moves the cursor over the 'Men' section, then 'Tops' and clicks on the 'Jackets' subsection link,
        and returns the visibility of the header page element"""
        self.action_move_to_element(self.element_is_visible(self.header_locators.MEN_SECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.TOPS_SUBSECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.JACKETS_SUBSECTION))
        self.element_is_visible(self.header_locators.JACKETS_SUBSECTION).click()
        return self.element_is_visible(self.common_locators.HEADER_PAGE)

    @allure.step('Check redirection of the "Hoodies & Sweatshirts" subsection of "Men" section link')
    def check_redirection_of_hoodies_subsection_of_men_section_link(self):
        """This method checks the redirection of the 'Hoodies & Sweatshirts' subsection link of the 'Men' section.
        It moves the cursor over the 'Men' section, then 'Tops' and clicks on the 'Hoodies & Sweatshirts' subsection link,
        and returns the visibility of the header page element"""
        self.action_move_to_element(self.element_is_visible(self.header_locators.MEN_SECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.TOPS_SUBSECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.JACKETS_SUBSECTION))
        self.element_is_visible(self.header_locators.HOODIES_SWEATSHIRTS_SUBSECTION).click()
        return self.element_is_visible(self.common_locators.HEADER_PAGE)

    @allure.step('Check redirection of the "Tees" subsection of "Men" section link')
    def check_redirection_of_tees_subsection_of_men_section_link(self):
        """This method checks the redirection of the 'Tees' subsection link of the 'Men' section.
        It moves the cursor over the 'Men' section, then 'Tops' and clicks on the 'Tees' subsection link,
        and returns the visibility of the header page element"""
        self.action_move_to_element(self.element_is_visible(self.header_locators.MEN_SECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.TOPS_SUBSECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.JACKETS_SUBSECTION))
        self.element_is_visible(self.header_locators.TEES_SUBSECTION).click()
        return self.element_is_visible(self.common_locators.HEADER_PAGE)

    @allure.step('Check redirection of the "Tanks" subsection of "Men" section link')
    def check_redirection_of_tanks_subsection_of_men_section_link(self):
        """This method checks the redirection of the 'Tanks' subsection link of the 'Men' section.
        It moves the cursor over the 'Men' section, then 'Tops' and clicks on the 'Tees' subsection link,
        and returns the visibility of the header page element"""
        self.action_move_to_element(self.element_is_visible(self.header_locators.MEN_SECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.TOPS_SUBSECTION))
        self.action_move_to_element(self.element_is_visible(self.header_locators.JACKETS_SUBSECTION))
        self.element_is_visible(self.header_locators.TANKS_SUBSECTION).click()
        return self.element_is_visible(self.common_locators.HEADER_PAGE)
