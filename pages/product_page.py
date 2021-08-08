from .base_page import BasePage
from .locators import ProductPageLocators


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




    




