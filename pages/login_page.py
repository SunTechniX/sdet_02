from .main_page import MainPage
from data.locators import LoginPageLocators
from data.login_data import LoginData


class LoginPage(MainPage):
    def login_procedure(self) -> None:
        ''' Заполняет поля именем, паролем и нажать кнопку 'Login' '''
        self.write_to_element(LoginPageLocators.login_field('user-name'), LoginData.USER)
        self.write_to_element(LoginPageLocators.login_field('password'), LoginData.PASS)
        self.click_to_element(LoginPageLocators.login_field('login-button'))
