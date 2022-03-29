from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        email_place = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
        email_place.send_keys(email)
        password = str(time.time()) + "pass"
        password_place = self.browser.find_element(*LoginPageLocators.REG_PASSWORD)
        password_place.send_keys(password)
        password_confirm = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        password_confirm.send_keys(password)
        submit_reg = self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON)
        submit_reg.click()
