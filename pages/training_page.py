from pages.base_page import BasePage
from locators.training_page_locators import TrainingPageLocators
import allure


@allure.epic('Training Page')
class TrainingPage(BasePage):
    locators = TrainingPageLocators

    @allure.step('Check the Sidebar Shop By title is visible and contains text "Shop By"')
    def check_sidebar_panel_shop_by(self):
        """This method checks that the Sidebar Shop By title is
        visible and contains text 'Shop By' """
        shop_by = self.element_is_visible(self.locators.SHOP_BY)
        return shop_by.text

    @allure.step('Check the Sidebar Category title is visible and contains text "Category"')
    def check_sidebar_panel_category(self):
        """This method checks that the Sidebar Category title is
        visible and contains text 'Category' """
        category = self.element_is_visible(self.locators.CATEGORY)
        return category.text

    @allure.step('Check the Sidebar Video Download is visible and contains text "Video Download"')
    def check_sidebar_panel_video_download(self):
        """This method checks that the Sidebar Video Download is
        visible and contains text 'Video Download' """
        video_download = self.element_is_visible(self.locators.VIDEO_DOWNLOAD)
        return video_download.text

    @allure.step('Check the Sidebar Video Download is visible and contains URL')
    def check_sidebar_panel_video_download_href(self):
        """This method checks that the Sidebar Video Download is
        visible and contains URL"""
        video_download = self.element_is_visible(self.locators.VIDEO_DOWNLOAD)
        return video_download.get_attribute("href")

    @allure.step('Check the Sidebar Compare Products is visible and contains text "Compare Products"')
    def check_sidebar_panel_compare_products(self):
        """This method checks that the Sidebar Compare Products is
        visible and contains text 'Compare Products' """
        compare_products = self.element_is_visible(self.locators.COMPARE_PRODUCTS)
        return compare_products.text

    @allure.step('Check the Sidebar My Wish List is visible and contains text "My Wish List"')
    def check_sidebar_panel_my_wish_list(self):
        """This method checks that the Sidebar My Wish List is
        visible and contains text 'My Wish List' """
        my_wish_list = self.element_is_visible(self.locators.MY_WISH_LIST)
        return my_wish_list.text

    @allure.step('Check the title Training is visible and contains text "Training"')
    def check_title_training(self):
        """This method checks that the title Training is
        visible and contains text 'Training' """
        training = self.element_is_visible(self.locators.HEAD_TEXT)
        return training.text

    @allure.step('Checks the block training main display')
    def check_block_training_main_display(self):
        """This method checks that the block training main display"""
        block_1 = self.element_is_visible(self.locators.BLOCK_1_MAIN)
        self.action_move_to_element(block_1)
        return block_1.is_displayed()

    @allure.step('Checks the block training erin display')
    def check_block_training_erin_display(self):
        """This method checks that the block training erin display"""
        block_2 = self.element_is_visible(self.locators.BLOCK_2_ERIN)
        self.action_move_to_element(block_2)
        return block_2.is_displayed()

    @allure.step('Checks the block training on demand display')
    def check_block_training_demand_display(self):
        """This method checks that the block training on demand display"""
        block_3 = self.element_is_visible(self.locators.BLOCK_3_ON_DEMAND)
        self.action_move_to_element(block_3)
        return block_3.is_displayed()

    @allure.step('Check the title Top Videos is visible and contains text "Top Videos"')
    def check_title_top_videos(self):
        """This method checks that the title Top Videos is
        visible and contains text 'Top Videos' """
        top_videos = self.element_is_visible(self.locators.TOP_VIDEOS)
        self.action_move_to_element(top_videos)
        return top_videos.text

    @allure.step("Check the cursor change on hover on the block training main")
    def check_the_cursor_change_to_block_training_main(self):
        """
        This method hovers the mouse cursor over the block training main,
        hovers the mouse cursor over the block training main,
        and checks for the block cursor change
        """
        # Get block properties before hover
        cursor_before = self.driver.execute_script("""return window.getComputedStyle(document.body).cursor;""")
        # Hover mouse cursor on a block training main
        block_1_main = self.element_is_visible(self.locators.BLOCK_1_MAIN)
        self.action_move_to_element(block_1_main)
        # Hover mouse cursor over block training main
        cursor = self.element_is_present(self.locators.BLOCK_1_MAIN)
        cursor_after = self.check_element_hover_style_using_js(cursor, "cursor")
        return cursor_before, cursor_after

    @allure.step("Check the cursor change on hover on the block training erin")
    def check_the_cursor_change_to_block_training_erin(self):
        """
        This method hovers the mouse cursor over the block training erin,
        hovers the mouse cursor over the block training erin,
        and checks for the block cursor change
        """
        # Get block properties before hover
        cursor_before = self.driver.execute_script("""return window.getComputedStyle(document.body).cursor;""")
        # Hover mouse cursor on a block training erin
        block_2_erin = self.element_is_visible(self.locators.BLOCK_2_ERIN)
        self.action_move_to_element(block_2_erin)
        # Hover mouse cursor over block training erin
        cursor = self.element_is_present(self.locators.BLOCK_2_ERIN)
        cursor_after = self.check_element_hover_style_using_js(cursor, "cursor")
        return cursor_before, cursor_after

    @allure.step("Check the cursor change on hover on the block training on demand")
    def check_the_cursor_change_to_block_training_on_demand(self):
        """
        This method hovers the mouse cursor over the block training on demand,
        hovers the mouse cursor over the block training on demand,
        and checks for the block cursor change
        """
        # Get block properties before hover
        cursor_before = self.driver.execute_script("""return window.getComputedStyle(document.body).cursor;""")
        # Hover mouse cursor on a block training on demand
        block_3_on_demand = self.element_is_visible(self.locators.BLOCK_3_ON_DEMAND)
        self.action_move_to_element(block_3_on_demand)
        # Hover mouse cursor over block training on demand
        cursor = self.element_is_present(self.locators.BLOCK_3_ON_DEMAND)
        cursor_after = self.check_element_hover_style_using_js(cursor, "cursor")
        return cursor_before, cursor_after
