import pytest

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage


@pytest.mark.sauce
class TestSauce():
    def test_sauce(self, browser, browser_del_cookie):
        cart_data = dict()
        login_page = LoginPage(browser)
        login_page.login_procedure()
        products_page = ProductsPage(browser)
        products_page.add_to_cart(browser, 'Backpack', cart_data)
        products_page.add_to_cart(browser, 'T-Shirt', cart_data)
        cart_page = CartPage(browser)
        cart_page.go_cart(cart_data)
        checkout_page = CheckoutPage(browser)
        checkout_page.fill_person_data_fields()
        for i, name in enumerate(cart_data.keys(), start=1):
            checkout_page.assert_cart_item_name(i, name)
        checkout_page.assert_cart_subtotal_price(sum(cart_data.values()))
        checkout_page.click_finish_button()
        checkout_page.assert_thanks_msg()
