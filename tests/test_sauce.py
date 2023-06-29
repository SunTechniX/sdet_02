import pytest

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage


@pytest.mark.sauce
class TestSauce():
    def test_sauce(self, browser):
        browser.delete_all_cookies()
        cart_data = dict()
        login_page = LoginPage(browser)
        login_page.login_procedure()
        products_page = ProductsPage(browser)
        products_page.add_to_cart(browser, 'Backpack', cart_data)
        products_page.add_to_cart(browser, 'T-Shirt', cart_data)
        cart_page = CartPage(browser)
        cart_page.go_cart(cart_data)
        checkout_page = CheckoutPage(browser)
        checkout_page.go_checkout(cart_data)
        checkout_page.assert_thanks_msg()
