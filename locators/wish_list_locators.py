from selenium.webdriver.common.by import By


class WishListPageLocators:

    ADDED_CARD_TO_MY_WISH_LIST = (By.CSS_SELECTOR, "div[class='products-grid wishlist'] li[class='product-item']")
    DELETE_CARD_BUTTON = (By.CSS_SELECTOR, "a[data-role='remove']")
