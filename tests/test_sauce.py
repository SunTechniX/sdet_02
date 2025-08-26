import pytest

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.products_page import ProductsPage


@pytest.mark.sauce
class TestSauce:

    def test_sauce(self, browser_fixture, browser_del_cookie):
        cart_data = dict()
        login_page = LoginPage(browser_fixture)
        login_page.login_procedure()
        products_page = ProductsPage(browser_fixture)
        products_page.add_to_cart(browser_fixture, 'Backpack', cart_data)
        products_page.add_to_cart(browser_fixture, 'T-Shirt', cart_data)
        cart_page = CartPage(browser_fixture)
        cart_page.go_cart(cart_data)
        checkout_page = CheckoutPage(browser_fixture)
        checkout_page.fill_person_data_fields()
        items_name = checkout_page.get_items_from_cart(cart_data)
        checkout_page.assert_cart_item_name(1, next(items_name))
        checkout_page.assert_cart_item_name(2, next(items_name))
        checkout_page.assert_cart_subtotal_price(sum(cart_data.values()))
        checkout_page.click_finish_button()
        checkout_page.assert_thanks_msg()
