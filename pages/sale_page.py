import allure

from locators.sale_page_locators import SideBarLocators, MainContentPromoBlocks
from pages.base_page import BasePage


class SalePage(BasePage):
    side_bar_locators = SideBarLocators
    promo_blocks_locators = MainContentPromoBlocks

    @allure.step("Check text in Women's deals title")
    def check_text_in_women_deals_title(self):
        women_deals_title = self.element_is_visible(self.side_bar_locators.WOMEN_DEALS_TITLE)
        title_women_deals = women_deals_title.text
        return title_women_deals

    @allure.step("Get actual title of webpage")
    def get_actual_title(self, driver):
        actual_title = driver.title
        return actual_title

    @allure.step("Get actual URL of webpage")
    def get_actual_url(self, driver):
        actual_url = driver.current_url
        return actual_url

    @allure.step("Check text in Men's deals title")
    def check_text_in_men_deals_title(self):
        men_deals_title = self.element_is_visible(self.side_bar_locators.MEN_DEALS_TITLE)
        title_men_deals = men_deals_title.text
        return title_men_deals

    @allure.step("Check text in Gear deals title")
    def check_text_in_gear_deals_title(self):
        gear_deals_title = self.element_is_visible(self.side_bar_locators.GEAR_DEALS_TITLE)
        title_gear_deals = gear_deals_title.text
        return title_gear_deals

    @allure.step("Check img in main block - Women's Deals")
    def check_img_in_main_block(self):
        img = self.element_is_visible(self.promo_blocks_locators.SALE_WOMEN_IMG)
        img_src = img.get_attribute("src")
        return img_src

    @allure.step("Check img in 2 columns block - Men's Deals")
    def check_img_in_men_block(self):
        img = self.element_is_visible(self.promo_blocks_locators.SALE_MEN_IMG)
        img_src = img.get_attribute("src")
        return img_src

    @allure.step("Check img in 2 columns block - Gear Deals")
    def check_img_in_gear_block(self):
        img = self.element_is_visible(self.promo_blocks_locators.SALE_GEAR_IMG)
        img_src = img.get_attribute("src")
        return img_src

    @allure.step("Check title-text in main block - Women's Deals")
    def check_title_text_in_main_block(self):
        main_block_title = self.element_is_visible(self.promo_blocks_locators.SALE_WOMEN_TITLE)
        main_block_title_text = main_block_title.text
        return main_block_title_text

    @allure.step("Check content-text in main block - Women's Deals")
    def check_content_text_in_main_block(self):
        main_block_content = self.element_is_visible(self.promo_blocks_locators.SALE_WOMEN_CONTENT)
        main_block_content_text = main_block_content.text
        return main_block_content_text

    @allure.step("Check title-text in 2 columns block - Men's Deals")
    def check_title_text_in_men_block(self):
        men_block_title = self.element_is_visible(self.promo_blocks_locators.SALE_MEN_TITLE)
        men_block_title_text = men_block_title.text
        return men_block_title_text

    @allure.step("Check content-text in 2 columns block - Men's Deals")
    def check_content_text_in_men_block(self):
        men_block_content = self.element_is_visible(self.promo_blocks_locators.SALE_MEN_CONTENT)
        men_block_content_text = men_block_content.text
        return men_block_content_text

    @allure.step("Check title-text in 2 columns block - Gear Deals")
    def check_title_text_in_gear_block(self):
        gear_block_title = self.element_is_visible(self.promo_blocks_locators.SALE_GEAR_TITLE)
        gear_block_title_text = gear_block_title.text
        return gear_block_title_text

    @allure.step("Check content-text in 2 columns block - Gear Deals")
    def check_content_text_in_gear_block(self):
        gear_block_content = self.element_is_visible(self.promo_blocks_locators.SALE_GEAR_CONTENT)
        gear_block_content_text = gear_block_content.text
        return gear_block_content_text
