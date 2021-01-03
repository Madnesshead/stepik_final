from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_url()
        self.add_product_to_basket()

    def should_be_product_url(self):
        assert 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/' in self.browser.current_url, \
            'Current page is not product page'

    def add_product_to_basket(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not presented"
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()
        self.solve_quiz_and_get_code()
        name_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_ALERT).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_ALERT).text
        assert name_in_basket == name, 'Wrong name for book added to basket'
        assert price_in_basket == price, 'Wrong price for book added to basket'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
