import pytest
from .data import Data
from .pages.login_page import LoginPage
from .pages.cart_page import CartPage
from .pages.checkout_page import CheckoutPage
from .pages.products_page import ProductsPage
from .pages.stuff_page import StuffPage


@pytest.mark.sauce
class TestSauce():
    def add_to_cart(self, browser, cart_names, cart_price):
        stuff_page = StuffPage(browser, browser.current_url)
        stuff_page.present_add_to_cart_button()
        stuff_page.click_add_to_cart()
        stuff_page.present_remove_from_cart_button()
        stuff_page.present_name()
        cart_names.append(stuff_page.get_name())
        stuff_page.present_price()
        cart_price.append(stuff_page.get_price())
        stuff_page.present_back_to_products_button()
        stuff_page.click_back_to_products()

    def test_sauce(self, browser):
        browser.delete_all_cookies()
        user_name = Data.USER
        user_pass = Data.PASS
        first_name = Data.FIRST_NAME
        last_name = Data.LAST_NAME
        postal_code = Data.POSTAL_CODE
        cart_names = []
        cart_price = []
        link = Data.LINK

        login_page = LoginPage(browser, link)
        login_page.open_url()
        login_page.present_username_field()
        login_page.write_to_username_field(user_name)
        login_page.present_password_field()
        login_page.write_to_password_field(user_pass)
        login_page.present_login_button()
        login_page.click_login_button()

        products_page = ProductsPage(browser, browser.current_url)
        products_page.present_product('Backpack')
        products_page.click_to_product('Backpack')

        self.add_to_cart(browser, cart_names, cart_price)

        products_page = ProductsPage(browser, browser.current_url)
        products_page.present_product('T-Shirt')
        products_page.click_to_product('T-Shirt')

        self.add_to_cart(browser, cart_names, cart_price)

        cart_page = CartPage(browser, browser.current_url)
        cart_page.present_cart_pic()
        cart_page.click_to_cart_pic()
        cart_page.present_cart_name(1)
        cart_page.present_cart_price(1)
        cart_page.present_cart_name(2)
        cart_page.present_cart_price(2)
        cart_page.assert_cart_name(1, cart_names[0])
        cart_page.assert_cart_price(1, cart_price[0])
        cart_page.assert_cart_name(2, cart_names[1])
        cart_page.assert_cart_price(2, cart_price[1])

        cart_page.present_checkout_button()
        cart_page.click_checkout_button()

        checkout_page = CheckoutPage(browser, browser.current_url)
        checkout_page.present_first_name_field()
        checkout_page.present_last_name_field()
        checkout_page.present_postal_code_field()

        checkout_page.write_to_first_name_field(first_name)
        checkout_page.write_to_last_name_field(last_name)
        checkout_page.write_to_postal_code_field(postal_code)

        checkout_page.present_continue_button()
        checkout_page.click_continue_button()


        checkout_page.present_cart_backpack_name()
        checkout_page.assert_cart_backpack_name(cart_names[0])
        checkout_page.present_cart_tshirt_name()
        checkout_page.assert_cart_tshirt_name(cart_names[1])
        checkout_page.present_subtotal_price()
        checkout_page.assert_cart_subtotal_price(sum(cart_price))
        checkout_page.present_finish_button()
        checkout_page.click_finish_button()

        checkout_page.present_thanks_msg()

