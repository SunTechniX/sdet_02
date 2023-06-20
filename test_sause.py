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
        first_name = 'George'
        last_name = 'Michael'
        postal_code = '735690'
        cart_names = []
        cart_price = []
        link = LINK
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.should_be_username_field()
        login_page.write_to_username_field(user_name)
        login_page.should_be_password_field()
        login_page.write_to_password_field(user_pass)
        login_page.should_be_login_button()
        login_page.click_login_button()

        # Переходим на страницу продукции
        products_page = ProductsPage(browser, browser.current_url)
        products_page.should_be_product_backpack()
        products_page.click_to_product_backpack()

        # 'Провалились' в товар
        stuff_page = StuffPage(browser, browser.current_url)
        stuff_page.should_be_add_to_cart_button()
        stuff_page.click_add_to_cart()
        stuff_page.should_be_remove_from_cart_button()
        stuff_page.should_be_name()
        cart_names.append(stuff_page.get_name())
        stuff_page.should_be_price()
        cart_price.append(stuff_page.get_price())
        stuff_page.should_be_back_to_products_button()
        stuff_page.click_back_to_products()

        # Вернулись на страницу продукции
        products_page = ProductsPage(browser, browser.current_url)
        products_page.should_be_product_tshirt()
        products_page.click_to_product_tshirt()

        # 'Провалились' в товар
        stuff_page = StuffPage(browser, browser.current_url)
        stuff_page.should_be_add_to_cart_button()
        stuff_page.click_add_to_cart()
        stuff_page.should_be_remove_from_cart_button()
        stuff_page.should_be_name()
        cart_names.append(stuff_page.get_name())
        stuff_page.should_be_price()
        cart_price.append(stuff_page.get_price())
        stuff_page.should_be_back_to_products_button()
        stuff_page.click_back_to_products()

        # Переходим в корзину
        cart_page = CartPage(browser, browser.current_url)
        cart_page.should_be_cart_pic()
        cart_page.click_to_cart_pic()
        cart_page.should_be_cart_backpack_name()
        cart_page.should_be_cart_backpack_price()
        cart_page.should_be_cart_tshirt_name()
        cart_page.should_be_cart_tshirt_price()
        cart_page.check_cart_backpack_name(cart_names[0])
        cart_page.check_cart_backpack_price(cart_price[0])
        cart_page.check_cart_tshirt_name(cart_names[1])
        cart_page.check_cart_tshirt_price(cart_price[1])

        cart_page.should_be_checkout_button()
        cart_page.click_checkout_button()

        # Переходим в CHECKOUT
        checkout_page = CheckoutPage(browser, browser.current_url)
        checkout_page.should_be_first_name_field()
        checkout_page.should_be_last_name_field()
        checkout_page.should_be_postal_code_field()

        checkout_page.write_to_first_name_field(first_name)
        checkout_page.write_to_last_name_field(last_name)
        checkout_page.write_to_postal_code_field(postal_code)

        checkout_page.should_be_continue_button()
        checkout_page.click_continue_button()

        # Переходим в CHECKOUT - side 2
        checkout_page.should_be_cart_backpack_name()
        checkout_page.check_cart_backpack_name(cart_names[0])
        checkout_page.should_be_cart_tshirt_name()
        checkout_page.check_cart_tshirt_name(cart_names[1])
        checkout_page.should_be_subtotal_price()
        checkout_page.check_cart_subtotal_price(sum(cart_price))
        checkout_page.should_be_finish_button()
        checkout_page.click_finish_button()

        checkout_page.should_be_thanks_msg()

