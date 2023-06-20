# pytest -v -s -m harry_potter test_sause.py
# pytest -v -s test_sause.py

import pytest
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
from .pages.checkout_page import CheckoutPage
from .pages.products_page import ProductsPage
from .pages.stuff_page import StuffPage


LINK = "https://www.saucedemo.com/"

@pytest.mark.sause
class TestSause():
    #link = LINK

    def test_sause(self, browser):
        browser.delete_all_cookies()
        user_name = 'standard_user'
        user_pass = 'secret_sauce'
        cart_price = 0
        link = LINK
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.should_be_username_field()
        login_page.write_to_username_field(user_name)
        login_page.should_be_password_field()
        login_page.write_to_password_field(user_pass)
        login_page.should_be_login_button()
        login_page.click_login_button()

        products_page = ProductsPage(browser, browser.current_url)
        products_page.should_be_product_backpack()
        products_page.click_to_product_backpack()

        stuff_page = StuffPage(browser, browser.current_url)
        stuff_page.should_be_add_to_cart_button()
        stuff_page.click_add_to_cart()
        stuff_page.should_be_remove_from_cart_button()
        stuff_page.should_be_back_to_products_button()
        stuff_page.should_be_price()
        cart_price += stuff_page.get_price()
        stuff_page.click_back_to_products()

        products_page = ProductsPage(browser, browser.current_url)
        products_page.should_be_product_tshirt()
        products_page.click_to_product_tshirt()

        stuff_page = StuffPage(browser, browser.current_url)
        stuff_page.should_be_add_to_cart_button()
        stuff_page.click_add_to_cart()
        stuff_page.should_be_remove_from_cart_button()
        stuff_page.should_be_back_to_products_button()
        stuff_page.should_be_price()
        cart_price += stuff_page.get_price()
        stuff_page.click_back_to_products()

        products_page = ProductsPage(browser, browser.current_url)
        print(cart_price)
