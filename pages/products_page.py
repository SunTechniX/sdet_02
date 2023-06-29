from .main_page import MainPage
from .stuff_page import StuffPage
from data.locators import ProductsPageLocators


class ProductsPage(MainPage):
    def add_to_cart(self, browser, stuff, cart_data):
        self.click_to_product(stuff)
        stuff_page = StuffPage(browser)
        stuff_page.click_add_to_cart()
        stuff_page.assert_remove_from_cart_button()
        cart_data[stuff_page.get_name()] = stuff_page.get_price()
        stuff_page.click_back_to_products()

    def click_to_product(self, name):
        product = self.get_element(ProductsPageLocators.product_name(name))
        self.scroll_to_element(product)
        product.click()
