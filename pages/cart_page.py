from .main_page import MainPage
from .locators import CartPageLocators


class CartPage(MainPage):
    def assert_cart_name(self, num, name):
        assert name == self.get_element_text(CartPageLocators.cart_item(num, 'name')), name + " Name is not equal"

    def assert_cart_price(self, num, price):
        price_s = self.get_element_text(CartPageLocators.cart_item(num, 'price'))
        assert price == float(price_s[1:]), "Price is not equal"

    def click_checkout_button(self):
        self.click_to_element(CartPageLocators.CART_CHECKOUT_BUTTON)

    def get_cart_name(self, num):
        return self.get_element_text(CartPageLocators.cart_item(num, 'name'))

    def get_cart_price(self, num):
        price_s = self.get_element_text(CartPageLocators.cart_item(num, 'price'))
        return float(price_s[1:])

    def present_cart_name(self, num):
        assert self.is_element_present(CartPageLocators.cart_item(num, 'name')), "Name is not presented"

    def present_cart_price(self, num):
        assert self.is_element_present(CartPageLocators.cart_item(num, 'price')), "Price is not presented"

    def present_checkout_button(self):
        assert self.is_element_present(CartPageLocators.CART_CHECKOUT_BUTTON), "Checkout Button is not presented"
