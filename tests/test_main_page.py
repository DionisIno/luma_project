"""This section contains home page tests"""

from pages.main_page import MainPage
from data.data_urls import MAIN_PAGE_URL


class TestMainPage:

    class TestHotSellerSection:

        def test_verify_the_card_is_interactive_on_hover(self, driver):
            """This test checks that the card is interactive."""
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            shadow_before, shadow_after = page.check_for_shadow_appearance_when_hovering_over_the_card()
            assert shadow_before != shadow_after, \
                "Card is not interactive"

