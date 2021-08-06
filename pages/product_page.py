from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_promo_in_url()
        self.should_be_add_to_basket_button()

    def should_be_promo_in_url(self):
        product_url = self.browser.current_url
        if '?promo=newYear' in product_url:
            assert True, "There is no substring '?promo=newYear' on current page url"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "There is no add to basket button on this page"

    def add_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        link.click()

    def should_see_product_in_basket(self):
        alert_message = self.browser.find_element(By.CSS_SELECTOR, "div.alert-success .alertinner")
        assert  "The shellcoder's handbook" in alert_message.text, "There is no such product in your basket"

    def should_see_correct_basket_price(self):
        alert_message = self.browser.find_element(By.CSS_SELECTOR, "div.alert:last-child")
        assert "9,99 £" in alert_message.text, "Your basket price is not what expected"