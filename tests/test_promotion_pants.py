from data.data_urls import PromoBlockLinks
from data.gear_data import expected_link
from pages.promotion_pants_page import PromotionPantsPage


class TestPromotionPantsPage:

    def test_tc_19_01_01(self, driver):
        """Checking title of the Shopping Options section"""
        page = PromotionPantsPage(driver, PromoBlockLinks.PANTS_PROMO_URL)
        page.open()
        title = page.check_text_in_shopping_options_title()
        assert title == "Shopping Options", f"Expected title: 'Shopping Options', Actual title: {title}"

    def test_tc_19_01_02(self, driver):
        """Checking title of the Style section"""
        page = PromotionPantsPage(driver, PromoBlockLinks.PANTS_PROMO_URL)
        page.open()
        title = page.check_text_in_style_title()
        assert title == "STYLE", f"Expected title: 'STYLE', Actual title: {title}"
