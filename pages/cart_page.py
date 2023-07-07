from .main_page import MainPage
from data.locators import CartPageLocators


class CartPage(MainPage):
    def go_cart(self, cart_data: dict[str, float]) -> None:
        '''
        Проверяет содержимое корзины

        - Переходит в корзину
        - Проверяет полные наименования с корзине с данными сохранёнными в словаре
        - Проверяет цены товаров в корзине с данными сохранёнными в словаре
        - Нажимает внопку "Checkout"

        :param cart_data: словарь, хранящий полное название продукта и его цену
        '''
        self.click_to_cart_pic()
        for i, name, price in [(i, *d) for i, d in enumerate(cart_data.items(), start=1)]:
            self.equal_cart_name(i, name)
            self.equal_cart_price(i, price)

        self.click_checkout_button()

    def click_checkout_button(self) -> None:
        ''' Нажимает на кнопку "Checkout" '''
        self.click_to_element(CartPageLocators.CART_CHECKOUT_BUTTON)

    def equal_cart_name(self, num: int, name: str) -> None:
        '''
        Сравниает полное название name с названием WebElement-а по индексу num

        :param num: номер товара в списке
        :param name: полное наименование товара
        '''
        assert name == self.get_cart_name(num), f"{name} name is not equal"

    def equal_cart_price(self, num: int, price: float) -> None:
        '''
        Сравнивает цену price с 'ценой' (записью) WebElement-а по индексу num

        :param num: номер товара в списке
        :param price: цена товара
        '''
        assert price == self.get_cart_price(num), "Price is not equal"

    def get_cart_name(self, num: int) -> str:
        ''' По индексу num возвращает полное название товара, написанное на WebElement-е '''
        return self.get_element_text(CartPageLocators.cart_item(num, 'name'))

    def get_cart_price(self, num: int) -> float:
        ''' По индексу num возвращает цену товара, написанной на WebElement-е '''
        return float(self.get_element_text(CartPageLocators.cart_item(num, 'price')).replace('$', ''))
