from .base_page import BasePage
from .locators import StuffPageLocators


class StuffPage(BasePage):
    def click_add_to_cart(self):
        self.browser.find_element(*StuffPageLocators.STUFF_ADD_TO_CART_BUTTON).click()

    def click_back_to_products(self):
        self.browser.find_element(*StuffPageLocators.STUFF_BACK_TO_PRODUCTS_BUTTON).click()

    def get_name(self):
        return self.browser.find_element(*StuffPageLocators.STUFF_NAME).text

    def get_price(self):
        price_s = self.browser.find_element(*StuffPageLocators.STUFF_PRICE).text
        return float(price_s[1:])

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*StuffPageLocators.STUFF_ADD_TO_CART_BUTTON), "Add-to-Cart button is not presented"

    def should_be_back_to_products_button(self):
        assert self.is_element_present(*StuffPageLocators.STUFF_BACK_TO_PRODUCTS_BUTTON), "Back-to-Products button is not presented"

    def should_be_name(self):
        assert self.is_element_present(*StuffPageLocators.STUFF_NAME), "Stuff Name is not presented"

    def should_be_price(self):
        assert self.is_element_present(*StuffPageLocators.STUFF_PRICE), "Price is not presented"

    def should_be_remove_from_cart_button(self):
        assert self.is_element_present(*StuffPageLocators.STUFF_REMOVE_FROM_CART_BUTTON), "Remove-from-Cart button is not presented"
