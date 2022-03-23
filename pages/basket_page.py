from final_project_Python_test.pages.base_page import BasePage
from final_project_Python_test.pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url

    def should_be_empty_basket(self):
        #empty_basket_message = self.browser.find_element(*BasePageLocators.EMPTY_BASKET)
        #assert empty_basket_message.text == "Your basket is empty.", "Корзина не пуста"
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET)




