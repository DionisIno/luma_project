import allure
import pytest
from data.data_urls import MEN_PAGE_URL
from pages.men_page import MenPage


@allure.epic("MenPage")
class TestMenPage:
    @allure.title("TC 14.02.02 Verify the link Tops is visible and clickable.")
    def test_tc_14_02_02(self, driver):
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        link = page.verify_tops_link_is_visible_and_clickable()
        assert link, "The link 'Tops' is not visible"

    @allure.title("TC 14.02.03 Verify the link Tops redirects to a correct page.")
    def test_tc_14_02_03(self, driver):
        """Verify that the link 'Tops' correctly opens and redirects to a new webpage, the header 'Tops' is
              displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_tops_link_redirects_to_a_correct_page()
        assert current_page, "New page isn't open or the 'Tops' subhead is incorrect"

    @allure.title("TC 14.02.04 Verify the link 'Bottoms' is visible and clickable.")
    def test_tc_14_02_04(self, driver):
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        link = page.verify_bottoms_link_is_visible_and_clickable()
        assert link, "The link 'Bottoms' is not visible"

    @allure.title("TC 14.02.05 Verify the link 'Bottoms' redirects to a correct page.")
    def test_tc_14_02_05(self, driver):
        """Verify that the link 'Bottoms' correctly opens and redirects to a new webpage, the header 'Bottoms' is
          displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_bottoms_redirects_to_a_correct_page()
        assert current_page, "New page isn't open or the 'Bottoms' subhead is incorrect"

    @allure.title("TC 14.03.01 Verify the 'TOPS' subhead is displayed")
    def test_tc_14_03_01(self, driver):
        """Verify that the subhead 'TOPS' is displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        subhead_title = page.verify_subhead_tops_is_visible()
        assert subhead_title == "TOPS"

    @allure.title("TC 14.03.04 Verify the link 'Jackets' is visible and clickable.")
    def test_tc_14_03_04(self, driver):
        """Verify that the link 'Jackets' is displayed and clickable"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        link = page.verify_jackets_link_is_visible_and_clickable()
        assert link, "The link 'Jackets' is not visible"

    @allure.title("TC 14.06.01 Verify the 'Men' header is displayed")
    def test_tc_14_06_01(self, driver):
        """Verify that the header 'Men' is displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        subhead_title = page.verify_header_men_is_visible()
        assert subhead_title == "Men"

    @allure.title("TC 14.03.05 Verify the link 'Jackets' redirects to a correct page.")
    def test_tc_14_03_05(self, driver):
        """Verify that the link 'Jackets' correctly opens and redirects to a new webpage, the header 'Jackets' is
          displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_jackets_redirects_to_a_correct_page()
        assert current_page, "New page isn't open or the 'Jackets' subhead is incorrect"

    @allure.title("TC 14.03.06 Verify the link 'Tees' is visible and clickable.")
    def test_tc_14_03_06(self, driver):
        """Verify that the link 'Tees' is displayed and clickable"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        link = page.verify_tees_link_is_visible_and_clickable()
        assert link, "The link 'Tees' is not visible"
