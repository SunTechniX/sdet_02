from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def click_to_cart_pic(self):
        self.click_to_element(MainPageLocators.CART_PIC_LINK)

    def click_logout_btn(self):
        self.click_to_element(MainPageLocators.LOGOUT_BTN)

    def present_cart_pic(self):
        assert self.is_element_present(MainPageLocators.CART_PIC_LINK), "Cart picture link is not presented"

    def present_logout_btn(self):
        assert self.is_element_present(MainPageLocators.LOGOUT_BTN), "Logout Button is not presented"
