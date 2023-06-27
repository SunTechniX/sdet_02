from .main_page import MainPage
from .locators import ProductsPageLocators


class ProductsPage(MainPage):
    def click_to_product(self, name):
        prod = self.get_element(ProductsPageLocators.product_name(name))
        self.run_script(ProductsPageLocators.PROD_FOCUS_SCRIPT, prod)
        prod.click()

    def present_product(self, name):
        assert self.is_element_present(ProductsPageLocators.product_name(name)), name + " is not presented"
