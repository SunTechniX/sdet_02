from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def click_to_cart_pic(self):
        self.browser.find_element(*CartPageLocators.CART_PIC_LINK).click()

    def should_be_cart_pic(self):
        assert self.is_element_present(*CartPageLocators.CART_PIC_LINK), "Cart picture link is not presented"
