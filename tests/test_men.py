import allure
from data.data_urls import MEN_PAGE_URL, MenPageImageURLS
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


class TestMenPagePromoBlock:

    @allure.title("TC 14.06.01 Verify the 'Men' header is displayed")
    def test_tc_14_06_01(self, driver):
        """Verify that the header 'Men' is displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        subhead_title = page.verify_header_men_is_visible()
        assert subhead_title == "Men"

    @allure.title("TC 14.06.21 Verify the visibility of 'Luma shorts' promo block.")
    def test_tc_14_06_21(self, driver):
        """Verify that the block 'Luma shorts' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_shorts = page.check_block_shorts_display()
        assert block_shorts is True, "The element is not visible"

    @allure.title("TC 14.06.22 Verify the visibility of the image in the 'Luma shorts' promo block.")
    def test_tc_14_06_22(self, driver):
        """Verify that the image in the block 'Luma shorts' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_shorts_image = page.check_block_shorts_image_display()
        assert block_shorts_image == MenPageImageURLS.LUMA_SHORTS_IMG_URL, "The image is not correct"

    @allure.title("TC 14.06.23 Verify that the 'Luma shorts' text is visible.")
    def test_tc_14_06_23(self, driver):
        """Verify that text-1 in 'Luma shorts' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_shorts_text_1 = page.verify_block_shorts_text_1()
        assert block_shorts_text_1 == "Luma shorts", "The text is not correct"

    @allure.title("TC 14.06.24 Verify that the 'Cool it now' text is visible.")
    def test_tc_14_06_24(self, driver):
        """Verify that text-2 in 'Luma shorts' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_shorts_text_2 = page.verify_block_shorts_text_2()
        assert block_shorts_text_2 == "Cool it now", "The text is not correct"

    @allure.title("TC 14.06.25 Verify that the 'Shop Shorts' text is visible.")
    def test_tc_14_06_25(self, driver):
        """Verify that text-3 in 'Luma shorts' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_shorts_text_3 = page.verify_block_shorts_text_3()
        assert block_shorts_text_3 == "Shop Shorts", "The text is not correct"

    @allure.title("TC 14.06.26 Verify the click on the block 'Luma shorts' redirects to a correct page.")
    def test_tc_14_06_26(self, driver):
        """Verify that the click on the block 'Luma shorts' correctly redirects to a new webpage"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_block_shorts_link_redirects_to_a_correct_page()
        assert current_page, "New page isn't open"

    @allure.title("TC 14.06.27 Verify the visibility of 'Luma tees' promo block.")
    def test_tc_14_06_27(self, driver):
        """Verify that the block 'Luma tees' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_tees = page.check_block_tees_display()
        assert block_tees is True, "The element is not visible"

    @allure.title("TC 14.06.28 Verify the visibility of the image in the 'Luma tees' promo block.")
    def test_tc_14_06_28(self, driver):
        """Verify that the image in the block 'Luma tees' is displayed on the Men page"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_tees_image = page.check_block_tees_image_display()
        assert block_tees_image == MenPageImageURLS.LUMA_TEES_IMG_URL, "The image is not correct"

    @allure.title("TC 14.06.29 Verify that the 'Luma tees' text is visible.")
    def test_tc_14_06_29(self, driver):
        """Verify that text-1 in 'Luma tees' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_tees_text_1 = page.verify_block_shorts_text_1()
        assert block_tees_text_1 == "Luma tees", "The text is not correct"

    @allure.title("TC 14.06.30 Verify that the 'Grab a tee or two!' text is visible.")
    def test_tc_14_06_30(self, driver):
        """Verify that text-2 in 'Luma tees' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_tees_text_2 = page.verify_block_shorts_text_2()
        assert block_tees_text_2 == "Grab a tee or two!", "The text is not correct"

    @allure.title("TC 14.06.31 Verify that the 'Shop Tees' text is visible.")
    def test_tc_14_06_31(self, driver):
        """Verify that text-3 in 'Luma tees' block correctly displayed"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        block_tees_text_3 = page.verify_block_tees_text_3()
        assert block_tees_text_3 == "Shop Tees", "The text is not correct"

    @allure.title("TC 14.06.32 Verify the click on the block 'Luma tees' redirects to a correct page.")
    def test_tc_14_06_32(self, driver):
        """Verify that the click on the block 'Luma tees' correctly redirects to a new webpage"""
        page = MenPage(driver, MEN_PAGE_URL)
        page.open()
        current_page = page.verify_block_tees_link_redirects_to_a_correct_page()
        assert current_page, "New page isn't open"
