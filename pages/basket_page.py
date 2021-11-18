from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_empty_basket()
        self.should_be_message_empty_basket()

    def should_be_basket_url(self):
        assert 'basket' in self.browser.current_url, "Not basket page"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_TITLE), "Basket is not empty"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_EMPTY_MESSAGE), "Not message about empty basket"