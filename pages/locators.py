from selenium.webdriver.common.by import By


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group a")


class ProductPageLocators:
    ITEM_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    ITEM_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    ADD_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button.btn")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages")


class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner p")
