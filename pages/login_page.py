from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        if 'login' in login_url:
        	assert True, "There is no substring 'login' on current page url"

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert True, "There is no login form on this page"

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert True, "There is no register form on this page"

    def register_new_user(self):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER)
        email = str(time.time()) + "@fakemail.org"
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER)
        password = str(time.time()) + "password"
        password_field.send_keys(password)
        password_confirm_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM_REGISTER)
        password_confirm_field.send_keys(password)
        register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register.click()