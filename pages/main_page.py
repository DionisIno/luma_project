"""This section contains the basic steps for running homepage tests"""
import time
from selenium.webdriver.common.by import By

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver import ActionChains


class MainPage(BasePage):
    locators = MainPageLocators


    @allure.step("Check the transition to the page my desires when clicking on the button")
    def check_the_transition_to_the_page_my_wish_after_click_on_the_button(self):
        """
        This method hovers the mouse over the product card,
        clicks the add to favorites button
        and checks that the correct page has been navigated to.
        :return:
        """
        action = ActionChains(self.driver)
        product_card = self.element_is_visible(self.locators.PRODUCT_CARD)
        self.action_move_to_element(product_card)
        print('card')
        button = self.element_is_present(self.locators.PRODUCT_CARD_BUTTONS["add_to_wish_list"])
        print(button.text)
        self.action_move_to_element(button)
        # action.click(button).perform()
        button.click()
        # self.driver.execute_script("arguments[0].click();", button)
        print("button")
        time.sleep(5)
        # action.pause(10).perform()
        error_message = self.get_error_message()
        return error_message

    def get_error_message(self):

        error_message_locator = (By.XPATH, "//div[@data-bind='html: $parent.prepareMessageForHtml(message.text)']")
        window_handles = self.driver.window_handles
        print(f"""window_handles : {len(window_handles)}""")
        print(self.driver.current_url)
        print(self.driver.title)
        # script = """
        #     var element = document.querySelector('.message.error div');
        #     var computedStyle = window.getComputedStyle(element, '::before');
        #     var content = computedStyle.content;
        #
        #     return content;
        # """
        # script = """
        #     var element = document.querySelector('.message.error');
        #     var pseudoElement = window.getComputedStyle(element, ':before').getPropertyValue('content');
        #     var temp = document.createElement('div');
        #     temp.innerHTML = pseudoElement;
        #     var content = temp.textContent || temp.innerText;
        #     return content.replace(/['"]+/g, '');
        # """
        # result = self.driver.execute_script(script)
        # print(result)
        error_message_element = wait(self.driver, 30).until(EC.visibility_of_element_located(error_message_locator))
        print(error_message_element.text)
        # print("element")
        # error_message = self.driver.execute_script("return arguments[0].textContent;", error_message_element)
        # print(error_message)
        return error_message_element