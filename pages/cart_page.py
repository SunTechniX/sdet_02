from .main_page import MainPage
from data.locators import CartPageLocators


class CartPage(MainPage):
    def go_cart(self, cart_data: dict[str, float]) -> None:
        '''
        Проверить содержимое корзины

        - Перейти в корзину
        - Проверить полные наименования с корзине с данными сохранёнными в словаре
        - Проверить цены товаров в корзине с данными сохранёнными в словаре
        - Нажать внопку "Checkout"

        :param cart_data: словарь, хранящий полное название продукта (str) и его цену (float)
        '''
        self.click_to_cart_pic()
        for i, name, price in [(i, *d) for i, d in enumerate(cart_data.items(), start=1)]:
            self.equal_cart_name(i, name)
            self.equal_cart_price(i, price)

        self.click_checkout_button()

    def click_checkout_button(self) -> None:
        ''' Нажать на кнопку "Checkout" '''
        self.click_to_element(CartPageLocators.CART_CHECKOUT_BUTTON)

    def equal_cart_name(self, num: int, name: str) -> None:
        '''
        Сравнить полное название name с названием WebElement-а по индексу num

        :param num: номер товара в списке (int)
        :param name: полное наименование товара (str)
        '''
        assert name == self.get_cart_name(num), f"{name} name is not equal"

    def equal_cart_price(self, num: int, price: float) -> None:
        '''
        Сравнить цену price с 'ценой' (записью) WebElement-а по индексу num

        :param num: номер товара в списке (int)
        :param price: цена товара (float)
        '''
        assert price == self.get_cart_price(num), "Price is not equal"

    def get_cart_name(self, num: int) -> str:
        ''' По индексу num возвращает полное название товара, написанное на WebElement-е '''
        return self.get_element_text(CartPageLocators.cart_item(num, 'name'))

    def get_cart_price(self, num: int) -> float:
        ''' По индексу num возвращает цену товара, написанной на WebElement-е '''
        return float(self.get_element_text(CartPageLocators.cart_item(num, 'price')).replace('$', ''))
