from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/', \
            'Current page is not login page'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), \
            "Login email field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWD), \
            "Login password field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORGOTTEN), \
            "Login forgotten password link is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), \
            "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTR_EMAIL), \
            "Registration email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTR_PASSWD), \
            "Registration password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTR_CONFIRM), \
            "Password confirmation field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTR_BUTTON), \
            "Register button is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTR_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTR_PASSWD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTR_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTR_BUTTON).click()
