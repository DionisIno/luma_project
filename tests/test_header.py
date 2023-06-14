import pytest
from data.data_urls import MAIN_PAGE_URL, CREATE_ACCOUNT_PAGE_URL, SIGN_IN_URL, MEN_BOTTOMS_URL, \
    MEN_BOTTOMS_PANTS_URL, MEN_BOTTOMS_SHORTS_URL, MEN_PAGE_URL
from pages.header_page import HeaderPage


class TestHeader:

    def test_tc_01_01_01_greeting_message_is_displayed(self, driver):
        """Check greeting message == 'Default welcome msg!' and is visible"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        message = page.check_greeting_message()
        assert message is not None and message.text == "Default welcome msg!", \
            "The greeting message is not displayed or the text is incorrect"

    def test_tc_01_01_02_display_and_interactivity_of_the_create_an_account_link(self, driver):
        """Check 'Create an account' link is displayed and underlined"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        assert "underline" in page.check_element_hover_style(page.header_locators.CREATE_AN_ACCOUNT, 'text-decoration',
            2), "Link 'Create an account' is either not displayed or not underlined on hover"

    def test_tc_01_01_03_correctness_create_an_account_link(self, driver):
        """Check 'Create an account' link click redirects to the account’s registration page and \
        the "Create New Customer Account" header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.click_and_return_element(page.header_locators.CREATE_AN_ACCOUNT)
        header = page.check_common_header()
        assert driver.current_url == CREATE_ACCOUNT_PAGE_URL and header.text == "Create New Customer Account", \
            "Create an account page is either not opened or the page header is incorrect"

    def test_tc_01_01_04_display_and_interactivity_of_the_sign_in_link(self, driver):
        """Check 'Sign In' link is displayed and underlined"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        assert "underline" in page.check_element_hover_style(page.header_locators.SIGN_IN, 'text-decoration', 2), \
            "Link 'Sign In' is either not displayed or not underlined on hover"

    def test_tc_01_01_05_correctness_sign_in_link(self, driver):
        """Check 'Sign In' link click redirects to the login page and \
        the "Customer Login" header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.click_and_return_element(page.header_locators.SIGN_IN)
        header = page.check_common_header()
        assert driver.current_url == SIGN_IN_URL and header.text == "Customer Login", \
            "Sign In page is either not opened or the page header is incorrect"

    def test_tc_01_02_04_display_and_interactivity_of_the_logo(self, driver):
        """Check that the cursor changes to a 'hand' indicating the logo is a clickable element, \
        and that clicking on it causes the page to reload and redirect to the main page"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        assert "pointer" in page.check_element_hover_style(page.header_locators.LOGO, 'cursor', 2), \
            "Failed: The cursor does not change to a 'hand' when hovering over the logo"

    def test_tc_01_03_36_correctly_redirected_the_link_sale(self, driver):
        """Verify 'Sale' link click redirected to the page and the 'Sale' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        link = page.redirected_the_link_sale()
        assert link, "Sale page isn't opened or the page header is incorrect"

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

    def test_tc_01_02_03_presence_of_a_placeholder_in_the_search_field(self, driver):
        """Check the "Search" field in the header contains the placeholder 'Search entire store here...'"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        assert page.check_search_field() == "Search entire store here...", \
            "Text in the Placeholder field does not match or is missing"

    def test_tc_01_02_02_functionality_of_the_search_field(self, driver):
        """Check the "Search" field is activated and the drop-down list appears with various product"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        dropdown_items = page.enter_search_field_and_get_dropdown()
        assert dropdown_items is not None and len(dropdown_items) > 0, "Error: No drop-down list appears or it`s empty"

    def test_tc_01_02_01_display_and_interactivity_of_the_search_field(self, driver):
        """Check the "Search" field is activated with a vertical flashing symbol "|" and highlighted"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        initial_box_shadow, active_box_shadow = page.activate_search_field_and_check_style()
        assert initial_box_shadow != active_box_shadow, "Error: Search field style doesn't change on activation"

    def test_tc_01_03_35_visible_and_interactive_the_link_sale(self, driver):
        """Verify the link 'Sale' is visible and interactive"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        link = page.link_sale_is_visible_and_interactive()
        assert link, "The link 'Sale' isn't visible and non-interactive"

    def test_tc_01_03_33_correctly_redirected_the_link_training(self, driver):
        """Verify 'Training' link click redirected to the page and the 'Training' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_training()
        assert current_page, "Training page isn't opened or the page header is incorrect"

    def test_tc_01_03_34_correctly_redirected_the_link_training_video_download(self, driver):
        """Verify 'Training - Video Download' link click redirected to the 'Video Download' page
            and the 'Video Download' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_training_video_download()
        assert current_page, "Video Download page isn't opened or the page header is incorrect"

    def test_tc_01_03_32_visible_and_interactive_the_link_training(self, driver):
        """Verify the link 'Training' is visible and interactive and link 'Video Download' is visible"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        link = page.link_training_is_visible_and_interactive()
        assert link, "The link 'Sale' isn't visible and non-interactive"

    def test_tc_01_03_01_visible_and_interactive_the_link_what_is_new(self, driver):
        """Verify the link 'What's new' is visible and interactive"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        link = page.link_what_is_new_is_visible_and_interactive()
        assert link, "The link 'What's new' isn't visible and non-interactive"

    def test_tc_01_03_04_correct_redirection_of_the_link_women(self, driver):
        """Verify that the link 'Women' correctly opens and redirects to a new webpage, the header 'Women' is
        displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirection_of_the_link_women()
        assert current_page, "'Women' page isn't open or the 'Women' header is incorrect"

    def test_tc_01_03_02_correctly_redirected_the_link_what_is_new(self, driver):
        """Verify the link 'What's new' redirected to the page and the 'What's new' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_what_is_new()
        assert current_page, "What's new page isn't opened or the page header is incorrect"

    def test_tc_01_03_27_visible_and_interactive_the_link_gear(self, driver):
        """Verify the link 'Gear' is visible and interactive"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        link = page.link_gear_is_visible_and_interactive()
        assert link, "The link 'Gear' isn't visible or non-interactive"

    def test_tc_01_03_23_display_and_interactivity_of_the_bottoms_subsection(self, driver):
        """Check the 'Bottoms' subsection in 'Men' section is displayed and the 'Pants' and 'Shorts' \
        subsections is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        dropdown_items = page.check_men_bottoms_subsection()
        assert dropdown_items.is_displayed(), "Error: The Pants and Shorts subsection is not displayed"

    def test_tc_01_03_24_correctness_bottoms_link(self, driver):
        """Check 'Bottoms' subsection link in 'Men' section click redirects to the Bottoms page and \
        the 'Bottoms' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_men_bottoms_subsection_link()
        header = page.check_common_header()
        assert driver.current_url == MEN_BOTTOMS_URL and header.text == "Bottoms", \
            "Bottoms page of Men section is either not opened or the page header is incorrect"

    def test_tc_01_03_25_correctness_pants_link(self, driver):
        """Check 'Pants' subsection link in 'Men' section click redirects to the Pants page and \
        the 'Pants' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_men_pants_subsection_link()
        header = page.check_common_header()
        assert driver.current_url == MEN_BOTTOMS_PANTS_URL and header.text == "Pants", \
            "Pants page of Men section is either not opened or the page header is incorrect"

    def test_tc_01_03_26_correctness_shorts_link(self, driver):
        """Check 'Shorts' subsection link in 'Men' section click redirects to the Shorts page and \
            the 'Shorts' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_men_shorts_subsection_link()
        header = page.check_common_header()
        assert driver.current_url == MEN_BOTTOMS_SHORTS_URL and header.text == "Shorts", \
            "Shorts page of Men section is either not opened or the page header is incorrect"

    def test_tc_01_03_15_display_and_interactivity_of_the_men_section(self, driver):
        """Check the 'Tops' & 'Bottoms' subsections in 'Men' section is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        dropdown_items = page.check_men_section_link()
        assert dropdown_items.is_displayed(), "Error: Tops and Bottoms subsections is not displayed"

    def test_tc_01_03_28_correctly_redirected_the_link_gear(self, driver):
        """Verify the link 'Gear' redirected to the page and the 'Gear' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_gear()
        assert current_page, "The 'Gear' page isn't opened or the page header is incorrect"

    def test_tc_01_03_29_correctly_redirected_the_link_gear_bags(self, driver):
        """Verify the link 'Bags' redirected to the page and the 'Bags' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_gear_bags()
        assert current_page, "The 'Bags' page isn't opened or the page header is incorrect"

    def test_tc_01_03_30_correctly_redirected_the_link_gear_fitness_equipment(self, driver):
        """Verify the link 'Fitness Equipment' redirected to the page and the 'Fitness Equipment' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_gear_fitness_equipment()
        assert current_page, "The 'Fitness Equipment' page isn't opened or the page header is incorrect"

    def test_tc_01_03_31_correctly_redirected_the_link_gear_watches(self, driver):
        """Verify the link 'Fitness Equipment' redirected to the page and the 'Fitness Equipment' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        current_page = page.redirected_the_link_gear_watches()
        assert current_page, "The 'Watches' page isn't opened or the page header is incorrect"

    def test_tc_01_03_16_correctness_of_the_men_section_link(self, driver):
        """Check the 'Men' section click redirects to the Men page and the 'Men' header is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.check_redirection_of_men_section_link()
        header = page.check_common_header()
        assert driver.current_url == MEN_PAGE_URL and header.text == "Men", \
            "Men page of Men section is either not opened or the page header is incorrect"

    def test_tc_01_03_17_display_and_interactivity_of_the_tops_subsection(self, driver):
        """Check the 'Tops' subsection in 'Men' section is displayed and the 'Jackets', 'Shorts', \
        'Hoodies & Sweatshirts', 'Tees' and 'Tanks' subsections is displayed"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        dropdown_items = page.check_men_tops_subsection()
        assert dropdown_items.is_displayed(), "Error: The 'Jackets', 'Shorts', 'Hoodies & Sweatshirts', \
            'Tees' and 'Tanks' subsections is not displayed"

    def test_tc_01_01_06_the_absence_of_the_create_an_account_link_display(self, driver):
        """Check the 'Create an account' link is not displayed if the user is authorized"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.user_authorization()
        assert page.element_is_not_visible(page.header_locators.CREATE_AN_ACCOUNT), \
            "Error: 'Create an account' link is visible"

    def test_tc_01_01_07_the_absence_of_the_sign_in_link_display(self, driver):
        """Check the 'Sign In' link is not displayed if the user is authorized"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.user_authorization()
        assert page.element_is_not_visible(page.header_locators.SIGN_IN), \
            "Error: 'Sign In' link is visible"

    @pytest.mark.xfail
    def test_tc_01_01_08_the_display_of_the_dropdown_button(self, driver):
        """Check the dropdown button is displayed if the user is authorized"""
        page = HeaderPage(driver, MAIN_PAGE_URL)
        page.open()
        page.user_authorization()
        page.element_is_clickable(page.header_locators.DROPDOWN_BUTTON)
        assert page.element_is_visible(page.header_locators.DROPDOWN_BUTTON), \
            "Error: dropdown button is not visible"
