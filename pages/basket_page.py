from .base_page import BasePage
from .locators import BasePageLocators
from .locators import ProductPageLocators
import pytest

class BasketPage(BasePage):

    def should_basket_be_empty(self):
        try:
            basket_empty = self.browser.find_element(*BasePageLocators.BASKET_EMPTY)
        except (NoSuchElementException):
            return False
        return True

    def should_see_product_in_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME) 
        alert_message_product = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE_PRODUCT)
        assert product_name.text == alert_message_product.text, "There is no such product in your basket"

    def should_see_correct_basket_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        alert_message_price = self.browser.find_element(*ProductPageLocators.ALERT_MESSAGE_PRICE) 
        assert product_price.text == alert_message_price.text, "Your basket price is not what expected"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_success_message_dissappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def go_to_basket_page(self):
        basket_link = self.browser.find_element(*BasePageLocators.BASKET_LINK)
        basket_link.click()
