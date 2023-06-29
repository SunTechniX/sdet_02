from .main_page import MainPage
from data.locators import CheckoutPageLocators
from data.person_data import PersonData


class CheckoutPage(MainPage):
    def assert_cart_item_name(self, num, name):
        assert name == self.get_element_text(CheckoutPageLocators.checkout_product_name(num)),\
            f"Item {name} is not equal"

    def assert_cart_subtotal_price(self, price):
        price_s = self.get_element_text(CheckoutPageLocators.CHECKOUT_SUBTOTAL_PRICE)
        assert price == float(price_s[price_s.rfind('$') + 1:]), "Total Price is not equal"

    def assert_thanks_msg(self):
        assert self.is_element_present(CheckoutPageLocators.CHECKOUT_THANKS_MSG), "Thanks Message is not presented"

    def click_continue_button(self):
        self.click_to_element(CheckoutPageLocators.CHECKOUT_CONTINUE_BUTTON)

    def click_finish_button(self):
        self.click_to_element(CheckoutPageLocators.CHECKOUT_FINISH_BUTTON)

    def fill_person_data_fields(self):
        self.write_to_element(CheckoutPageLocators.CHECKOUT_FIRST_NAME, PersonData.FIRST_NAME)
        self.write_to_element(CheckoutPageLocators.CHECKOUT_LAST_NAME, PersonData.LAST_NAME)
        self.write_to_element(CheckoutPageLocators.CHECKOUT_POSTAL_CODE, PersonData.POSTAL_CODE)
        self.click_continue_button()

    def go_checkout(self, cart_data):
        self.fill_person_data_fields()
        for i, name in enumerate(cart_data.keys(), start=1):
            self.assert_cart_item_name(i, name)

        self.assert_cart_subtotal_price(sum(cart_data.values()))
        self.click_finish_button()
