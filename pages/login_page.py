from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def click_login_button(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).click()

    def write_to_username_field(self, user_name):
        self.browser.find_element(*LoginPageLocators.USERNAME_FIELD).send_keys(user_name)

    def write_to_password_field(self, password):
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)

    def should_be_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), "Login Button is not presented"

    def should_be_username_field(self):
        assert self.is_element_present(*LoginPageLocators.USERNAME_FIELD), "Username Field is not presented"

    def should_be_password_field(self):
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FIELD), "Password Field is not presented"
