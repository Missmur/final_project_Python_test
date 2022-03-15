from .pages import product_page
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
import time


def test_quest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.assert_item_price()
    page.assert_item_name()


