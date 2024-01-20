import pytest
import allure

from data.data_urls import GEAR_PAGE_URL
from data.gear_data import expected_link
from pages.gear_page_ import GearPage


@allure.epic("Test Gear Page")
class TestGearPage:

    @allure.title('TC 10.01.01 - Verify title of the Category section')
    def test_tc_10_01_01_presence_category_section_heading(self, driver):
        """Checking title of the Category section"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        title = page.check_text_in_category_title()
        assert title == "Category", f"Expected title: 'Category', Actual title: {title}"

    @allure.title('TC 11.01.02 - Verify Bags menu is displayed and enabled')
    def test_tc_11_01_02_presence_bags_menu(self, driver):
        """Check that Bags is displayed and enabled"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        bags = page.check_bags_element()
        assert bags is not None, "The element isn't displayed or not enabled"

    @allure.title('TC 11.01.02 - Verify Bags menu link functionality')
    def test_tc_11_01_03_bags_link_is_correct(self, driver):
        """Check that bags link is correct"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        page.check_bags_functionality()
        assert page.get_actual_url(driver) == expected_link['bags_url'], \
            'The link is not correct'

    @allure.title('TC 11.01.02 - Verify Fitness equipment menu is displayed and enabled')
    def test_tc_11_01_04_presence_fitness_equipment_menu(self, driver):
        """Check that fitness_equipment is displayed and enabled"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        fitness_equipment = page.check_fitness_equipment_element()
        assert fitness_equipment is not None, "The element isn't displayed or not enabled"

    @allure.title('TC 11.01.02 - Verify Fitness equipment menu link functionality')
    def test_TC_11_01_05_fitness_equipment_link_is_correct(self, driver):
        """Check that fitness_equipment link is correct"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        page.check_fitness_equipment_functionality()
        assert page.get_actual_url(driver) == expected_link['fitness_equipment_url'], \
            'The link is not correct'

    @allure.title('TC 11.01.02 - Verify Watches menu is displayed and enabled')
    def test_tc_11_01_06_presence_watches_menu(self, driver):
        """Check that watches is displayed and enabled"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        watches = page.check_watches_element()
        assert watches is not None, "The element isn't displayed or not enabled"

    @allure.title('TC 11.01.02 - Verify Watches menu link functionality')
    def test_tc_11_01_07_watches_link_is_correct(self, driver):
        """Check that watches link is correct"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        page.check_watches_functionality()
        assert page.get_actual_url(driver) == expected_link['watches_url'], \
            'The link is not correct'
