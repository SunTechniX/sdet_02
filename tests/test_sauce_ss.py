import pytest

from pages_ss.login_page_ss import LoginPageSS
from pages_ss.cart_page_ss import CartPageSS
from pages_ss.checkout_page_ss import CheckoutPageSS
from pages_ss.products_page_ss import ProductsPageSS


@pytest.mark.sauce
class TestSauceSS:

    def test_sauce_ss(self, browser_selene, selene_del_cookie):
        cart_data = dict()
        login_page = LoginPageSS()
        login_page.login_procedure()
        products_page = ProductsPageSS()
        products_page.add_to_cart('Backpack', cart_data)
        products_page.add_to_cart('T-Shirt', cart_data)
        cart_page = CartPageSS()
        cart_page.go_cart(cart_data)
        checkout_page = CheckoutPageSS()
        checkout_page.fill_person_data_fields()
        items_name = checkout_page.get_items_from_cart(cart_data)
        checkout_page.assert_cart_item_name(1, next(items_name))
        checkout_page.assert_cart_item_name(2, next(items_name))
        checkout_page.assert_cart_subtotal_price(sum(cart_data.values()))
        checkout_page.click_finish_button()
        checkout_page.assert_thanks_msg()
