from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):
    def check_cart_backpack_name(self, name):
        assert name == self.browser.find_element(*CartPageLocators.CART_BACKPACK_NAME).text, "BackPack Name is not equal"

    def check_cart_backpack_price(self, price):
        price_s = self.browser.find_element(*CartPageLocators.CART_BACKPACK_PRICE).text
        assert price == float(price_s[1:]), "BackPack Price is not equal"

    def check_cart_tshirt_name(self, name):
        assert name == self.browser.find_element(*CartPageLocators.CART_TSHIRT_NAME).text, "T-shirt Name is not equal"

    def check_cart_tshirt_price(self, price):
        price_s = self.browser.find_element(*CartPageLocators.CART_TSHIRT_PRICE).text
        assert price == float(price_s[1:]), "T-shirt Price is not equal"

    def click_checkout_button(self):
        self.browser.find_element(*CartPageLocators.CART_CHECKOUT_BUTTON).click()

    def get_cart_backpack_name(self):
        return self.browser.find_element(*CartPageLocators.CART_BACKPACK_NAME).text

    def get_cart_backpack_price(self):
        price_s = self.browser.find_element(*CartPageLocators.CART_BACKPACK_PRICE).text
        return float(price_s[1:])

    def get_cart_tshirt_name(self):
        return self.browser.find_element(*CartPageLocators.CART_TSHIRT_NAME).text

    def get_cart_tshirt_price(self):
        price_s = self.browser.find_element(*CartPageLocators.CART_TSHIRT_PRICE).text
        return float(price_s[1:])

    def should_be_cart_backpack_name(self):
        assert self.is_element_present(*CartPageLocators.CART_BACKPACK_NAME), "BackPack Name is not presented"

    def should_be_cart_backpack_price(self):
        assert self.is_element_present(*CartPageLocators.CART_BACKPACK_PRICE), "BackPack Price is not presented"

    def should_be_cart_tshirt_name(self):
        assert self.is_element_present(*CartPageLocators.CART_TSHIRT_NAME), "T-Shirt Name is not presented"

    def should_be_cart_tshirt_price(self):
        assert self.is_element_present(*CartPageLocators.CART_TSHIRT_PRICE), "T-Shirt Price is not presented"

    def should_be_checkout_button(self):
        assert self.is_element_present(*CartPageLocators.CART_CHECKOUT_BUTTON), "Checkout Button is not presented"
