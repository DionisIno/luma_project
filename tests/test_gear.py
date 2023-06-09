from data.data_urls import GEAR_PAGE_URL
from data.gear_data import expected_link
from pages.gear_page_ import GearPage


class TestGearPage:

    def test_tc_11_01_02(self, driver):
        """Check that Bags is displayed and enabled"""
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        bags = page.check_bags_element()
        assert bags is not None, "The element isn't displayed or not enabled"

    def test_TC_11_01_03(self, driver):
        page = GearPage(driver, GEAR_PAGE_URL)
        page.open()
        page.check_bags_functionality()
        assert page.get_actual_url(driver) == expected_link['gear_url'], \
            'The link is not correct'

