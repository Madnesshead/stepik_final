from selenium.webdriver.common.by import By


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
