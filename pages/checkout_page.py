from .base_page import BasePage
from .locators import CheckoutPageLocators


class CheckoutPage(BasePage):
    def check_cart_backpack_name(self, name):
        assert name == self.browser.find_element(*CheckoutPageLocators.CHECKOUT_BACKPACK_NAME).text, "BackPack Name is not equal"

    def check_cart_tshirt_name(self, name):
        assert name == self.browser.find_element(*CheckoutPageLocators.CHECKOUT_TSHIRT_NAME).text, "T-shirt Name is not equal"

    def check_cart_subtotal_price(self, price):
        price_s = self.browser.find_element(*CheckoutPageLocators.CHECKOUT_SUBTOTAL_PRICE).text
        assert price == float(price_s[price_s.rfind('$') + 1:]), "Total Price is not equal"

    def click_continue_button(self):
        self.browser.find_element(*CheckoutPageLocators.CHECKOUT_CONTINUE_BUTTON).click()

    def click_finish_button(self):
        self.browser.find_element(*CheckoutPageLocators.CHECKOUT_FINISH_BUTTON).click()

    def should_be_continue_button(self):
        assert self.is_element_present(*CheckoutPageLocators.CHECKOUT_CONTINUE_BUTTON), "Continue Button is not presented"

    def should_be_cart_backpack_name(self):
        assert self.is_element_present(*CheckoutPageLocators.CHECKOUT_BACKPACK_NAME), "BackPack Name is not presented"

    def should_be_cart_tshirt_name(self):
        assert self.is_element_present(*CheckoutPageLocators.CHECKOUT_TSHIRT_NAME), "T-Shirt Name is not presented"

    def should_be_finish_button(self):
        assert self.is_element_present(*CheckoutPageLocators.CHECKOUT_FINISH_BUTTON), "Finish Button is not presented"

    def should_be_first_name_field(self):
        assert self.is_element_present(*CheckoutPageLocators.CHECKOUT_FIRST_NAME), "First Name Field is not presented"

    def should_be_last_name_field(self):
        assert self.is_element_present(*CheckoutPageLocators.CHECKOUT_LAST_NAME), "Last Name Field is not presented"

    def should_be_thanks_msg(self):
        assert self.is_element_present(*CheckoutPageLocators.CHECKOUT_THANKS_MSG), "Thenks Message is not presented"

    def should_be_postal_code_field(self):
        assert self.is_element_present(*CheckoutPageLocators.CHECKOUT_POSTAL_CODE), "Postal Code Field is not presented"

    def should_be_subtotal_price(self):
        assert self.is_element_present(*CheckoutPageLocators.CHECKOUT_SUBTOTAL_PRICE), "Total Price is not presented"

    def write_to_first_name_field(self, first_name):
        self.browser.find_element(*CheckoutPageLocators.CHECKOUT_FIRST_NAME).send_keys(first_name)

    def write_to_last_name_field(self, last_name):
        self.browser.find_element(*CheckoutPageLocators.CHECKOUT_LAST_NAME).send_keys(last_name)

    def write_to_postal_code_field(self, postal_code):
        self.browser.find_element(*CheckoutPageLocators.CHECKOUT_POSTAL_CODE).send_keys(postal_code)
