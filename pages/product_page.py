from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_promo_in_url()
        self.should_be_add_to_basket_button()
    def should_be_promo_in_url(self):
        product_url = self.browser.current_url
        if 'promo' in product_url:
            assert True, "There is no substring 'promo' on current page url"
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "There is no add to basket button on this page"



    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

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




