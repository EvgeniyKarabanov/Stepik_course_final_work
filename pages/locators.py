from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    BASKET_TITLE = (By.CSS_SELECTOR, ".basket-title")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    GUEST_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    GUEST_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    GUEST_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.NAME, "registration_submit")

class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alertinner strong")
    NAME_BOOK = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_BOOK = (By.CSS_SELECTOR, ".product_main .price_color")
