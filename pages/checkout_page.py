from .main_page import MainPage
from .locators import CheckoutPageLocators


class CheckoutPage(MainPage):
    def assert_cart_backpack_name(self, name):
        assert name == self.get_element_text(CheckoutPageLocators.CHECKOUT_BACKPACK_NAME), "BackPack Name is not equal"

    def assert_cart_tshirt_name(self, name):
        assert name == self.get_element_text(CheckoutPageLocators.CHECKOUT_TSHIRT_NAME), "T-shirt Name is not equal"

    def assert_cart_subtotal_price(self, price):
        price_s = self.get_element_text(CheckoutPageLocators.CHECKOUT_SUBTOTAL_PRICE)
        assert price == float(price_s[price_s.rfind('$') + 1:]), "Total Price is not equal"

    def click_continue_button(self):
        self.click_to_element(CheckoutPageLocators.CHECKOUT_CONTINUE_BUTTON)

    def click_finish_button(self):
        self.click_to_element(CheckoutPageLocators.CHECKOUT_FINISH_BUTTON)

    def present_continue_button(self):
        assert self.is_element_present(CheckoutPageLocators.CHECKOUT_CONTINUE_BUTTON), "Continue Button is not presented"

    def present_cart_backpack_name(self):
        assert self.is_element_present(CheckoutPageLocators.CHECKOUT_BACKPACK_NAME), "BackPack Name is not presented"

    def present_cart_tshirt_name(self):
        assert self.is_element_present(CheckoutPageLocators.CHECKOUT_TSHIRT_NAME), "T-Shirt Name is not presented"

    def present_finish_button(self):
        assert self.is_element_present(CheckoutPageLocators.CHECKOUT_FINISH_BUTTON), "Finish Button is not presented"

    def present_first_name_field(self):
        assert self.is_element_present(CheckoutPageLocators.CHECKOUT_FIRST_NAME), "First Name Field is not presented"

    def present_last_name_field(self):
        assert self.is_element_present(CheckoutPageLocators.CHECKOUT_LAST_NAME), "Last Name Field is not presented"

    def present_thanks_msg(self):
        assert self.is_element_present(CheckoutPageLocators.CHECKOUT_THANKS_MSG), "Thenks Message is not presented"

    def present_postal_code_field(self):
        assert self.is_element_present(CheckoutPageLocators.CHECKOUT_POSTAL_CODE), "Postal Code Field is not presented"

    def present_subtotal_price(self):
        assert self.is_element_present(CheckoutPageLocators.CHECKOUT_SUBTOTAL_PRICE), "Total Price is not presented"

    def write_to_first_name_field(self, first_name):
        self.write_to_element(CheckoutPageLocators.CHECKOUT_FIRST_NAME, first_name)

    def write_to_last_name_field(self, last_name):
        self.write_to_element(CheckoutPageLocators.CHECKOUT_LAST_NAME, last_name)

    def write_to_postal_code_field(self, postal_code):
        self.write_to_element(CheckoutPageLocators.CHECKOUT_POSTAL_CODE, postal_code)
