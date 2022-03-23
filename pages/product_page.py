from selenium.webdriver.common.by import By

from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def assert_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert item_name == self.browser.find_element(By.CSS_SELECTOR, "div.alertinner strong").text, "Не совпадает название книги"

    def assert_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert item_price == self.browser.find_element(By.CSS_SELECTOR, "div.alertinner p strong").text, "Не совпадает цена товара со стоимостью корзины"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"

    def add_item_to_basket(self):
        add_to_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_to_button.click()