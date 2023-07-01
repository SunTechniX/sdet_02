from .main_page import MainPage
from .stuff_page import StuffPage
from data.locators import ProductsPageLocators


class ProductsPage(MainPage):
    def add_to_cart(self, browser, stuff: str, cart_data: dict) -> None:
        '''
        Поместить товар в корзину

        В списке продуктов кликает на продукт stuff
        'проваливается' в страницу продукта
        кликает на кнопку 'Add to cart'
        проверяет, что на странице есть кнопка 'Remove' (появляется вместо кнопку 'Add to cart')
        полное название продукта и его цена сохраняются в словарь cart_data
        нажимается ссылка 'Back to products'

        :param stuff: название товара, который нужно положить в корзину, например 'Backpack', 'T-Shirt'
        :param cart_data: словарь, хранящий полное название продукта (str) и его цену (float)
        '''
        self.click_to_product(stuff)
        stuff_page = StuffPage(browser)
        stuff_page.click_add_to_cart()
        stuff_page.assert_remove_from_cart_button()
        cart_data[stuff_page.get_name()] = stuff_page.get_price()
        stuff_page.click_back_to_products()

    def click_to_product(self, name: str):
        ''' Проскроллировать страницу до продукта и кликнуть по нему '''
        product = self.get_element(ProductsPageLocators.product_name(name))
        self.scroll_to_element(product)
        product.click()
