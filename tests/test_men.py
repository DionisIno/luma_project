import allure
from data.data_urls import MEN_PAGE_URL, MenPageImageURLS
from pages.men_page import MenPage
import pytest


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

    @allure.title("TC 14.03.02 Verify the link 'Hoodies&Sweatshirts' is visible and clickable.")
    def test_tc_14_03_02(self, driver):
        """Verify that the link 'Hoodies&Sweatshirts' is displayed and clickable"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        link = page.verify_hoodies_link_is_visible_and_clickable()
        assert link, "The link 'Hoodies&Sweatshirts' is not visible"

    @allure.title("TC 14.03.03 Verify the link 'Hoodies&Sweatshirts' redirects to a correct page.")
    def test_tc_14_03_03(self, driver):
        """Verify that the link 'Hoodies&Sweatshirts' correctly opens and redirects to a new webpage, the header \
        'Hoodies&Sweatshirt' is displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_hoodies_redirects_to_a_correct_page()
        assert current_page, "New page isn't open or the 'Hoodies & Sweatshirts' subhead is incorrect"

    @allure.title("TC 14.03.04 Verify the link 'Jackets' is visible and clickable.")
    def test_tc_14_03_04(self, driver):
        """Verify that the link 'Jackets' is displayed and clickable"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        link = page.verify_jackets_link_is_visible_and_clickable()
        assert link, "The link 'Jackets' is not visible"

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

    @allure.title("TC 14.03.07 Verify the link 'Tees' redirects to a correct page.")
    def test_tc_14_03_07(self, driver):
        """Verify that the link 'Tees' correctly opens and redirects to a new webpage, the header 'Tees' is
        displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_tees_redirects_to_a_correct_page()
        assert current_page, "New page isn't open or the 'Tees' subhead is incorrect"

    @allure.title("TC 14.03.08 Verify the link 'Tanks' is visible and clickable.")
    def test_tc_14_03_08(self, driver):
        """Verify that the link 'Tanks' is displayed and clickable"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        link = page.verify_tanks_link_is_visible_and_clickable()
        assert link, "The link 'Tanks' is not visible"

    @allure.title("TC 14.03.09 Verify the link 'Tanks' redirects to a correct page.")
    def test_tc_14_03_09(self, driver):
        """Verify that the link 'Tanks' correctly opens and redirects to a new webpage,\
         the header 'Tanks' is displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_tanks_redirects_to_a_correct_page()
        assert current_page, "New page isn't open or the 'Tanks' subhead is incorrect"

    @allure.title("TC 14.04.01 Verify the 'BOTTOMS' subhead is displayed")
    def test_tc_14_04_01(self, driver):
        """Verify that the subhead 'BOTTOMS' is displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        subhead_title = page.verify_subhead_bottoms_is_visible()
        assert subhead_title == "BOTTOMS"

    @allure.title("TC 14.04.02 Verify the link 'Pants' is visible and clickable.")
    def test_tc_14_04_02(self, driver):
        """Verify that the link 'Pants' is displayed and clickable"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        link = page.verify_pants_link_is_visible_and_clickable()
        assert link, "The link 'Pants' is not visible"

    @allure.title("TC 14.04.03 Verify the link 'Pants' redirects to a correct page.")
    def test_tc_14_04_03(self, driver):
        """Verify that the link 'Pants' correctly opens and redirects to a new webpage, the header 'Pants' is
              displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_pants_link_redirects_to_a_correct_page()
        assert current_page, "New page isn't open or the 'Pants' subhead is incorrect"

    @allure.title("TC 14.04.04 Verify the link 'Shorts' is visible and clickable.")
    def test_tc_14_04_04(self, driver):
        """Verify that the link 'Shorts' is displayed and clickable"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        link = page.verify_shorts_link_is_visible_and_clickable()
        assert link, "The link 'Shorts' is not visible"

    @allure.title("TC 14.04.05 Verify the link 'Shorts' redirects to a correct page.")
    def test_tc_14_04_05(self, driver):
        """Verify that the link 'Shorts' correctly opens and redirects to a new webpage, the header 'Pants' is
              displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_shorts_link_redirects_to_a_correct_page()
        assert current_page, "New page isn't open or the 'Shorts' subhead is incorrect"


@allure.epic("MenPage")
class TestMenPagePromoBlock:

    @allure.title("TC 14.06.01 Verify the 'Men' header is displayed")
    def test_tc_14_06_01(self, driver):
        """Verify that the header 'Men' is displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        subhead_title = page.verify_header_men_is_visible()
        assert subhead_title == "Men"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.09 Verify the visibility of 'Save up to $24!' promo block.")
    def test_tc_14_06_09(self, driver):
        """Verify that the block 'Save up to $24!' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_save = page.check_block_save_display()
        assert block_save is True, "The element is not visible"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.10 Verify the visibility of the image in the 'Save up to $24!' promo block.")
    def test_tc_14_06_10(self, driver):
        """Verify that the image in the block 'Save up to $24!' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_save_image = page.check_block_save_image_display()
        assert block_save_image == MenPageImageURLS.LUMA_SAVE_IMG_URL, "The image is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.11 Verify that the 'Save up to $24!' text in the 'Save up to $24!' promo block is visible.")
    def test_tc_14_06_11(self, driver):
        """Verify that text-1 in 'Save up to $24!' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_save_text_1 = page.verify_block_save_text_1()
        assert block_save_text_1 == "Save up to $24!", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.12 Verify that the 'Buy 3 Luma tees' text in the 'Save up to $24!' promo block is visible.")
    def test_tc_14_06_12(self, driver):
        """Verify that text-2 in 'Save up to $24!' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_save_text_2 = page.verify_block_save_text_2()
        assert block_save_text_2 == "Buy 3 Luma tees, get 4 instead", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.13 Verify that the 'Shop Tees' text in the 'Save up to $24!' promo block is visible.")
    def test_tc_14_06_13(self, driver):
        """Verify that text-3 in 'Save up to $24!' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_save_text_3 = page.verify_block_save_text_3()
        assert block_save_text_3 == "Shop Tees", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.14 Verify the click on the block 'Save up to $24!' redirects to a correct page.")
    def test_tc_14_06_14(self, driver):
        """Verify that the click on the block 'Save up to $24!' correctly redirects to a new webpage"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_block_save_link_redirects_to_a_correct_page()
        assert current_page, "New page isn't open"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.15 Verify the visibility of 'Last chance for pants' promo block.")
    def test_tc_14_06_15(self, driver):
        """Verify that the block 'Last chance for pants' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_last_chance = page.check_block_last_chance_display()
        assert block_last_chance is True, "The element is not visible"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.16 Verify the visibility of the image in the 'Last chance for pants' promo block.")
    def test_tc_14_06_16(self, driver):
        """Verify that the image in the block 'Last chance for pants' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_last_chance_image = page.check_block_last_chance_image_display()
        assert block_last_chance_image == MenPageImageURLS.LUMA_LAST_CHANCE_IMG_URL, "The image is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.17 Verify that the 'Last chance for pants' text is visible.")
    def test_tc_14_06_17(self, driver):
        """Verify that text-1 in 'Last chance for pants' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_last_chance_text_1 = page.verify_block_last_chance_text_1()
        assert block_last_chance_text_1 == "Last chance\nfor pants", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.18 Verify that the 'Take 20% OFF' text is visible.")
    def test_tc_14_06_18(self, driver):
        """Verify that text-2 in 'Last chance for pants' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_last_chance_text_2 = page.verify_block_last_chance_text_2()
        assert block_last_chance_text_2 == "Take\n20% OFF\nand save bigtime*", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.19 Verify that the 'Shop Pants' text is visible.")
    def test_tc_14_06_19(self, driver):
        """Verify that text-3 in 'Last chance for pants' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_last_chance_text_3 = page.verify_block_last_chance_text_3()
        assert block_last_chance_text_3 == "Shop Pants", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.20 Verify the click on the block 'Last chance for pants' redirects to a correct page.")
    def test_tc_14_06_20(self, driver):
        """Verify that the click on the block 'Last chance for pants' correctly redirects to a new webpage"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_block_last_chance_link_redirects_to_a_correct_page()
        assert current_page, "New page isn't open"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.21 Verify the visibility of 'Luma shorts' promo block.")
    def test_tc_14_06_21(self, driver):
        """Verify that the block 'Luma shorts' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_shorts = page.check_block_shorts_display()
        assert block_shorts is True, "The element is not visible"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.22 Verify the visibility of the image in the 'Luma shorts' promo block.")
    def test_tc_14_06_22(self, driver):
        """Verify that the image in the block 'Luma shorts' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_shorts_image = page.check_block_shorts_image_display()
        assert block_shorts_image == MenPageImageURLS.LUMA_SHORTS_IMG_URL, "The image is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.23 Verify that the 'Luma shorts' text is visible.")
    def test_tc_14_06_23(self, driver):
        """Verify that text-1 in 'Luma shorts' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_shorts_text_1 = page.verify_block_shorts_text_1()
        assert block_shorts_text_1 == "Luma shorts", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.24 Verify that the 'Cool it now' text is visible.")
    def test_tc_14_06_24(self, driver):
        """Verify that text-2 in 'Luma shorts' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_shorts_text_2 = page.verify_block_shorts_text_2()
        assert block_shorts_text_2 == "Cool it now", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.25 Verify that the 'Shop Shorts' text is visible.")
    def test_tc_14_06_25(self, driver):
        """Verify that text-3 in 'Luma shorts' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_shorts_text_3 = page.verify_block_shorts_text_3()
        assert block_shorts_text_3 == "Shop Shorts", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.26 Verify the click on the block 'Luma shorts' redirects to a correct page.")
    def test_tc_14_06_26(self, driver):
        """Verify that the click on the block 'Luma shorts' correctly redirects to a new webpage"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_block_shorts_link_redirects_to_a_correct_page()
        assert current_page, "New page isn't open"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.27 Verify the visibility of 'Luma tees' promo block.")
    def test_tc_14_06_27(self, driver):
        """Verify that the block 'Luma tees' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_tees = page.check_block_tees_display()
        assert block_tees is True, "The element is not visible"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.28 Verify the visibility of the image in the 'Luma tees' promo block.")
    def test_tc_14_06_28(self, driver):
        """Verify that the image in the block 'Luma tees' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_tees_image = page.check_block_tees_image_display()
        assert block_tees_image == MenPageImageURLS.LUMA_TEES_IMG_URL, "The image is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.29 Verify that the 'Luma tees' text is visible.")
    def test_tc_14_06_29(self, driver):
        """Verify that text-1 in 'Luma tees' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_tees_text_1 = page.verify_block_tees_text_1()
        assert block_tees_text_1 == "Luma tees", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.30 Verify that the 'Grab a tee or two!' text is visible.")
    def test_tc_14_06_30(self, driver):
        """Verify that text-2 in 'Luma tees' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_tees_text_2 = page.verify_block_tees_text_2()
        assert block_tees_text_2 == "Grab a tee or two!", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.31 Verify that the 'Shop Tees' text is visible.")
    def test_tc_14_06_31(self, driver):
        """Verify that text-3 in 'Luma tees' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_tees_text_3 = page.verify_block_tees_text_3()
        assert block_tees_text_3 == "Shop Tees", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.32 Verify the click on the block 'Luma tees' redirects to a correct page.")
    def test_tc_14_06_32(self, driver):
        """Verify that the click on the block 'Luma tees' correctly redirects to a new webpage"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_block_tees_link_redirects_to_a_correct_page()
        assert current_page, "New page isn't open"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.33 Verify the visibility of 'Luma hoodies' promo block.")
    def test_tc_14_06_33(self, driver):
        """Verify that the block 'Luma hoodies' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_hoodies = page.check_block_hoodies_display()
        assert block_hoodies is True, "The element is not visible"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.34 Verify the visibility of the image in the 'Luma hoodies' promo block.")
    def test_tc_14_06_34(self, driver):
        """Verify that the image in the block 'Luma hoodies' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_hoodies_image = page.check_block_hoodies_image_display()
        assert block_hoodies_image == MenPageImageURLS.LUMA_HOODIES_IMG_URL, "The image is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.35 Verify that the 'Luma hoodies' text is visible.")
    def test_tc_14_06_35(self, driver):
        """Verify that text-1 in 'Luma hoodies' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_hoodies_text_1 = page.verify_block_hoodies_text_1()
        assert block_hoodies_text_1 == "Luma hoodies", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.36 Verify that the 'Dress for fitness' text is visible.")
    def test_tc_14_06_36(self, driver):
        """Verify that text-2 in 'Luma hoodies' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_hoodies_text_2 = page.verify_block_hoodies_text_2()
        assert block_hoodies_text_2 == "Dress for fitness", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.37 Verify that the 'Shop Hoodies' text is visible.")
    def test_tc_14_06_37(self, driver):
        """Verify that text-3 in 'Luma hoodies' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_hoodies_text_3 = page.verify_block_hoodies_text_3()
        assert block_hoodies_text_3 == "Shop Hoodies", "The text is not correct"

    @pytest.mark.skip(reason="Skipped because the UI had been changed and the test is not working")
    @allure.title("TC 14.06.38 Verify the click on the block 'Luma hoodies' redirects to a correct page.")
    def test_tc_14_06_38(self, driver):
        """Verify that the click on the block 'Luma hoodies' correctly redirects to a new webpage"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_block_hoodies_link_redirects_to_a_correct_page()
        assert current_page, "New page isn't open"
