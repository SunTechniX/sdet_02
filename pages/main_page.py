from .base_page import BasePage
from data.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser):
        super(MainPage, self).__init__(browser)

    def click_to_cart_pic(self) -> None:
        ''' Нажимает на "Корзинку", куда 'складыватся' продукты '''
        self.click_to_element(MainPageLocators.CART_PIC_LINK)

    def click_logout_btn(self) -> None:
        ''' Нажимает кнопку "Logout" (по требованию задания не используется) '''
        self.click_to_element(MainPageLocators.LOGOUT_BTN)

    def assert_logout_btn(self) -> None:
        ''' Проверяет наличия кнопки "Logout" '''
        assert self.is_element_present(MainPageLocators.LOGOUT_BTN), "Logout Button is not presented"
