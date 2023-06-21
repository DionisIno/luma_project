import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver import ActionChains
from locators.wish_list_locators import WishListPageLocators as wl
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    @allure.step('Open a browser')
    def open(self):
        """This method opens a browser by the provided link"""
        self.driver.get(self.url)

    @allure.step('Find a visible element')
    def element_is_visible(self, locator, timeout=10):
        """
        This method expects to verify that the element is present in the DOM tree, visible, and displayed on the page.
        Visibility means that the element is not only displayed but also has a height and width greater than 0.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Find visible elements')
    def elements_are_visible(self, locator, timeout=10):
        """
        This method expects to verify that the elements are present in the DOM tree, visible and displayed on the page.
        Visibility means that the elements are not only displayed but also have a height and width greater than 0.
        Locator - is used to find the elements.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Find a present element')
    def element_is_present(self, locator, timeout=5):
        """
        This method expects to verify that the element is present in the DOM tree,
        but not necessarily visible and displayed on the page.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Find present elements')
    def elements_are_present(self, locator, timeout=5):
        """
           This method expects to verify that the elements are present in the DOM tree,
           but not necessarily visible and displayed on the page.
           Locator - is used to find the elements.
           Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
           """
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.step('Find a not visible element')
    def element_is_not_visible(self, locator, timeout=5):
        """
         This method expects to verify whether the element is invisible or not.
         The element is present in the DOM tree.
         Locator - is used to find the element.
         Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
         """
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step('Find clickable elements')
    def element_is_clickable(self, locator, timeout=5):
        """
        This method expects to verify that the element is visible, displayed on the page, and enabled.
        The element is present in the DOM tree.
        Locator - is used to find the element.
        Timeout - the duration it will wait for. The default is set to 5 seconds, but it can be modified if needed.
        """
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step('Go to specified element')
    def go_to_element(self, element):
        """
        This method scrolls the page to the selected element, making it visible to the user.
        """
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Move cursor to element')
    def action_move_to_element(self, element):
        """
        This method moves the mouse cursor to the center of the selected element, simulating a hover action.
        It can be used to test the interactivity of an element when the mouse cursor is hovering over it.
        """
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    @allure.step('Click on element and return it')
    def click_and_return_element(self, locator, seconds=15):
        """
        This method finds a visible element using the provided locator,
        performs a click action on it, and then returns the element.
        Locator - is used to find the element.
        """
        element = self.element_is_visible(locator)
        wait(self.driver, seconds)
        element.click()
        return element

    @allure.step('Check element hover style')
    def check_element_hover_style(self, locator, css_property, seconds=10):
        """
        This method finds a visible element using the provided locator,
        simulates a hover action by moving the cursor to it,
        and then returns the value of the specified CSS property of the element.
        Locator - is used to find the element.
        Css_property - the name of the CSS property whose value is to be returned.
        """
        element = self.element_is_visible(locator)  # Get the WebElement using locator
        wait(self.driver, seconds)
        self.action_move_to_element(element)  # Move to the element
        return element.value_of_css_property(css_property)

    @allure.step('Check element hover style using JavaScript')
    def check_element_hover_style_using_js(self, element, css_property):
        """
        This method finds a visible element using the provided locator,
        simulates a hover action by moving the cursor to it,
        and then returns the value of the specified CSS property of the element using JavaScript.
        Locator - is used to find the element.
        Css_property - the name of the CSS property whose value is to be returned.
        """
        element_property = self.driver.execute_script(
            f"return getComputedStyle(arguments[0]).getPropertyValue('{css_property}');", element)
        return element_property

    @allure.step('Get element text')
    def get_text(self, locator):
        """
        This method get element text
        :return: element text
        """
        text = self.element_is_visible(locator)
        return text.text

    def delete_my_wish_list(self):
        elements = self.elements_are_visible(wl.ADDED_CARD_TO_MY_WISH_LIST)
        try:
            flag = True
            while flag:
                print(len(elements))
                self.action_move_to_element(elements[0])
                button = self.element_is_present(wl.DELETE_CARD_BUTTON)
                self.driver.execute_script("arguments[0].click();", button)
                if len(elements) == 0:
                    flag = False
        except StaleElementReferenceException:
            pass

    @allure.step('Checking if 1 or more browser windows are open. If the 2nd is detected, then it returns to the 1st')
    def switch_between_opened_windows(self):
        """
        Checking if 1 or more browser windows are open
        If the 2nd is detected, then it returns to the 1st
        """
        try:
            current_url = self.driver.current_url
            print("Current URL (base_page try): ", current_url)
            second_window = self.driver.window_handles[1]
            if second_window:
                first_window = self.driver.window_handles[0]
                print('Window[0]: ', first_window)
                self.driver.switch_to.window(first_window)
                current_url = self.driver.current_url
                print("Current URL (base_page try, if): ", current_url)

        except:
            print("There is only one window. The second window is not revealed. The presence of a third, not tested.")

    @allure.step('Shows all opened windows')
    def show_all_opened_windows(self):
        """
        Shows all opened windows
        """
        handles = self.driver.window_handles
        size = len(handles)

        if size == 1:
            print('Additional windows not found. Only one active browser window found.')
        else:
            print('Number of detected windows: ', size)

            for x in range(size):
                self.driver.switch_to.window(handles[x])
                print(self.driver.title)

    @allure.step('Find element (unpacking)')
    def find_element(self, locator):
        """Find element (unpacking)"""
        return self.driver.find_element(*locator)

    @allure.step('Move cursor to element. Perform a click action without navigating to a new page')
    def action_move_to_element_click_no_new_window(self, locator):
        """
        This method moves the mouse cursor to the center of the selected element.
        Perform a click action without navigating to a new page
        """
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step(
        'Click not in the center of the selector, but in its right part, to the right from the center by 5 pixels')
    def click_to_the_right_of_the_center_of_the_locator_by_5_pixels(self, locator, timeout=5):
        """
        Click not in the center of the selector, but in its right part,
        to the right from the center by 5 pixels
        """
        element = wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, 5, 0)
        actions.click().perform()

    @allure.step(
        'Click not in the center of the selector, but in its right part, with a margin from the right edge of 5 pixels')
    def count_the_number_of_elements_with_the_same_selectors(self, locator, timeout=5):
        """
        Count number of elements with same selectors
        Can be used if there are fields to fill in and the field filling error has the same locator,
        you can understand the number of incorrectly filled fields or not filled at all
        """
        elements = wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        count = len(elements)
        print("Number of elements with the same (or FAIL) locators: ", count)

    def debug_headless_CI_in_GitHub_Actions_if_no_CSS_selector_found(self):
        """
        Getting all CSS elements on a page and outputting them to a CI report
        CI debugging options
        """
        ALL_CSS_ELEMENTS_ON_PAGE = (By.CSS_SELECTOR, '*')
        # elements = self.driver.find_element(ALL_CSS_ELEMENTS_ON_PAGE)
        try:
            elements = self.driver.execute_script("return document.querySelectorAll('*')")
            for element in elements:
                tag_name = element.tag_name
                text = element.text
                attributes = element.get_attribute("outerHTML")
                print(f"Tag Name: {tag_name}")
                print(f"Text: {text}")
                print(f"Attributes: {attributes}")
                print("--------")
        except:
            print('At this stage, an error appeared in the output of additional elements')

    @allure.step(
        'Click not in the center of the selector, but in its right part, to the right from the center by 45 pixels')
    def click_to_the_right_of_the_center_of_the_locator_by_45_pixels(self, locator, timeout=5):
        """
        Click not in the center of the selector, but in its right part,
        to the right from the center by 45 pixels
        """
        element = wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, 45, 0)
        actions.click().perform()

    @allure.step('Get required element visible')
    def find_required_element(self):
        """
        This method finds a required element, making it visible to the user.
        """
        return "return window.getComputedStyle(arguments[0],'::after').getPropertyValue('content')"

    @allure.step("Getting actual URL of the current webpage")
    def get_actual_url_of_current_page(self):
        """
        This method allows to get URL of the current page
        """
        actual_url = self.driver.current_url
        return actual_url

    @allure.step("Getting actual title of the current webpage")
    def get_actual_title_of_current_page(self):
        """
        This method allows to get a title of the current page
        """
        actual_title = self.driver.title
        return actual_title

    @allure.step(
        'Click not in the center of the selector, but in its right part, to the right from the center by 45 pixels')
    def click_to_the_right_of_the_center_of_the_locator_by_95_pixels(self, locator, timeout=5):
        """
        Click not in the center of the selector, but in its right part,
        to the right from the center by 95 pixels
        """
        element = wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element_with_offset(element, 95, 0)
        actions.click().perform()
