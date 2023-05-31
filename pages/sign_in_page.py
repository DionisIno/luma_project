from locators.sign_in_page_locators import SingInPageLocators
from pages.base_page import BasePage


class SignInPage(BasePage):
    locators = SingInPageLocators

    def check_h1_header(self):
        heading = self.element_is_visible(self.locators.PAGE_HEADER)
        return heading
