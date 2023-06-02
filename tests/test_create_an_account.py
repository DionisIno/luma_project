from data.data_urls import CREATE_ACCOUNT_PAGE_URL
from pages.create_an_account_page import CreateAccountPage

create_account_data = {
    "h1_heading": 'Create New Customer Account',
    "new_account_personal_information_heading": 'Personal Information'
}


class TestCreateAnAccount:
    def test_04_01_01_h1_heading(self, driver):
        """ Verify that the Create An Account page heading is present. """
        create_account_page = CreateAccountPage(driver, CREATE_ACCOUNT_PAGE_URL)
        create_account_page.open()
        h1_heading = create_account_page.check_h1_header()
        assert h1_heading is not None and h1_heading.text == create_account_data['h1_heading'], \
            "H1 Heading is not present"
