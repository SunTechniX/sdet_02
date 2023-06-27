from selenium.webdriver.common.by import By


class AccountPageLocators:
    ACC_WELCOME_TEXT = (By.XPATH, "//strong[contains(text(),'Welcome')]")
    ACC_WELCOME_USER = (By.XPATH, "//strong[contains(text(),'Welcome')]/span")
    ACC_DEPOSIT_BTN = (By.XPATH, "//button[starts-with(text(),'Deposit')]")
    ACC_AMOUNT_FIELD = (By.XPATH, "//input[@ng-model='amount']")
    ACC_DEPOSIT_SUBMIT = (By.XPATH, "//button[@type='submit']")
    ACC_DEPOSIT_SUCCESS_MSG = (By.XPATH, "//span[@ng-show='message']")
    ACC_TRANSACT_BTN = (By.XPATH, "//button[@ng-click='transactions()']")


class CartPageLocators:
    @staticmethod
    def cart_item(num, field):
        return By.XPATH, f"//div[@class='cart_item'][{num}]//div[@class='inventory_item_{field}']"

    CART_CHECKOUT_BUTTON = (By.CSS_SELECTOR, '#checkout')


class CheckoutPageLocators:
    CHECKOUT_FIRST_NAME = (By.CSS_SELECTOR, '#first-name')
    CHECKOUT_LAST_NAME = (By.CSS_SELECTOR, '#last-name')
    CHECKOUT_POSTAL_CODE = (By.CSS_SELECTOR, '#postal-code')
    CHECKOUT_CONTINUE_BUTTON = (By.CSS_SELECTOR, '#continue')
    CHECKOUT_SUBTOTAL_PRICE = (By.CSS_SELECTOR, '.summary_subtotal_label')
    CHECKOUT_BACKPACK_NAME = (By.XPATH, "//div[@class='cart_item'][1]//div[@class='inventory_item_name']")
    CHECKOUT_TSHIRT_NAME = (By.XPATH, "//div[@class='cart_item'][2]//div[@class='inventory_item_name']")
    CHECKOUT_FINISH_BUTTON = (By.CSS_SELECTOR, '#finish')
    CHECKOUT_THANKS_MSG = (By.XPATH, "//h2[contains(text(),'Thank you for your order!')]")


class LoginPageLocators:
    USERNAME_FIELD = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
    LOGIN_BTN = (By.CSS_SELECTOR, '#login-button')


class MainPageLocators:
    CART_PIC_LINK = (By.CSS_SELECTOR, '.shopping_cart_link')
    LOGOUT_BTN = (By.XPATH, "//button[starts-with(text(),'Logout')]")


class ProductsPageLocators:
    @staticmethod
    def product_name(name):
        return By.XPATH, "//div[@class='inventory_item_name'][contains(text(),'" + name + "')]"

    PROD_FOCUS_SCRIPT = "return arguments[0].scrollIntoView(true);"


class StuffPageLocators:
    STUFF_NAME = (By.CSS_SELECTOR, ".inventory_details_name")
    STUFF_PRICE = (By.CSS_SELECTOR, '.inventory_details_price')
    STUFF_ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    STUFF_BACK_TO_PRODUCTS_BUTTON = (By.CSS_SELECTOR, "button[name='back-to-products']")
    STUFF_REMOVE_FROM_CART_BUTTON = (By.XPATH, "//button[contains(text(),'Remove')]")

