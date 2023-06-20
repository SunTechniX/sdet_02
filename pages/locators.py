from selenium.webdriver.common.by import By


class AccountPageLocators():
    ACC_WELCOME_TEXT = (By.XPATH, "//strong[contains(text(),'Welcome')]")
    ACC_WELCOME_USER = (By.XPATH, "//strong[contains(text(),'Welcome')]/span")
    ACC_DEPOSIT_BTN = (By.XPATH, "//button[starts-with(text(),'Deposit')]")
    ACC_AMOUNT_FIELD = (By.XPATH, "//input[@ng-model='amount']")
    ACC_DEPOSIT_SUBMIT = (By.XPATH, "//button[@type='submit']")
    ACC_DEPOSIT_SUCCESS_MSG = (By.XPATH, "//span[@ng-show='message']")
    ACC_TRANSACT_BTN = (By.XPATH, "//button[@ng-click='transactions()']")

class BasePageLocators():
    CART_PIC_LINK = (By.CSS_SELECTOR, '.shopping_cart_link')
    LOGOUT_BTN = (By.XPATH, "//button[starts-with(text(),'Logout')]")
    #LOGOUT_BTN = (By.XPATH, "//button[@ng-click='byebye()']")
    #HOME_BTN = (By.XPATH, "//button[starts-with(text(),'Home')]")

class CartPageLocators():
    CART_PIC_LINK = (By.CSS_SELECTOR, '.shopping_cart_link')

class CheckoutPageLocators():
    CART_PIC_LINK = (By.CSS_SELECTOR, '.shopping_cart_link')

class LoginPageLocators():
    USERNAME_FIELD = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
    LOGIN_BTN = (By.CSS_SELECTOR, '#login-button')

class ProductsPageLocators():
    PROD_BACKPACK = (By.XPATH, "//div[@class='inventory_item_name'][contains(text(),'Backpack')]")
    PROD_TSHIRT = (By.XPATH, "//div[@class='inventory_item_name'][contains(text(),'T-Shirt')]")

class StuffPageLocators():
    #STUFF_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[name='add-to-cart-sauce-labs-backpack']")
    STUFF_ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    STUFF_BACK_TO_PRODUCTS_BUTTON = (By.CSS_SELECTOR, "button[name='back-to-products']")
    #STUFF_REMOVE_FROM_CART_BUTTON = (By.CSS_SELECTOR, "button[name='remove-sauce-labs-backpack']")
    STUFF_REMOVE_FROM_CART_BUTTON = (By.XPATH, "//button[contains(text(),'Remove')]")
    STUFF_PRICE = (By.CSS_SELECTOR, 'div.inventory_details_price')
