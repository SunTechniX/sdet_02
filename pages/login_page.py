from .main_page import MainPage
from data.locators import LoginPageLocators
from data.login_data import LoginData


class LoginPage(MainPage):
    def login_procedure(self) -> None:
        ''' Заполнить поля именем, паролем и нажать кнопку 'Login' '''
        self.write_to_element(LoginPageLocators.USERNAME_FIELD, LoginData.USER)
        self.write_to_element(LoginPageLocators.PASSWORD_FIELD, LoginData.PASS)
        self.click_to_element(LoginPageLocators.LOGIN_BTN)
