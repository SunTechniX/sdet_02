from .base_page import BasePage
from .locators import CheckoutPageLocators


class CheckoutPage(BasePage):
    def click_to_checkout_button(self):
        self.browser.find_element(*CheckoutPageLocators.CART_PIC_LINK).click()
