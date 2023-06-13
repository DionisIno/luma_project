"""This section contains Training page tests"""
from data.data_urls import TRAINING_PAGE_URL
from pages.training_page import TrainingPage
import allure


@allure.epic("Training Page")
class TestMainPage:
    @allure.feature("Testing Training Page Sidebar")
    class TestTrainingSidebar:

        @allure.title("TC 16.01.01 Verify Sidebar panel title Shop By is visible")
        def test_tc_16_01_01(self, driver):
            """Check Sidebar Shop By title has correct text and is visible"""
            page = TrainingPage(driver, TRAINING_PAGE_URL)
            page.open()
            title = page.check_sidebar_panel_name()
            assert title == "Shop By", f"Expected title: 'Shop By, Actual title: {title}"
