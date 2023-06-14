import time
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver import ActionChains
from locators.wish_list_locators import WishListPageLocators as wl


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

    @allure.step('Move cursor to element. Perform a click action without navigating to a new page.')
    def action_move_to_element_click_no_new_window(self, locator):
        """
        This method moves the mouse cursor to the center of the selected element.
        Perform a click action without navigating to a new page
        """
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

