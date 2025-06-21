from pages.base_page import BasePage


class CheckoutTwoPage(BasePage):
    PRODUCT_NAME_SELECTOR = '[data-test="inventory-item-name"]'
    DESCRIPTION_ABOUT_PRODUCT_SELECTOR = '[data-test="inventory-item-desc"]'
    QUANTITY_OF_PRODUCTS_SELECTOR = '[data-test="item-quantity"]'
    PAYMENT_INFORMATION_SELECTOR = '[data-test="payment-info-value"]'
    SHIPPING_INFORMATION_SELECTOR = '[data-test="shipping-info-value"]'
    PRODUCT_TOTAL_PRICE_SELECTOR = '[data-test="total-label"]'
    BUTTON_CANCEL_SELECTOR = '#cancel'
    BUTTON_FINISH_SELECTOR = '#finish'


    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-step-two.html'


    def checking_order_details(self):
        self.assert_text_in_element(self.PRODUCT_NAME_SELECTOR,'Sauce Labs Backpack')
        self.assert_text_in_element(self.DESCRIPTION_ABOUT_PRODUCT_SELECTOR,'carry.allTheThings() with the sleek,'
                                                                            ' streamlined Sly Pack that melds '
                                                                            'uncompromising style with unequaled '
                                                                            'laptop and tablet protection.')
        self.assert_text_in_element(self.QUANTITY_OF_PRODUCTS_SELECTOR, '1')
        self.assert_text_in_element(self.PAYMENT_INFORMATION_SELECTOR, 'SauceCard #31337')
        self.assert_text_in_element(self.SHIPPING_INFORMATION_SELECTOR, 'Free Pony Express Delivery!')
        self.assert_text_in_element(self.PRODUCT_TOTAL_PRICE_SELECTOR, 'Total: $32.39')
        self.assert_element_is_visible(self.BUTTON_CANCEL_SELECTOR)
        self.wait_for_selector_and_click(self.BUTTON_FINISH_SELECTOR)

