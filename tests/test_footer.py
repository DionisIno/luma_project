from selenium.webdriver.common.by import By


def test_check_link(driver):
    driver.get("https://magento.softwaretestingboard.com/")
    link = driver.find_element(By.CSS_SELECTOR, "ul[class='footer links'] li:nth-child(1)")
    print("4")
    assert link.is_enabled()
