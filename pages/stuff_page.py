from .main_page import MainPage
from data.locators import StuffPageLocators


class StuffPage(MainPage):
    def assert_remove_from_cart_button(self) -> None:
        ''' Проверка наличия кнопки "Remove" '''
        assert self.is_element_present(StuffPageLocators.STUFF_REMOVE_FROM_CART_BUTTON),\
            "Remove-from-Cart button is not presented"

    def click_add_to_cart(self) -> None:
        ''' Нажать кнопку добавления товара в корзину '''
        self.click_to_element(StuffPageLocators.STUFF_ADD_TO_CART_BUTTON)

    def click_back_to_products(self) -> None:
        ''' Нажать кнопку возврата к списку продуктов '''
        self.click_to_element(StuffPageLocators.STUFF_BACK_TO_PRODUCTS_BUTTON)

    def get_name(self) -> str :
        ''' Получить текст (строка) из WebElement-а '''
        return self.get_element_text(StuffPageLocators.STUFF_NAME)

    def get_price(self) -> float:
        ''' Получить цену (вещественная величина) из WebElement-а '''
        price_s = self.get_element_text(StuffPageLocators.STUFF_PRICE)
        return float(price_s.replace('$', ''))
