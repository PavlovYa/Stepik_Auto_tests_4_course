from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver

driver = webdriver.Chrome()

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # driver.current_url
        assert "login" in self.browser.current_url, "Not login page"

    def should_be_login_field(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FIELD), "Login field is not presented"

    def should_be_pass_field(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.PASS_FIELD), "Pass field is not presented"