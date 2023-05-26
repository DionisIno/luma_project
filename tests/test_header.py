
BASE_URL = "https://magento.softwaretestingboard.com/"


def test_example(driver):
    driver.get("https://magento.softwaretestingboard.com/")


def test_check_page_title(driver):
    driver.get(BASE_URL)
    assert driver.title == 'Home Page'
