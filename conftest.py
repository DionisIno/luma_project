import json
import os
import shutil

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from locators.sign_in_page_locators import SingInPageLocators as sil
from locators.header_page_locators import HeaderPageLocators as hpl
from data.data_urls import MAIN_PAGE_URL
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def driver():
    print('\nstart browser...')
    chrome_options = Options()
    if 'CI' in os.environ:
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver.set_window_size(1900, 1000)
    else:
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        driver.maximize_window()
    yield driver
    print('\nquit browser...')
    driver.quit()


@pytest.fixture(scope="session")
def config():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(current_dir, "config.json")
    with open(config_file) as f:
        config = json.load(f)
    return config


@pytest.fixture(scope="function")
def sing_in(driver, config):
    driver.get(MAIN_PAGE_URL)
    sing_in_button = wait(driver, config["timeout"]).until(EC.visibility_of_element_located(hpl.SIGN_IN))
    sing_in_button.click()
    email = wait(driver, config["timeout"]).until(EC.visibility_of_element_located(sil.CUSTOMER_EMAIL))
    email.send_keys(config["email"])
    password = wait(driver, config["timeout"]).until(EC.visibility_of_element_located(sil.CUSTOMER_PASSWORD))
    password.send_keys(config["password"])
    button = wait(driver, config["timeout"]).until(EC.element_to_be_clickable(sil.SIGN_IN_BUTTON))
    button.click()

@pytest.fixture(scope="session", autouse=True)
def clear_allure_result_folder():
    allure_result_folder = "allure_result"
    if not os.path.exists(allure_result_folder):
        os.makedirs(allure_result_folder)
    else:
        for file_name in os.listdir(allure_result_folder):
            file_path = os.path.join(allure_result_folder, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
    yield