from pages.sign_in_page import SignInPage
from data.sign_in_data import sign_in_data
from data.data_urls import SIGN_IN_URL


class TestRegisteredCustomers:
    def test_check_link(self, driver):
        """Check Login Page Heading is present """
        sign_in_page = SignInPage(driver, SIGN_IN_URL)
        sign_in_page.open()
        h1_heading = sign_in_page.check_h1_header()
        assert h1_heading is not None and h1_heading.text == sign_in_data["h1_heading"], "H1 Heading is not present"
