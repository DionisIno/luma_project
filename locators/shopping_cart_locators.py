"""This section contains locators for Shopping Cart page"""
import random
# from pages.shopping_cart_page import ShoppingCartPage
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
    PRICE_ITEM = (By.CSS_SELECTOR, '#shopping-cart-table > tbody > tr.item-info > td.col.price > span > span > span')
    SUBTOTAL_ITEM = (By.CSS_SELECTOR, "td.col.subtotal span.price")
    SUBTOTAL_SUMMARY = (By.CSS_SELECTOR, 'td.amount span[data-th="Subtotal"]')
    DISCOUNT_SUMMARY = (By.CSS_SELECTOR, 'tbody > tr:nth-child(2) > td > span > span')
    TAX_SUMMARY = (By.CSS_SELECTOR, '#cart-totals > div > table > tbody > tr.totals-tax > td > span')
    ORDER_TOTAL = (By.CSS_SELECTOR, '.grand.totals > td > strong > span')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "button.action.primary.checkout span")
    DELETE_BUTTON = (By.CSS_SELECTOR, "a.action.action-delete")
    TABLE_HEADERS = {
        "Item": (By.CSS_SELECTOR, 'th.col.item span'),
        "Price": (By.CSS_SELECTOR, 'th.col.price span'),
        "Qty": (By.CSS_SELECTOR, 'th.col.qty span'),
        "Subtotal": (By.CSS_SELECTOR, 'th.col.subtotal span')
    }
    TITLE_ITEMS = (By.CSS_SELECTOR, " td.col.item > div > strong > a")

    # Apply Discount Code
    APPLY_DISCOUNT_CODE = (By.CSS_SELECTOR, "#block-discount-heading")
    INPUT_DISCOUNT_CODE = (By.CSS_SELECTOR, "#coupon_code")
    BTN_APPLY_DISCOUNT = (By.CSS_SELECTOR, "#discount-coupon-form > div > div.actions-toolbar > div > button")
    MSG_CODE_IS_NOT_VALID = (By.CSS_SELECTOR, "#maincontent > div.page.messages > div:nth-child(2) > div > div > div")

    # More Choices
    num = random.randint(2, 4)
    MORE_CHOICES_ITEMS_LIST = (By.CSS_SELECTOR, f"div.block-content.content > div > ol > li > div")
    CARD_ITEM_MORE_CHOICES = (By.CSS_SELECTOR, f"div.block-content.content > div > ol > li:nth-child({num}) > div")
    TITLE_ITEM_MORE_CHOICES = (By.CSS_SELECTOR, f".block-content.content > div > ol > li:nth-child({num}) > div > div > strong > a")
    PRICE_ITEM_MORE_CHOICES = (By.CSS_SELECTOR, "div.price-box.price-final_price > span")
    BTNS_ADD_TO_CART = (By.XPATH, f"//div[1]/ol[1]/li[{num}]//button[1]")
    
