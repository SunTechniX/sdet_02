from .main_page import MainPage
from .locators import LoginPageLocators


class LoginPage(MainPage):
    def click_login_button(self):
        self.click_to_element(LoginPageLocators.LOGIN_BTN)

    def present_login_button(self):
        assert self.is_element_present(LoginPageLocators.LOGIN_BTN), "Login Button is not presented"

    def present_username_field(self):
        assert self.is_element_present(LoginPageLocators.USERNAME_FIELD), "Username Field is not presented"

    def present_password_field(self):
        assert self.is_element_present(LoginPageLocators.PASSWORD_FIELD), "Password Field is not presented"

    def write_to_username_field(self, user_name):
        self.write_to_element(LoginPageLocators.USERNAME_FIELD, user_name)

    def write_to_password_field(self, password):
        self.write_to_element(LoginPageLocators.PASSWORD_FIELD, password)
