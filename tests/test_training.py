"""This section contains Training page tests"""
from data.data_urls import TRAINING_PAGE_URL, VIDEO_DOWNLOAD_PAGE_URL
from pages.training_page import TrainingPage
import allure
import pytest


@pytest.fixture(scope="function")
def training_page(driver):
    """This function navigate to Training page and open"""
    page = TrainingPage(driver, TRAINING_PAGE_URL)
    page.open()
    return page


@allure.epic("Training Page")
class TestMainPage:
    @allure.feature("Testing Training Page Sidebar")
    class TestTrainingSidebar:

        @allure.title("TC 16.01.01 Verify Sidebar panel title Shop By is visible and contains text 'Shop By'")
        def test_tc_16_01_01_check_sidebar_shop_by_title(self, training_page):
            """Check Sidebar Shop By title has correct text and is visible"""
            title = training_page.check_sidebar_panel_shop_by()
            assert title == "Shop By", f"Expected title: 'Shop By', Actual title: {title}"

        @allure.title("TC 16.01.02 Verify Sidebar panel title Category is visible and contains text 'Category'")
        def test_tc_16_01_02_check_sidebar_category_title(self, training_page):
            """Check Sidebar Category title has correct text and is visible"""
            title = training_page.check_sidebar_panel_category()
            assert title == "Category", f"Expected title: 'Category', Actual title: {title}"

        @allure.title("TC 16.01.03 Verify Sidebar title Video Download is visible and contains text 'Video Download'")
        def test_tc_16_01_03_check_sidebar_video_download_title(self, training_page):
            """Check Sidebar Video Download title has correct text and is visible"""
            title = training_page.check_sidebar_panel_video_download()
            assert title == "Video Download", f"Expected title: 'Video Download', Actual title: {title}"

        @allure.title("TC 16.01.04 Verify Sidebar panel title Video Download contains URL")
        def test_tc_16_01_04_check_sidebar_video_download_href(self, training_page):
            """Check Sidebar Video Download contains URL"""
            href = training_page.check_sidebar_panel_video_download_href()
            assert href == VIDEO_DOWNLOAD_PAGE_URL, f"Incorrect URL in Video Download"

        @allure.title("TC 16.01.05 Verify Sidebar panel title Compare Products is visible and contains text 'Compare Products'")
        def test_tc_16_01_05_check_sidebar_compare_products(self, training_page):
            """Check Sidebar Category title has correct text and is visible"""
            title = training_page.check_sidebar_panel_compare_products()
            assert title == "Compare Products", f"Expected title: 'Compare Products', Actual title: {title}"

        @allure.title("TC 16.01.06 Verify Sidebar panel title My Wish List is visible and contains text 'My Wish List'")
        def test_tc_16_01_06_check_sidebar_my_wish_list(self, training_page):
            """Check Sidebar Category title has correct text and is visible"""
            title = training_page.check_sidebar_panel_my_wish_list()
            assert title == "My Wish List", f"Expected title: 'My Wish List', Actual title: {title}"

        @allure.title("TC 16.02.01 Verify title Training is visible and contains text 'Training'")
        def test_tc_16_02_01_check_title_training(self, training_page):
            """Check Training title has correct text and is visible"""
            title = training_page.check_title_training()
            assert title == "Training", f"Expected title: 'Training', Actual title: {title}"

        @allure.title("TC 16.02.02 - Check the display of block 1 main")
        def test_tc_16_02_02_check_block_1_main_display(self, training_page):
            """This test checks block-promo training-main is displayed"""
            block_1 = training_page.check_block_training_main_display()
            assert block_1 is True, "The block-promo training-main is not visible"

        @allure.title("TC 16.02.03 - Check the display of block 2 erin")
        def test_tc_16_02_03_check_block_2_erin_display(self, training_page):
            """This test checks block-promo training-erin is displayed"""
            block_2 = training_page.check_block_training_erin_display()
            assert block_2 is True, "The block-promo training-erin is not visible"

        @allure.title("TC 16.02.04 - Check the display of block 3 on demand")
        def test_tc_16_02_04_check_block_3_training_on_demand_display(self, training_page):
            """This test checks block-promo training-on-demand is displayed"""
            block_3 = training_page.check_block_training_demand_display()
            assert block_3 is True, "The block-promo training-erin is not visible"

        @allure.title("TC 16.02.05 Verify title Training is visible and contains text 'Top Videos'")
        def test_tc_16_02_05_check_title_training(self, training_page):
            """Check Top Videos title has correct text and is visible"""
            title = training_page.check_title_top_videos()
            assert title == "Top Videos", f"Expected title: 'Top Videos', Actual title: {title}"

        @allure.title("TC 16.02.06 Check the cursor change to block training main ")
        def test_tc_16_02_06_check_the_cursor_change_to_block_training_main(self, training_page):
            """This test check the cursor change when hovering over the block training main"""
            cursor_before, cursor_after = training_page.check_the_cursor_change_to_block_training_main()
            assert cursor_before != cursor_after, "Mouse cursor has not changed on the block training main"

        @allure.title("TC 16.02.07 Check the cursor change to block training erin")
        def test_tc_16_02_07_check_the_cursor_change_to_block_training_erin(self, training_page):
            """This test check the cursor change when hovering over the block training erin"""
            cursor_before, cursor_after = training_page.check_the_cursor_change_to_block_training_erin()
            assert cursor_before != cursor_after, "Mouse cursor has not changed on the block training erin"

        @allure.title("TC 16.02.08 Check the cursor change to block training on demand")
        def test_tc_16_02_08_check_the_cursor_change_to_block_training_on_demand(self, training_page):
            """This test check the cursor change when hovering over the block training on demand"""
            cursor_before, cursor_after = training_page.check_the_cursor_change_to_block_training_on_demand()
            assert cursor_before != cursor_after, "Mouse cursor has not changed on the block training on demand"

        @allure.title("TC 16.02.08 Check the title page")
        def test_tc_16_02_09_verify_title_page_training(self, training_page):
            """This test check the title page"""
            title = training_page.get_actual_title_of_current_page()
            assert title == 'Training', f"Expected title: 'Training', Actual title: {title}"
