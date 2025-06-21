from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.chekout_step_two_page import CheckoutTwoPage
from pages.checkout_complete_page import CheckoutCompletePage
from src.config.api_constants import EnvConfig


def test_checkout_order(browser):
    page = browser.new_page()
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    checking_details = CheckoutTwoPage(page)
    wait_complete_and_logout = CheckoutCompletePage(page)

    login_page.login(EnvConfig.USERNAME, EnvConfig.PASSWORD)
    inventory_page.add_first_item_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_form('John', 'Doe', '12345')
    checking_details.checking_order_details()
    wait_complete_and_logout.wait_complete_page()
    wait_complete_and_logout.logout_by_toolbar()
