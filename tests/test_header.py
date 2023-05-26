from selenium.webdriver.common.by import By

BASE_URL = "https://magento.softwaretestingboard.com/"


def test_example(driver):
    driver.get("https://magento.softwaretestingboard.com/")


def test_check_page_title(driver):
    driver.get(BASE_URL)
    assert driver.title == 'Home Page'


def test_check_link(driver):
    driver.get("https://magento.softwaretestingboard.com/")
    link = driver.find_element(By.CSS_SELECTOR, "li[class^='level0 nav-1']")
    assert link.is_enabled()

