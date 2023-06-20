from .base_page import BasePage
from .locators import ProductsPageLocators


class ProductsPage(BasePage):
    def click_to_product_backpack(self):
        self.browser.find_element(*ProductsPageLocators.PROD_BACKPACK).click()

    def click_to_product_tshirt(self):
        prod = self.browser.find_element(*ProductsPageLocators.PROD_TSHIRT)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", prod)
        prod.click()

    def should_be_product_backpack(self):
        assert self.is_element_present(*ProductsPageLocators.PROD_BACKPACK), "BackPack is not presented"

    def should_be_product_tshirt(self):
        assert self.is_element_present(*ProductsPageLocators.PROD_TSHIRT), "T-Shirt is not presented"
