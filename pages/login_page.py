from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        current_url = webdriver.current_url
        assert (*LoginPageLocators.LOGIN_URL) in current_url, "'login' is not in current url"

    def should_be_login_form(self):
        self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), "Register form is not presented"
