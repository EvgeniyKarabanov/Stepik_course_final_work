import time
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import math


class ProductPage(BasePage):
    def should_add_to_cart(self):
        self.should_be_button_add_to_cart()
        add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART)
        add_to_basket.click()
        #self.solve_quiz_and_get_code()
        #self.should_be_message_add_to_basket()
        #self.should_be_add_this_book(self.find_element(*ProductPageLocators.NAME_BOOK))
        #self.should_be_add_true_price(self.find_element(*ProductPageLocators.PRICE_BOOK))
        #time.sleep(500)

    def should_be_button_add_to_cart(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CART), "Button 'add to basket' is not presented"

    def should_be_message_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADDED_TO_BASKET), "No message about added book"

    def should_be_add_this_book(self, name_book):
        assert name_book == self.browser.find_elements(*ProductPageLocators.MESSAGE_ADDED_TO_BASKET)[0].text, "Add wrong book"

    def should_be_add_true_price(self, price_book):
        assert price_book == self.browser.find_elements(*ProductPageLocators.MESSAGE_ADDED_TO_BASKET)[2].text, "Add wrong price book"

    def should_not_be_success_message_v2(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADDED_TO_BASKET), "Message is not disappeared"

    def should_not_be_success_message_v1(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADDED_TO_BASKET), \
           "Success message is presented, but should not be"