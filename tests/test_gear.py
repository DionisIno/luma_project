from data.data_urls import GEAR_PAGE_URL
from data.gear_data import expected_link
from pages.gear_page_ import GearPage


class TestGearPage:

    def test_tc_10_01_01(self, driver):
        """Checking title of the Category section"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        title = page.check_text_in_category_title()
        assert title == "Category", f"Expected title: 'Category', Actual title: {title}"

    def test_tc_11_01_02(self, driver):
        """Check that Bags is displayed and enabled"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        bags = page.check_bags_element()
        assert bags is not None, "The element isn't displayed or not enabled"

    def test_TC_11_01_03(self, driver):
        """Check that bags link is correct"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        page.check_bags_functionality()
        assert page.get_actual_url(driver) == expected_link['bags_url'], \
            'The link is not correct'

    def test_tc_11_01_04(self, driver):
        """Check that fitness_equipment is displayed and enabled"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        fitness_equipment = page.check_fitness_equipment_element()
        assert fitness_equipment is not None, "The element isn't displayed or not enabled"

    def test_TC_11_01_05(self, driver):
        """Check that fitness_equipment link is correct"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        page.check_fitness_equipment_functionality()
        assert page.get_actual_url(driver) == expected_link['fitness_equipment_url'], \
            'The link is not correct'

    def test_tc_11_01_06(self, driver):
        """Check that watches is displayed and enabled"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        watches = page.check_watches_element()
        assert watches is not None, "The element isn't displayed or not enabled"

    def test_TC_11_01_07(self, driver):
        """Check that watches link is correct"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        page.check_watches_functionality()
        assert page.get_actual_url(driver) == expected_link['watches_url'], \
            'The link is not correct'
