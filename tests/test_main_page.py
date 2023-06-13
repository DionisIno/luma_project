"""This section contains home page tests"""
import json
import time

import allure
import pytest

from pages.main_page import MainPage
from data.data_urls import MAIN_PAGE_URL


@allure.epic("Main Page")
class TestMainPage:
    @allure.feature("Testing Hot Seller Section")
    class TestHotSellerSection:

        @allure.title("Check the transition to the page my wish after clicking on the button")
        def test_06_01_17_check_the_transition_to_the_page_my_wish_after_click_on_the_button(self, driver):
            page = MainPage(driver, MAIN_PAGE_URL)
            page.open()
            error_message_text = page.check_the_transition_to_the_page_my_wish_after_click_on_the_button()
            # assert error_message == error_message_text, \
            #     f"The text does not equal {error_message} or did not go to the page 'My desires'"