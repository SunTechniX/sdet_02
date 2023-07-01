from .main_page import MainPage
from data.locators import CartPageLocators


class CartPage(MainPage):
    def go_cart(self, cart_data):
        self.click_to_cart_pic()
        for i, name, price in [(i, *d) for i, d in enumerate(cart_data.items(), start=1)]:
            self.equal_cart_name(i, name)
            self.equal_cart_price(i, price)

        self.click_checkout_button()

    def click_checkout_button(self):
        self.click_to_element(CartPageLocators.CART_CHECKOUT_BUTTON)

    def equal_cart_name(self, num, name):
        assert name == self.get_cart_name(num), f"{name} name is not equal"

    def equal_cart_price(self, num, price):
        assert price == self.get_cart_price(num), "Price is not equal"

    def get_cart_name(self, num):
        return self.get_element_text(CartPageLocators.cart_item(num, 'name'))

    def get_cart_price(self, num):
        return float(self.get_element_text(CartPageLocators.cart_item(num, 'price')).replace('$', ''))

