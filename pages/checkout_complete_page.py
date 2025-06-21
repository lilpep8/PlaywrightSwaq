from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    IMAGE_SELECTOR = 'img[alt="Pony Express"]'
    THANKS_FOR_ORDER_SELECTOR = '[data-test="complete-header"]'
    DISPATCH_MESSAGE_SELECTOR = '[data-test="complete-text"]'
    BUTTON_SELECTOR = '[data-test="back-to-products"]'
    BUTTON_TOOLBAR_SELECTOR = '#react-burger-menu-btn'
    BUTTON_LOGOUT_SELECTOR = '#logout_sidebar_link'


    def __init__(self, page):
        super().__init__(page)
        self._endpoint = 'checkout-complete.html'


    def wait_complete_page(self):
        self.assert_element_is_visible(self.THANKS_FOR_ORDER_SELECTOR)
        self.assert_element_is_visible(self.DISPATCH_MESSAGE_SELECTOR)
        self.assert_element_is_visible(self.BUTTON_SELECTOR)
        self.assert_element_is_visible(self.IMAGE_SELECTOR)


    def logout_by_toolbar(self):
        self.wait_for_selector_and_click(self.BUTTON_TOOLBAR_SELECTOR)
        self.wait_for_selector_and_click(self.BUTTON_LOGOUT_SELECTOR)
