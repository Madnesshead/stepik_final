from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert '/basket/' in self.browser.current_url, 'Current page is not basket page'

    def should_not_have_items(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BUY), \
            "Items to buy is presented when basket must be empty"

    def should_have_message_if_empty(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text == \
            'Your basket is empty. Continue shopping', "Empty basket message is not presented"
