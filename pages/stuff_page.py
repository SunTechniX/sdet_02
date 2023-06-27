from .main_page import MainPage
from .locators import StuffPageLocators


class StuffPage(MainPage):
    def click_add_to_cart(self):
        self.click_to_element(StuffPageLocators.STUFF_ADD_TO_CART_BUTTON)

    def click_back_to_products(self):
        self.click_to_element(StuffPageLocators.STUFF_BACK_TO_PRODUCTS_BUTTON)

    def get_name(self):
        return self.get_element_text(StuffPageLocators.STUFF_NAME)

    def get_price(self):
        price_s = self.get_element_text(StuffPageLocators.STUFF_PRICE)
        return float(price_s[1:])

    def present_add_to_cart_button(self):
        assert self.is_element_present(StuffPageLocators.STUFF_ADD_TO_CART_BUTTON),\
            "Add-to-Cart button is not presented"

    def present_back_to_products_button(self):
        assert self.is_element_present(StuffPageLocators.STUFF_BACK_TO_PRODUCTS_BUTTON),\
            "Back-to-Products button is not presented"

    def present_name(self):
        assert self.is_element_present(StuffPageLocators.STUFF_NAME), "Stuff Name is not presented"

    def present_price(self):
        assert self.is_element_present(StuffPageLocators.STUFF_PRICE), "Price is not presented"

    def present_remove_from_cart_button(self):
        assert self.is_element_present(StuffPageLocators.STUFF_REMOVE_FROM_CART_BUTTON),\
            "Remove-from-Cart button is not presented"
