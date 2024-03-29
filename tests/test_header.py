import allure
import pytest

from data.data_urls import MAIN_PAGE_URL, CREATE_ACCOUNT_PAGE_URL, SIGN_IN_URL, MEN_BOTTOMS_URL, \
    MEN_BOTTOMS_PANTS_URL, MEN_BOTTOMS_SHORTS_URL, MEN_PAGE_URL, MEN_TOPS_URL, MEN_JACKETS_URL, MEN_HOODIES_URL, \
    MEN_TEES_URL, MEN_TANKS_URL, MY_ACCOUNT_URL, MY_WISHLIST_URL, SIGN_OUT_URL, WOMEN_TOPS_URL, WOMEN_JACKETS_URL, \
    WOMEN_HOODIES_URL, WOMEN_TEES_URL, WOMEN_BRAS_TANKS_URL, WOMEN_BOTTOMS_URL, WOMEN_BOTTOMS_PANTS_URL, \
    WOMEN_BOTTOMS_SHORTS_URL
from pages.header_page import HeaderPage


@pytest.fixture(scope="function")
def header_page(driver):
    header_page = HeaderPage(driver, MAIN_PAGE_URL)
    header_page.open()
    return header_page


@allure.epic('Test Header')
class TestHeader:

    @pytest.mark.skip(reason="Skipped because the element was changed in the updated UI design.")
    @allure.title('TC 01.01.01 greeting message is visible')
    def test_tc_01_01_01_greeting_message_is_displayed(self, driver):
        """Check greeting message == 'Default welcome msg!' and is visible"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        message = page.check_greeting_message()
        assert message is not None and message.text == "Default welcome msg!", \
            "The greeting message is not displayed or the text is incorrect"

    @allure.title('TC 01.01.02 display and interactivity of the "Create an account" link')
    def test_tc_01_01_02_display_and_interactivity_of_the_create_an_account_link(self, driver):
        """Check 'Create an account' link is displayed and underlined"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        assert "underline" in page.check_element_hover_style(page.header_locators.CREATE_AN_ACCOUNT, 'text-decoration',
            2), "Link 'Create an account' is either not displayed or not underlined on hover"

    @allure.title('TC 01.01.03 correctness of the "Create an account" link')
    def test_tc_01_01_03_correctness_create_an_account_link(self, driver):
        """Check 'Create an account' link click redirects to the account’s registration page and \
        the "Create New Customer Account" header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.click_and_return_element(page.header_locators.CREATE_AN_ACCOUNT)
        header = page.check_common_header()
        assert driver.current_url == CREATE_ACCOUNT_PAGE_URL and header.text == "Create New Customer Account", \
            "Create an account page is either not opened or the page header is incorrect"

    @allure.title('TC 01.01.04 display and interactivity of the "Sign In" link')
    def test_tc_01_01_04_display_and_interactivity_of_the_sign_in_link(self, driver):
        """Check 'Sign In' link is displayed and underlined"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        assert "underline" in page.check_element_hover_style(page.header_locators.SIGN_IN, 'text-decoration', 2), \
            "Link 'Sign In' is either not displayed or not underlined on hover"

    @allure.title('TC 01.01.05 correctness of the "Sign In" link')
    def test_tc_01_01_05_correctness_sign_in_link(self, driver):
        """Check 'Sign In' link click redirects to the login page and the "Customer Login" header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.click_and_return_element(page.header_locators.SIGN_IN)
        header = page.check_common_header()
        assert driver.current_url == SIGN_IN_URL and header.text == "Customer Login", \
            "Sign In page is either not opened or the page header is incorrect"

    @allure.title('TC 01.02.04 display and interactivity of the logo')
    def test_tc_01_02_04_display_and_interactivity_of_the_logo(self, driver):
        """Check that the cursor changes to a 'hand' indicating the logo is a clickable element, \
        and that clicking on it causes the page to reload and redirect to the main page"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        assert "pointer" in page.check_element_hover_style(page.header_locators.LOGO, 'cursor', 2), \
            "Failed: The cursor does not change to a 'hand' when hovering over the logo"

    @allure.title('TC 01.03.36 correctly redirected the link sale')
    def test_tc_01_03_36_correctly_redirected_the_link_sale(self, driver):
        """Verify 'Sale' link click redirected to the page and the 'Sale' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        link = page.redirected_the_link_sale()
        assert link, "Sale page isn't opened or the page header is incorrect"

    @allure.title('TC 01.02.05 display and interactivity of the cart icon')
    def test_tc_01_02_05_display_and_interactivity_of_the_cart_icon(self, driver):
        """Check hovering over the shopping cart icon changes the cursor to a "hand," indicating that the cart is a \
        clickable element, click on it and the message "You have no items in your shopping cart." appears"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        assert "pointer" in page.check_element_hover_style(page.header_locators.CART_ICON, 'cursor', 2), \
            "Failed: The cursor does not change to a 'hand' when hovering over the cart icon"
        page.click_and_return_element(page.header_locators.CART_ICON)
        assert "You have no items in your shopping cart." in page.check_cart_message(), \
            "Failed: The message in the cart is not correct or the cart is not empty"

    @allure.title('TC 01.02.03 presence of a  placeholder in the "Search" field')
    def test_tc_01_02_03_presence_of_a_placeholder_in_the_search_field(self, driver):
        """Check the "Search" field in the header contains the placeholder 'Search entire store here...'"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        assert page.check_search_field() == "Search entire store here...", \
            "Text in the Placeholder field does not match or is missing"

    @allure.title('TC 01.02.02 functionality of the "Search" field')
    def test_tc_01_02_02_functionality_of_the_search_field(self, driver):
        """Check the "Search" field is activated and the drop-down list appears with various product"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        dropdown_items = page.enter_search_field_and_get_dropdown()
        assert dropdown_items is not None and len(dropdown_items) > 0, "Error: No drop-down list appears or it`s empty"

    @allure.title('TC 01.02.01 display and interactivity of the "Search" field')
    def test_tc_01_02_01_display_and_interactivity_of_the_search_field(self, driver):
        """Check the "Search" field is activated with a vertical flashing symbol "|" and highlighted"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        initial_box_shadow, active_box_shadow = page.activate_search_field_and_check_style()
        assert initial_box_shadow != active_box_shadow, "Error: Search field style doesn't change on activation"

    @allure.title('TC 01.03.35 visible and interactive the link "Sale"')
    def test_tc_01_03_35_visible_and_interactive_the_link_sale(self, driver):
        """Verify the link 'Sale' is visible and interactive"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        link = page.link_sale_is_visible_and_interactive()
        assert link, "The link 'Sale' isn't visible and non-interactive"

    @allure.title('TC 01.03.33 correctly redirected the link "Training"')
    def test_tc_01_03_33_correctly_redirected_the_link_training(self, driver):
        """Verify 'Training' link click redirected to the page and the 'Training' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_training()
        assert current_page, "Training page isn't opened or the page header is incorrect"

    @allure.title('TC 01.03.34 correctly redirected the link "Training Video Download"')
    def test_tc_01_03_34_correctly_redirected_the_link_training_video_download(self, driver):
        """Verify 'Training - Video Download' link click redirected to the 'Video Download' page
            and the 'Video Download' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_training_video_download()
        assert current_page, "Video Download page isn't opened or the page header is incorrect"

    @allure.title('TC_01_03_32_visible_and_interactive_the_link_"Training"')
    def test_tc_01_03_32_visible_and_interactive_the_link_training(self, driver):
        """Verify the link 'Training' is visible and interactive and link 'Video Download' is visible"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        link = page.link_training_is_visible_and_interactive()
        assert link, "The link 'Sale' isn't visible and non-interactive"

    @allure.title('TC 01.03.01 visible and interactive the link "What is New"')
    def test_tc_01_03_01_visible_and_interactive_the_link_what_is_new(self, driver):
        """Verify the link 'What's new' is visible and interactive"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        link = page.link_what_is_new_is_visible_and_interactive()
        assert link, "The link 'What's new' isn't visible and non-interactive"

    @allure.title('TC 01.03.03 display and interactivity of the "Women" section')
    def test_tc_01_03_03_display_and_interactivity_of_the_woman_section(self, header_page):
        """Verify that the section Women in the header is visible and interactive"""
        dropdown_items = header_page.check_women_subsection()
        assert dropdown_items.is_displayed(), "'Women' section in the header isn't displayed "

    @allure.title('TC 01.03.04 correct redirection of the link "Women"')
    def test_tc_01_03_04_correct_redirection_of_the_link_women(self, driver):
        """Verify that the link 'Women' correctly opens and redirects to a new webpage, the header 'Women' is
        displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirection_of_the_link_women()
        assert current_page, "'Women' page isn't open or the 'Women' header is incorrect"

    @allure.title('TC 01.03.02 correctly redirected the_link "What is New"')
    def test_tc_01_03_02_correctly_redirected_the_link_what_is_new(self, driver):
        """Verify the link 'What's new' redirected to the page and the 'What's new' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_what_is_new()
        assert current_page, "What's new page isn't opened or the page header is incorrect"

    @allure.title('TC 01.03.27 visible and interactive the link "Gear"')
    def test_tc_01_03_27_visible_and_interactive_the_link_gear(self, driver):
        """Verify the link 'Gear' is visible and interactive"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        link = page.link_gear_is_visible_and_interactive()
        assert link, "The link 'Gear' isn't visible or non-interactive"

    @allure.title('TC 01.03.23 display and interactivity of the "Bottoms" section of the "Men" section')
    def test_tc_01_03_23_display_and_interactivity_bottoms_men_section(self, driver):
        """Check the 'Bottoms' subsection in 'Men' section is displayed and the 'Pants' and 'Shorts' \
        subsections is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        dropdown_items = page.check_men_bottoms_subsection()
        assert dropdown_items.is_displayed(), "Error: The Pants and Shorts subsection is not displayed"

    @allure.title('TC 01.03.24 correctness of the "Bottoms" link of the "Men" section')
    def test_tc_01_03_24_correctness_bottoms_link_men_section(self, driver):
        """Check 'Bottoms' subsection link in 'Men' section click redirects to the Bottoms page and \
        the 'Bottoms' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_men_bottoms_subsection_link()
        header = page.check_common_header()
        assert driver.current_url == MEN_BOTTOMS_URL and header.text == "Bottoms", \
            "Bottoms page of Men section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.25 correctness of the "Pants" link of the "Men" section')
    def test_tc_01_03_25_correctness_pants_link_men_section(self, driver):
        """Check 'Pants' subsection link click in 'Men' section redirects to the Pants page and \
        the 'Pants' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_men_pants_subsection_link()
        header = page.check_common_header()
        assert driver.current_url == MEN_BOTTOMS_PANTS_URL and header.text == "Pants", \
            "Pants page of Men section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.26 correctness "Shorts" link')
    def test_tc_01_03_26_correctness_shorts_link(self, driver):
        """Check 'Shorts' subsection link in 'Men' section click redirects to the Shorts page and \
            the 'Shorts' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_men_shorts_subsection_link()
        header = page.check_common_header()
        assert driver.current_url == MEN_BOTTOMS_SHORTS_URL and header.text == "Shorts", \
            "Shorts page of Men section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.15 display and interactivity of the "Men" section')
    def test_tc_01_03_15_display_and_interactivity_of_the_men_section(self, driver):
        """Check the 'Tops' & 'Bottoms' subsections in 'Men' section is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        dropdown_items = page.check_men_section_link()
        assert dropdown_items.is_displayed(), "Error: Tops and Bottoms subsections is not displayed"

    @allure.title('TC 01.03.28 correctly redirected the link "Gear"')
    def test_tc_01_03_28_correctly_redirected_the_link_gear(self, driver):
        """Verify the link 'Gear' redirected to the page and the 'Gear' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_gear()
        assert current_page, "The 'Gear' page isn't opened or the page header is incorrect"

    @allure.title('TC 01.03.29 correctly redirected the link "Gear - Bags"')
    def test_tc_01_03_29_correctly_redirected_the_link_gear_bags(self, driver):
        """Verify the link 'Bags' redirected to the page and the 'Bags' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_gear_bags()
        assert current_page, "The 'Bags' page isn't opened or the page header is incorrect"

    @allure.title('TC 01.03.30 correctly redirected the link "Gear - Fitness Equipment"')
    def test_tc_01_03_30_correctly_redirected_the_link_gear_fitness_equipment(self, driver):
        """Verify the link 'Fitness Equipment' redirected to the page and the 'Fitness Equipment' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_gear_fitness_equipment()
        assert current_page, "The 'Fitness Equipment' page isn't opened or the page header is incorrect"

    @allure.title('TC 01.03.31 correctly redirected the link "Gear - Watches"')
    def test_tc_01_03_31_correctly_redirected_the_link_gear_watches(self, driver):
        """Verify the link 'Fitness Equipment' redirected to the page and the 'Fitness Equipment' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_gear_watches()
        assert current_page, "The 'Watches' page isn't opened or the page header is incorrect"

    @allure.title('TC 01.03.16 correctness of the "Men" section link')
    def test_tc_01_03_16_correctness_of_the_men_section_link(self, driver):
        """Check the 'Men' section click redirects to the Men page and the 'Men' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_redirection_of_men_section_link()
        header = page.check_common_header()
        assert driver.current_url == MEN_PAGE_URL and header.text == "Men", \
            "Men page of Men section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.17 display and interactivity of the "Tops" section of the "Men" section')
    def test_tc_01_03_17_display_and_interactivity_of_the_tops_men_section(self, driver):
        """Check the 'Tops' subsection in 'Men' section is displayed and the 'Jackets', 'Shorts', \
        'Hoodies & Sweatshirts', 'Tees' and 'Tanks' subsections is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        dropdown_items = page.check_men_tops_subsection()
        assert dropdown_items.is_displayed(), "Error: The 'Jackets', 'Shorts', 'Hoodies & Sweatshirts', \
            'Tees' and 'Tanks' subsections is not displayed"

    @allure.title('TC 01.01.06 absence of the "Create an account" link display')
    def test_tc_01_01_06_the_absence_of_the_create_an_account_link_display(self, driver):
        """Check the 'Create an account' link is not displayed if the user is authorized"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.user_authorization()
        assert page.element_is_not_visible(page.header_locators.CREATE_AN_ACCOUNT), \
            "Error: 'Create an account' link is visible"

    @allure.title('TC 01.01.07 absence of the "Sign In" link display')
    def test_tc_01_01_07_the_absence_of_the_sign_in_link_display(self, driver):
        """Check the 'Sign In' link is not displayed if the user is authorized"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.user_authorization()
        assert page.element_is_not_visible(page.header_locators.SIGN_IN), \
            "Error: 'Sign In' link is visible"

    @allure.title('TC 01.01.08 display of the dropdown list button ')
    def test_tc_01_01_08_the_display_of_the_dropdown_button(self, driver):
        """Check the dropdown button is displayed if the user is authorized"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.user_authorization()
        page.element_is_visible(page.header_locators.DROPDOWN_BUTTON)
        assert page.element_is_visible(page.header_locators.DROPDOWN_BUTTON), \
            "Error: dropdown button is not visible"

    @allure.title('TC 01.01.09 functionality of the dropdown list button')
    def test_tc_01_01_09_the_functionality_of_the_dropdown_button(self, driver):
        """Check the display of the dropdown list after clicking the button if the user is authorized"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.user_authorization()
        page.click_and_return_element(page.header_locators.DROPDOWN_BUTTON)
        assert page.element_is_visible(page.header_locators.HEADER_LIST), \
            "Error: The dropdown list with sections 'My Account', 'My Wish List', 'Sign Out' is not appears"

    @allure.title('TC 01.03.18 correctness of the "Tops" link of the "Men" section')
    def test_tc_01_03_18_correctness_of_the_tops_men_section_link(self, driver):
        """Check 'Tops' subsection link click in 'Men' section redirects to the Tops-men page and \
        the 'Tops' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_redirection_of_tops_subsection_of_men_section_link()
        header = page.check_common_header()
        assert driver.current_url == MEN_TOPS_URL and header.text == "Tops", \
            "Tops-men page of Men section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.19 correctness of the "Jackets" link of the "Men" section')
    def test_tc_01_03_19_correctness_of_jackets_men_section_link(self, driver):
        """Check 'Jackets' subsection link click in 'Men' section redirects to the Jackets-men page and \
        the 'Jackets' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_redirection_of_jackets_subsection_of_men_section_link()
        header = page.check_common_header()
        assert driver.current_url == MEN_JACKETS_URL and header.text == "Jackets", \
            "Jackets-men page of Men section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.20 correctness of the "Hoodies & Sweatshirts" link of the "Men" section')
    def test_tc_01_03_20_correctness_of_hoodies_men_section_link(self, driver):
        """Check 'Hoodies & Sweatshirts' subsection link click in 'Men' section redirects to the \
        Hoodies & Sweatshirts-men page and the 'Hoodies & Sweatshirts' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_redirection_of_hoodies_subsection_of_men_section_link()
        header = page.check_common_header()
        assert driver.current_url == MEN_HOODIES_URL and header.text == "Hoodies & Sweatshirts", \
            "Hoodies & Sweatshirts-men page of Men section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.21 correctness of the "Tees" link of the "Men" section')
    def test_tc_01_03_21_correctness_of_tees_men_section_link(self, driver):
        """Check 'Tees' subsection link click in 'Men' section redirects to the Tees-men page and \
        the 'Tees' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_redirection_of_tees_subsection_of_men_section_link()
        header = page.check_common_header()
        assert driver.current_url == MEN_TEES_URL and header.text == "Tees", \
            "Tees-men page of Men section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.22 correctness of the "Tanks" link of the "Men" section')
    def test_tc_01_03_22_correctness_of_tanks_men_section_link(self, driver):
        """Check 'Tanks' subsection link click in 'Men' section redirects to the Tanks-men page and \
        the 'Tanks' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_redirection_of_tanks_subsection_of_men_section_link()
        header = page.check_common_header()
        assert driver.current_url == MEN_TANKS_URL and header.text == "Tanks", \
            "Tanks-men page of Men section is either not opened or the page header is incorrect"

    @allure.title('TC 01.01.10 functionality of the "My account" section in the dropdown list')
    def test_tc_01_01_10_functionality_of_the_my_account_in_the_dropdown_list(self, driver):
        """Check the list appears with sections 'My Account', 'My Wish List', 'Sign Out' after clicking the button,\
        then clicking on 'My Account' redirects to the account page with the header 'My Account' displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.user_authorization()
        page.check_redirection_of_the_my_account_link()
        header = page.check_common_header()
        assert driver.current_url == MY_ACCOUNT_URL and header.text == "My Account", \
            "My Account page is either not opened or the page header is incorrect"

    @allure.title('TC 01.01.11 functionality of the "My Wish List" section in the dropdown list')
    def test_tc_01_01_11_functionality_of_the_my_wish_list_in_the_dropdown_list(self, driver):
        """Check the list appears with sections 'My Account', 'My Wish List', 'Sign Out' after clicking the button,\
        then clicking on 'My Wish List' redirects to the account page with the header 'My Wish List' displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.user_authorization()
        page.check_redirection_of_the_my_wish_list_link()
        header = page.check_common_header()
        assert driver.current_url == MY_WISHLIST_URL and header.text == "My Wish List", \
            "My Wish List page is either not opened or the page header is incorrect"

    @allure.title('TC 01.01.12 functionality of the "Sign In" section in the dropdown list')
    def test_tc_01_01_12_functionality_of_the_sign_out_in_the_dropdown_list(self, driver):
        """Check the list appears with sections 'My Account', 'My Wish List', 'Sign Out' after clicking the button,\
        then clicking on 'Sign Out' redirects to the account page with the header 'You are signed out' displayed \
        and redirected to the Main Page after 5 seconds"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.user_authorization()
        page.check_redirection_of_the_sign_out_link()
        header = page.check_common_header()
        assert driver.current_url == SIGN_OUT_URL and header.text == "You are signed out", \
            "Sign Out page is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.05 display and interactivity of the "Tops" section of the "Women" section')
    def test_tc_01_03_05_display_and_interactivity_of_the_tops_women_section(self, driver):
        """Check the 'Tops' subsection in 'Women' section is displayed and the 'Jackets', 'Shorts', \
        'Hoodies & Sweatshirts', 'Tees' and 'Bras & Tanks' subsections is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        dropdown_items = page.check_women_tops_subsection()
        assert dropdown_items.is_displayed(), "Error: The 'Jackets', 'Shorts', 'Hoodies & Sweatshirts', \
            'Tees' and 'Bras & Tanks' subsections is not displayed"

    @allure.title('TC 01.03.06 correctness of the "Tops" link of the "Women" section')
    def test_tc_01_03_06_correctness_of_the_tops_women_section_link(self, driver):
        """Check 'Tops' subsection link click in 'Women' section redirects to the Tops-women page and \
        the 'Tops' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_redirection_of_tops_subsection_of_women_section_link()
        header = page.check_common_header()
        assert driver.current_url == WOMEN_TOPS_URL and header.text == "Tops", \
            "Tops-women page of Women section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.07 correctness of the "Jackets" link of the "Women" section')
    def test_tc_01_03_07_correctness_of_jackets_women_section_link(self, driver):
        """Check 'Jackets' subsection link click in 'Women' section redirects to the Jackets-women page and \
        the 'Jackets' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_redirection_of_jackets_subsection_of_women_section_link()
        header = page.check_common_header()
        assert driver.current_url == WOMEN_JACKETS_URL and header.text == "Jackets", \
            "Jackets-women page of Women section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.08 correctness of the "Hoodies & Sweatshirts" link of the "Women" section')
    def test_tc_01_03_08_correctness_of_hoodies_women_section_link(self, driver):
        """Check 'Hoodies & Sweatshirts' subsection link click in 'Women' section redirects to the \
        Hoodies & Sweatshirts-women page and the 'Hoodies & Sweatshirts' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_redirection_of_hoodies_subsection_of_women_section_link()
        header = page.check_common_header()
        assert driver.current_url == WOMEN_HOODIES_URL and header.text == "Hoodies & Sweatshirts", \
            "Hoodies & Sweatshirts-women page of Women section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.09 correctness of the "Tees" link of the "Women" section')
    def test_tc_01_03_09_correctness_of_tees_women_section_link(self, driver):
        """Check 'Tees' subsection link click in 'Women' section redirects to the Tees-women page and \
        the 'Tees' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_redirection_of_tees_subsection_of_women_section_link()
        header = page.check_common_header()
        assert driver.current_url == WOMEN_TEES_URL and header.text == "Tees", \
            "Tees-women page of Women section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.10 correctness of the "Bras" link of the "Women" section')
    def test_tc_01_03_10_correctness_of_bras_tanks_women_section_link(self, driver):
        """Check 'Bras & Tanks' subsection link click in 'Women' section redirects to the Bras & Tanks-women page and \
        the 'Bras & Tanks' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_redirection_of_tanks_subsection_of_women_section_link()
        header = page.check_common_header()
        assert driver.current_url == WOMEN_BRAS_TANKS_URL and header.text == "Bras & Tanks", \
            "Bras & Tanks-women page of Women section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.11 display and interactivity of the "Bottoms" section of the "Women" section')
    def test_tc_01_03_11_display_and_interactivity_bottoms_women_section(self, driver):
        """Check the 'Bottoms' subsection in 'Women' section is displayed and the 'Pants' and 'Shorts' \
        subsections is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        dropdown_items = page.check_women_bottoms_subsection()
        assert dropdown_items.is_displayed(), "Error: The Pants and Shorts subsection is not displayed"

    @allure.title('TC 01.03.12 correctness of the "Bottoms" link of the "Women" section')
    def test_tc_01_03_12_correctness_bottoms_link_women_section(self, driver):
        """Check 'Bottoms' subsection link in 'Women' section click redirects to the Bottoms page and \
        the 'Bottoms' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_women_bottoms_subsection_link()
        header = page.check_common_header()
        assert driver.current_url == WOMEN_BOTTOMS_URL and header.text == "Bottoms", \
            "Bottoms page of Women section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.13 correctness of the "Pants" link of the "Women" section')
    def test_tc_01_03_13_correctness_pants_link_women_section(self, driver):
        """Check 'Pants' subsection link click in 'Women' section redirects to the Pants page and \
        the 'Pants' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_women_pants_subsection_link()
        header = page.check_common_header()
        assert driver.current_url == WOMEN_BOTTOMS_PANTS_URL and header.text == "Pants", \
            "Pants page of Women section is either not opened or the page header is incorrect"

    @allure.title('TC 01.03.14 correctness of the "Shorts" link of the "Women" section')
    def test_tc_01_03_14_correctness_shorts_link_women_section(self, driver):
        """Check 'Shorts' subsection link click in 'Women' section redirects to the Shorts page and \
        the 'Shorts' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_women_shorts_subsection_link()
        header = page.check_common_header()
        assert driver.current_url == WOMEN_BOTTOMS_SHORTS_URL and header.text == "Shorts", \
            "Shorts page of Women section is either not opened or the page header is incorrect"
