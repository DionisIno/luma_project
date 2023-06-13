from selenium.webdriver.support import expected_conditions as EC
from locators.reviews_page_locators import ReviewsPageLocators

from selenium.webdriver.support.wait import WebDriverWait

from pages.reviews_page import ReviewsPage
from data.data_urls import REVIEWS_URL, REVIEWS_URL_GENERAL


class TestReviews:
    locators = ReviewsPageLocators

    def test_tc_01_15_01_check_that_it_is_possible_to_vote_for_1_star(self, driver):
        """
        The user is NOT logged in, located in the product card, section "Reviews"
        1. All required fields are filled with correct data
        2. Pressed 1 star
        3.The "Submit Review" button is pressed
        Result: Present in the DOM and visible on the page the message: "You submitted your review for moderation."
        """

        """Steps"""
        page = ReviewsPage(driver, REVIEWS_URL_GENERAL)
        page.open()

        # Get the current URL and print it
        current_url = driver.current_url
        print("Current URL:", current_url)

        page.open_review_menu()
        page.one_star_review_correct()
        page.nickname_input_review_correct()
        page.summary_input_review_correct()
        page.review_input_review_correct()

        """Button click"""
        page.send_review_correct()

        page.see_all_opened_windows()
        page.switch_between_opened_windows_to_base_one()

        """Checking the success message"""
        review_successfully_submitted = page.review_have_been_send_correctly()

        # Get the current URL and print it
        current_url = driver.current_url
        print("Current URL:", current_url)

        if review_successfully_submitted == "You submitted your review for moderation.":
            print('review_successfully_submitted', ' "Success" = Review sent successfully!')
            assert review_successfully_submitted == "You submitted your review for moderation.", "Leave a review failed"

        elif 'https://magento.softwaretestingboard.com/review/product/post/id' in current_url:
            print('review_successfully_submitted', ' "Success" = Review sent successfully!')
            print('The review is recorded at the address and under the number: ', current_url)
            assert 'https://magento.softwaretestingboard.com/review/product/post/id' in current_url, "Leave a review failed"

        else:
            print('Leave a review failed')
            assert review_successfully_submitted == "You submitted your review for moderation." or 'https://magento.softwaretestingboard.com/review/product/post/id' in current_url, "Leave a review failed"


    def test_swich_test(self, driver):
        # https://stepik.org/lesson/184253/step/6?unit=158843

        import os
        import math
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time

        """ Чтобы всё работало (дружба вебдрайвера и текущей версии браузера) """
        from selenium.webdriver.chrome.service import Service as ChromeService
        from webdriver_manager.chrome import ChromeDriverManager

        """ Ссылки """
        link = 'http://suninjuly.github.io/redirect_accept.html'

        """ Локаторы """
        # XPATH
        XPATH_BUTTON_I_WANT_TO_GO_ON_A_MAGIC_JOURNEY = '//button[text()="I want to go on a magical journey!"]'
        XPATH_SUBMIT_BUTTON = '//button[text()="Submit"]'
        # CSS
        CSS_VALUE_OF_X = '#input_value'
        CSS_INPUT_DATA = '#answer'

        # try:
        # Важно именно так написать, чтобы "подружить" версию браузера с хромдрайвером
        page = ReviewsPage(driver, link)
        page.open()

        """ Сколько окон есть """
        print('/.До клика')
        page.see_all_opened_windows()
        page.switch_between_opened_windows_to_base_one()
        print('.\До клика')

        """ Клик по кнопке """
        button_element = page.find_element(By.XPATH, XPATH_BUTTON_I_WANT_TO_GO_ON_A_MAGIC_JOURNEY)
        button_element_click = button_element.click()

        """ Сколько окон есть """
        print('/.После клика')
        page.see_all_opened_windows()
        page.switch_between_opened_windows_to_base_one()
        print('.\После клика')

        # """ Считывание, какие вкладки у нас есть (1-я и 2-я +print) + переключение на 2-ю вкладку"""
        # current_window = page.current_window_handle
        # print(current_window, ' = current_window')
        # new_window = page.window_handles[1]
        # print(new_window, ' = new_window')
        # switch_to_new_tab = page.switch_to.window(new_window)
        #
        #
        # """ Поиск значения 'X' и перевод его в текст """
        # value_of_x_element = page.find_element(By.CSS_SELECTOR, CSS_VALUE_OF_X)
        # convert_vlue_of_x_to_text = value_of_x_element.text
        # x = convert_vlue_of_x_to_text
        #
        # """ Вычисление формулы """
        # def calc(x):
        #     print(x, ' = x = распечатка изнутри функции "def calc(x)"')
        #     """ Вычисление формулы """
        #     return str(math.log(abs(12 * math.sin(int(x)))))
        # y = calc(x)
        # print(y, ' = y')
        #
        # """ Инпут полученных данны """
        # input_element = page.find_element(By.CSS_SELECTOR, CSS_INPUT_DATA)
        # input_element.send_keys(y)
        #
        # """ Клик по кнопке сабмит """
        # submit_button = page.find_element(By.XPATH, XPATH_SUBMIT_BUTTON)
        # submit_button_click = submit_button.click()
        #
        # """ Вывод цифр результата в консоль IDE = можно убрать 'вэйт' из 'finally' """
        # print(page.switch_to.alert.text, " = Вывод цифр результата в консоль IDE = можно убрать 'вэйт' из 'finaly'")

        # finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            # time.sleep(5)
            # закрываем браузер после всех манипуляций
            # page.quit()