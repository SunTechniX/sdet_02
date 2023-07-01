from .main_page import MainPage
from data.locators import CheckoutPageLocators
from data.person_data import PersonData


class CheckoutPage(MainPage):
    def assert_cart_item_name(self, num: int, name: str) -> None:
        '''
        Проверить, что название name совпадает с названием по индексу num из списка

        :param num: номер товара в списке (int)
        :param name: полное наименование товара (str)
        '''
        assert name == self.get_element_text(CheckoutPageLocators.checkout_product_name(num)),\
            f"Item {name} is not equal"

    def assert_cart_subtotal_price(self, price: float) -> None:
        '''
        Проверить, что общая стоимость price совпадает с общей стоимостью на странице

        :param price: цена товара (float)
        '''
        price_s = self.get_element_text(CheckoutPageLocators.CHECKOUT_SUBTOTAL_PRICE)
        assert price == float(price_s[price_s.rfind('$') + 1:]), "Total Price is not equal"

    def assert_thanks_msg(self) -> None:
        ''' Проверка, что на странице есть текст с благодарностью '''
        assert self.is_element_present(CheckoutPageLocators.CHECKOUT_THANKS_MSG), "Thanks Message is not presented"

    def click_continue_button(self) -> None:
        ''' Нажать на кнопку "Contunue" '''
        self.click_to_element(CheckoutPageLocators.CHECKOUT_CONTINUE_BUTTON)

    def click_finish_button(self) -> None:
        ''' Нажать на кнопку "Finish" '''
        self.click_to_element(CheckoutPageLocators.CHECKOUT_FINISH_BUTTON)

    def fill_person_data_fields(self) -> None:
        ''' Заполнить поля страницы данными покупателя и нажать кнопку 'Continue' '''
        self.write_to_element(CheckoutPageLocators.CHECKOUT_FIRST_NAME, PersonData.FIRST_NAME)
        self.write_to_element(CheckoutPageLocators.CHECKOUT_LAST_NAME, PersonData.LAST_NAME)
        self.write_to_element(CheckoutPageLocators.CHECKOUT_POSTAL_CODE, PersonData.POSTAL_CODE)
        self.click_continue_button()

    def go_checkout(self, cart_data: dict[str, float]) -> None:
        '''
        Оформление заказа

        вызвать функцию заполения данными покупателя,
        проверить точность заказа:
        - проверяется совпадение названий товаров, которые ложили в корзину и их цены
        - проверяется точно подсчёта суммы заказа
        нажать кнопку Finish

        :param cart_data: словарь, хранящий полное название продукта (str) и его цену (float)
        '''
        self.fill_person_data_fields()
        for i, name in enumerate(cart_data.keys(), start=1):
            self.assert_cart_item_name(i, name)

        self.assert_cart_subtotal_price(sum(cart_data.values()))
        self.click_finish_button()
