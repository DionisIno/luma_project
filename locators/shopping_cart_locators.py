"""This section contains locators for Shopping Cart page"""

from selenium.webdriver.common.by import By


class ShoppingCartPageLocators:
    TITLE = (By.CSS_SELECTOR, '[data-ui-id="page-title-wrapper"]')
    IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, 'div.cart-empty > p:nth-child(1)')
    HERE_LINK = (By.CSS_SELECTOR, 'div.cart-empty > p:nth-child(2) > a')
    SIZE_BUTTON = (By.CSS_SELECTOR, '#option-label-size-143-item-166')
    COLOR_BUTTON = (By.CSS_SELECTOR, '#option-label-color-93-item-53')
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '#product-addtocart-button')
    SHOPPING_CART_LINK = (By.CSS_SELECTOR,'div[data-bind="html: $parent.prepareMessageForHtml(message.text)"]>a')
    QUANTITY_FIELD = (By.CSS_SELECTOR, "input.input-text.qty")
    UPDATE_BUTTON = (By.CSS_SELECTOR, "button.action.update")




    
