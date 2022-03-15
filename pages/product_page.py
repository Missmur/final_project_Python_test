from selenium.webdriver.common.by import By

from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def assert_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert item_name in self.browser.find_element(By.CSS_SELECTOR, "div.alertinner strong").text, "Не совпадает название книги"

    def assert_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert item_price in self.browser.find_element(By.CSS_SELECTOR, "div.alertinner p strong").text, "Не совпадает цена товара со стоимостью корзины"
