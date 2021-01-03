from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.XPATH, "//span/a")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASSWD = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_FORGOTTEN = (By.CSS_SELECTOR, 'form#login_form a')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')

    REGISTR_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTR_PASSWD = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTR_CONFIRM = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTR_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div#content_inner h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div#content_inner p.price_color')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    FIRST_ALERT = (By.CSS_SELECTOR, 'div.alert:nth-child(1)')
    BOOK_NAME_IN_ALERT = (By.XPATH, '//div[contains(@class, "alertinner")]/strong')
    BOOK_PRICE_IN_ALERT = (By.XPATH, '//div[contains(@class, "alertinner")]/p/strong')
    THIRD_ALERT = (By.CSS_SELECTOR, 'div.alert:nth-child(3)')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert:nth-child(1)')


class BasketPageLocators:
    ITEMS_TO_BUY = (By.XPATH, '//div[contains(@class, "row")]/h2')
    EMPTY_BASKET_MESSAGE = (By.XPATH, '//div[contains(@id, "content_inner")]/p')
    EMPTY_BASKET_LINK = (By.XPATH, '//div[contains(@id, "content_inner")]/p/a')

