from selenium.webdriver.common.by import By

from page_objects.AddressPage import AddressPage


class CartPage:

    product_name = [By.CSS_SELECTOR, ".inventory_item_name"]
    checkout = [By.CSS_SELECTOR, "#checkout"]

    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self):
        return self.driver.find_element(*CartPage.product_name)

    def confirm_checkout(self):
        self.driver.find_element(*CartPage.checkout).click()
        address_page = AddressPage(self.driver)
        return address_page
