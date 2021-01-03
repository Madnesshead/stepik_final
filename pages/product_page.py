from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_url()
        self.add_product_to_basket()

    def should_be_product_url(self):
        assert self.browser.current_url == 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear', \
            'Current page is not product page'

    def add_product_to_basket(self):
        name = "The shellcoder's handbook"
        price = '£9.99'
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == name, 'Wrong book name'
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == price, 'Wrong book price'
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Add to basket button is not presented"
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()
        self.solve_quiz_and_get_code()
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_ALERT).text == name, \
            'Wrong name for book added to basket'
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_ALERT).text == price, \
            'Wrong price for book added to basket'
