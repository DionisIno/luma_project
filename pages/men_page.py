from selenium.webdriver.support.wait import WebDriverWait as wait, WebDriverWait
from data.data_urls import MEN_TOPS_URL, MEN_BOTTOMS_URL, MEN_JACKETS_URL, MEN_TEES_URL, MEN_TANKS_URL, MEN_HOODIES_URL, \
    MEN_BOTTOMS_PANTS_URL, MEN_BOTTOMS_SHORTS_URL
from locators.men_page_locators import MenPageLocators, MenPagePromoLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure


class MenPage(BasePage):
    side_bar_locators = MenPageLocators
    promo_locators = MenPagePromoLocators

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

    @allure.step('Correct redirection of the link "Hoodies&Sweatshirts" on Men page')
    def verify_hoodies_redirects_to_a_correct_page(self):
        """This method finds 'Hoodies&Sweatshirts' link and verifies it is correctly redirects to a new page"""
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(self.side_bar_locators.SIDE_BAR_HOODIES)
        )
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.side_bar_locators.MEN_SUBHEAD_TEXT_HOODIES)
        return url == MEN_HOODIES_URL and text == "Hoodies & Sweatshirts"

    @allure.step("Find clickable elements link 'Pants' on Men page")
    def verify_pants_link_is_visible_and_clickable(self):
        """This method finds 'Pants' link and verifies it is clickable"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_PANTS)
        wait(self.driver, 15)
        element.click()
        return element

    @allure.step('Correct redirection of the link "Pants" on Men page')
    def verify_pants_link_redirects_to_a_correct_page(self):
        """This method finds 'Pants' link and verifies it is correctly redirects to a new page"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_PANTS)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.side_bar_locators.MEN_SUBHEAD_TEXT_PANTS)
        return url == MEN_BOTTOMS_PANTS_URL and text == "Pants"

    @allure.step("Find clickable elements link 'Shorts' on Men page")
    def verify_shorts_link_is_visible_and_clickable(self):
        """This method finds 'Shorts' link and verifies it is clickable"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_SHORTS)
        wait(self.driver, 15)
        element.click()
        return element

    @allure.step('Correct redirection of the link "Shorts" on Men page')
    def verify_shorts_link_redirects_to_a_correct_page(self):
        """This method finds 'Pants' link and verifies it is correctly redirects to a new page"""
        element = self.element_is_visible(self.side_bar_locators.SIDE_BAR_SHORTS)
        element.click()
        url = self.driver.current_url
        text = self.get_text(self.side_bar_locators.MEN_SUBHEAD_TEXT_SHORTS)
        return url == MEN_BOTTOMS_SHORTS_URL and text == "Shorts"

    @allure.step('Verify subhead "BOTTOMS" on Men page')
    def verify_subhead_bottoms_is_visible(self):
        """This method finds subhead 'BOTTOMS' and verifies it is correctly displayed"""
        subhead_title = self.element_is_visible(self.side_bar_locators.SIDE_BAR_SUBHEAD_BOTTOMS)
        text_title = subhead_title.text
        return text_title

    @allure.step("Check display of the 'Luma shorts' block on Men page")
    def check_block_shorts_display(self):
        """Check visibility of the 'Luma shorts' block on Men page under the yellow block"""
        block_shorts = self.element_is_visible(self.promo_locators.LUMA_SHORTS_BLOCK)
        return block_shorts.is_displayed()

    @allure.step("Check display of the image in the 'Luma shorts' block on Men page")
    def check_block_shorts_image_display(self):
        """Check visibility of the 'Luma shorts' block on Men page under the yellow block"""
        element = self.element_is_visible(self.promo_locators.LUMA_SHORTS_BLOCK_IMG)
        block_shorts_image = element.get_attribute("src")
        return block_shorts_image

    @allure.step("Correct redirection of the click on the block 'Luma shorts' on Men page")
    def verify_block_shorts_link_redirects_to_a_correct_page(self):
        """This method verifies correct redirection to a new page after clicking on the block"""
        element = self.element_is_visible(self.promo_locators.LUMA_SHORTS_BLOCK)
        element.click()
        url = self.driver.current_url
        return url == MEN_BOTTOMS_SHORTS_URL

    @allure.step("Check display of the text-1 'Luma shorts' in the 'Luma shorts' block on Men page")
    def verify_block_shorts_text_1(self):
        """This method verifies correct display of the text-1 in the 'Luma shorts' block"""
        shorts_block_title1 = self.element_is_visible(self.promo_locators.LUMA_SHORTS_TITLE)
        shorts_block_title1_text = shorts_block_title1.text
        return shorts_block_title1_text

    @allure.step("Check display of the text-2 'Cool it now' in the 'Luma shorts' block on Men page")
    def verify_block_shorts_text_2(self):
        """This method verifies correct display of the text-2 in the 'Luma shorts' block"""
        shorts_block_title2 = self.element_is_visible(self.promo_locators.LUMA_SHORTS_TITLE_2)
        shorts_block_title2_text = shorts_block_title2.text
        return shorts_block_title2_text

    @allure.step("Check display of the text-3 'Shop Shorts' in the 'Luma shorts' block on Men page")
    def verify_block_shorts_text_3(self):
        """This method verifies correct display of the text-3 in the 'Luma shorts' block"""
        shorts_block_title3 = self.element_is_visible(self.promo_locators.LUMA_SHORTS_TITLE_3)
        shorts_block_title3_text = shorts_block_title3.text
        return shorts_block_title3_text

    @allure.step("Check display of the 'Luma tees' block on Men page")
    def check_block_tees_display(self):
        """Check visibility of the 'Luma tees' block on Men page under the yellow block"""
        block_tees = self.element_is_visible(self.promo_locators.LUMA_TEES_BLOCK)
        return block_tees.is_displayed()

    @allure.step("Check display of the image in the 'Luma tees' block on Men page")
    def check_block_tees_image_display(self):
        """Check visibility of the image of the 'Luma tees' block on Men page under the yellow block"""
        element = self.element_is_visible(self.promo_locators.LUMA_TEES_BLOCK_IMG)
        block_tees_image = element.get_attribute("src")
        return block_tees_image

    @allure.step("Check display of the text-1 'Luma tees' in the 'Luma tees' block on Men page")
    def verify_block_tees_text_1(self):
        """This method verifies correct display of the text-1 in the 'Luma tees' block"""
        tees_block_title1 = self.element_is_visible(self.promo_locators.LUMA_TEES_TITLE)
        tees_block_title1_text = tees_block_title1.text
        return tees_block_title1_text

    @allure.step("Check display of the text-2 'Grab a tee or two!' in the 'Luma tees' block on Men page")
    def verify_block_tees_text_2(self):
        """This method verifies correct display of the text-2 in the 'Luma tees' block"""
        tees_block_title2 = self.element_is_visible(self.promo_locators.LUMA_TEES_TITLE_2)
        tees_block_title2_text = tees_block_title2.text
        return tees_block_title2_text

    @allure.step("Check display of the text-3 'Shop Tees' in the 'Luma tees' block on Men page")
    def verify_block_tees_text_3(self):
        """This method verifies correct display of the text-3 in the 'Luma tees' block"""
        tees_block_title3 = self.element_is_visible(self.promo_locators.LUMA_TEES_TITLE_3)
        tees_block_title3_text = tees_block_title3.text
        return tees_block_title3_text

    @allure.step("Correct redirection of the click on the block 'Luma tees' on Men page")
    def verify_block_tees_link_redirects_to_a_correct_page(self):
        """This method verifies correct redirection to a new page after clicking on the block"""
        element = self.element_is_visible(self.promo_locators.LUMA_TEES_BLOCK)
        element.click()
        url = self.driver.current_url
        return url == MEN_TEES_URL

    @allure.step("Check display of the 'Luma hoodies' block on Men page")
    def check_block_hoodies_display(self):
        """Check visibility of the 'Luma hoodies' block on Men page under the 'Last chance block'"""
        block_hoodies = self.element_is_visible(self.promo_locators.LUMA_HOODIES_BLOCK)
        return block_hoodies.is_displayed()

    @allure.step("Check display of the image in the 'Luma hoodies' block on Men page")
    def check_block_hoodies_image_display(self):
        """Check visibility of the image of the 'Luma tees' block on Men page under the 'Last chance block'"""
        element = self.element_is_visible(self.promo_locators.LUMA_HOODIES_BLOCK_IMG)
        block_hoodies_image = element.get_attribute("src")
        return block_hoodies_image

    @allure.step("Check display of the text-1 'Luma hoodies' in the 'Luma hoodies' block on Men page")
    def verify_block_hoodies_text_1(self):
        """This method verifies correct display of the text-1 in the 'Luma hoodies' block"""
        hoodies_block_title1 = self.element_is_visible(self.promo_locators.LUMA_HOODIES_TITLE)
        hoodies_block_title1_text = hoodies_block_title1.text
        return hoodies_block_title1_text

    @allure.step("Check display of the text-2 'Dress for fitness' in the 'Luma hoodies' block on Men page")
    def verify_block_hoodies_text_2(self):
        """This method verifies correct display of the text-2 in the 'Luma hoodies' block"""
        hoodies_block_title2 = self.element_is_visible(self.promo_locators.LUMA_HOODIES_TITLE_2)
        hoodies_block_title2_text = hoodies_block_title2.text
        return hoodies_block_title2_text

    @allure.step("Check display of the text-3 'Shop Hoodies' in the 'Luma hoodies' block on Men page")
    def verify_block_hoodies_text_3(self):
        """This method verifies correct display of the text-3 in the 'Luma hoodies' block"""
        hoodies_block_title3 = self.element_is_visible(self.promo_locators.LUMA_HOODIES_TITLE_3)
        hoodies_block_title3_text = hoodies_block_title3.text
        return hoodies_block_title3_text

    @allure.step("Correct redirection of the click on the block 'Luma hoodies' on Men page")
    def verify_block_hoodies_link_redirects_to_a_correct_page(self):
        """This method verifies correct redirection to a new page after clicking on the block"""
        element = self.element_is_visible(self.promo_locators.LUMA_HOODIES_BLOCK)
        element.click()
        url = self.driver.current_url
        return url == MEN_HOODIES_URL

    @allure.step("Check display of the 'Last chance for pants' block on Men page")
    def check_block_last_chance_display(self):
        """Check visibility of the 'Last chance for pants' block on Men page"""
        block_last_chance = self.element_is_visible(self.promo_locators.LUMA_LAST_CHANCE_BLOCK)
        return block_last_chance.is_displayed()

    @allure.step("Check display of the image in the 'Last chance for pants' block on Men page")
    def check_block_last_chance_image_display(self):
        """Check visibility of the image of the 'Last chance' block on Men page"""
        element = self.element_is_visible(self.promo_locators.LUMA_LAST_CHANCE_BLOCK_BLOCK_IMG)
        block_last_chance_image = element.get_attribute("src")
        return block_last_chance_image

    @allure.step("Check display of the text-1 'Last chance for pants' in the 'Last chance for pants' block on Men page")
    def verify_block_last_chance_text_1(self):
        """This method verifies correct display of the text-1 in the 'Luma last chance' block"""
        last_chance_block_title1 = self.element_is_visible(self.promo_locators.LUMA_LAST_CHANCE_TITLE)
        last_chance_block_title1_text = last_chance_block_title1.text
        return last_chance_block_title1_text

    @allure.step("Check display of the text-2 'Take 20% OFF' in the 'Last chance for pants' block on Men page")
    def verify_block_last_chance_text_2(self):
        """This method verifies correct display of the text-2 in the 'Luma last chance' block"""
        last_chance_block_title2 = self.element_is_visible(self.promo_locators.LUMA_LAST_CHANCE_TITLE_2)
        last_chance_block_title2_text = last_chance_block_title2.text
        return last_chance_block_title2_text

    @allure.step("Check display of the text-3 'Shop Pants' in the 'Last chance for pants' block on Men page")
    def verify_block_last_chance_text_3(self):
        """This method verifies correct display of the text-3 in the 'Luma last chance' block"""
        last_chance_block_title3 = self.element_is_visible(self.promo_locators.LUMA_LAST_CHANCE_TITLE_3)
        last_chance_block_title3_text = last_chance_block_title3.text
        return last_chance_block_title3_text

    @allure.step("Correct redirection of the click on the block 'Last chance for pants' on Men page")
    def verify_block_last_chance_link_redirects_to_a_correct_page(self):
        """This method verifies correct redirection to a new page after clicking on the block"""
        element = self.element_is_visible(self.promo_locators.LUMA_LAST_CHANCE_BLOCK)
        element.click()
        url = self.driver.current_url
        return url == MEN_BOTTOMS_PANTS_URL

    @allure.step("Check display of the 'Save up to $24!' block on Men page")
    def check_block_save_display(self):
        """Check visibility of the 'Save up to $24!' block on Men page"""
        block_save = self.element_is_visible(self.promo_locators.LUMA_SAVE_BLOCK)
        return block_save.is_displayed()

    @allure.step("Check display of the image in the 'Save up to $24!' block on Men page")
    def check_block_save_image_display(self):
        """Check visibility of the image of the 'Save up to $24!' block on Men page"""
        element = self.element_is_visible(self.promo_locators.LUMA_SAVE_BLOCK_BLOCK_IMG)
        block_save_image = element.get_attribute("src")
        return block_save_image

    @allure.step("Check display of the text-1 'Save up to $24!' in the 'Save up to $24!' block on Men page")
    def verify_block_save_text_1(self):
        """This method verifies correct display of the text-1 in the 'Save up to $24!' block"""
        save_block_title1 = self.element_is_visible(self.promo_locators.LUMA_SAVE_TITLE)
        save_block_title1_text = save_block_title1.text
        return save_block_title1_text

    @allure.step("Check display of the text-2 'Buy 3 Luma tees' in the 'Save up to $24!' block on Men page")
    def verify_block_save_text_2(self):
        """This method verifies correct display of the text-2 in the 'Save up to $24!' block"""
        save_block_title2 = self.element_is_visible(self.promo_locators.LUMA_SAVE_TITLE_2)
        save_block_title2_text = save_block_title2.text
        return save_block_title2_text

    @allure.step("Check display of the text-3 'Shop Tees' in the 'Save up to $24!' block on Men page")
    def verify_block_save_text_3(self):
        """This method verifies correct display of the text-3 in the 'Save up to $24!' block"""
        save_block_title3 = self.element_is_visible(self.promo_locators.LUMA_SAVE_TITLE_3)
        save_block_title3_text = save_block_title3.text
        return save_block_title3_text

    @allure.step("Correct redirection of the click on the block 'Save up to $24!' on Men page")
    def verify_block_save_link_redirects_to_a_correct_page(self):
        """This method verifies correct redirection to a new page after clicking on the block"""
        element = self.element_is_visible(self.promo_locators.LUMA_SAVE_BLOCK)
        element.click()
        url = self.driver.current_url
        return url == MEN_TEES_URL

