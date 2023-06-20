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
    CART_BACKPACK_NAME = (By.XPATH, "//div[@class='cart_item'][1]/div[@class='cart_item_label']//div[@class='inventory_item_name']")
    #CART_BACKPACK_NAME = (By.CSS_SELECTOR, ".cart_list > .cart_item:nth-child(3) > .cart_item_label > a > .inventory_item_name")
    CART_BACKPACK_PRICE = (By.XPATH, "//div[@class='cart_item'][1]/div[@class='cart_item_label']//div[@class='inventory_item_price']")
    CART_TSHIRT_NAME = (By.XPATH, "//div[@class='cart_item'][2]/div[@class='cart_item_label']//div[@class='inventory_item_name']")
    #CART_TSHIRT_NAME = (By.CSS_SELECTOR, ".cart_list > .cart_item:nth-child(4) > .cart_item_label > a > .inventory_item_name")
    CART_TSHIRT_PRICE = (By.XPATH, "//div[@class='cart_item'][2]/div[@class='cart_item_label']//div[@class='inventory_item_price']")
    CART_CHECKOUT_BUTTON = (By.CSS_SELECTOR, '#checkout')

class CheckoutPageLocators():
    CHECKOUT_FIRST_NAME = (By.CSS_SELECTOR, '#first-name')
    CHECKOUT_LAST_NAME = (By.CSS_SELECTOR, '#last-name')
    CHECKOUT_POSTAL_CODE = (By.CSS_SELECTOR, '#postal-code')
    CHECKOUT_CONTINUE_BUTTON = (By.CSS_SELECTOR, '#continue')
    CHECKOUT_SUBTOTAL_PRICE = (By.CSS_SELECTOR, '.summary_subtotal_label')
    CHECKOUT_BACKPACK_NAME = (By.XPATH, "//div[@class='cart_item'][1]/div[@class='cart_item_label']//div[@class='inventory_item_name']")
    #CHECKOUT_BACKPACK_NAME = (By.CSS_SELECTOR, ".cart_list > .cart_item:nth-child(3) > .cart_item_label > a > .inventory_item_name")
    CHECKOUT_TSHIRT_NAME = (By.XPATH, "//div[@class='cart_item'][2]/div[@class='cart_item_label']//div[@class='inventory_item_name']")
    CHECKOUT_FINISH_BUTTON = (By.CSS_SELECTOR, '#finish')
    CHECKOUT_THANKS_MSG = (By.XPATH, "//h2[contains(text(),'Thank you for your order!')]")

class LoginPageLocators():
    USERNAME_FIELD = (By.CSS_SELECTOR, '#user-name')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
    LOGIN_BTN = (By.CSS_SELECTOR, '#login-button')

class ProductsPageLocators():
    PROD_BACKPACK = (By.XPATH, "//div[@class='inventory_item_name'][contains(text(),'Backpack')]")
    PROD_TSHIRT = (By.XPATH, "//div[@class='inventory_item_name'][contains(text(),'T-Shirt')]")

class StuffPageLocators():
    STUFF_NAME = (By.CSS_SELECTOR, ".inventory_details_name")
    STUFF_PRICE = (By.CSS_SELECTOR, '.inventory_details_price')
    #STUFF_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[name='add-to-cart-sauce-labs-backpack']")
    STUFF_ADD_TO_CART_BUTTON = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    STUFF_BACK_TO_PRODUCTS_BUTTON = (By.CSS_SELECTOR, "button[name='back-to-products']")
    #STUFF_REMOVE_FROM_CART_BUTTON = (By.CSS_SELECTOR, "button[name='remove-sauce-labs-backpack']")
    STUFF_REMOVE_FROM_CART_BUTTON = (By.XPATH, "//button[contains(text(),'Remove')]")
