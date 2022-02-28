from selenium.webdriver.common.by import By

from page_objects.CartPage import CartPage


class CataloguePage:

    product_list = [By.CSS_SELECTOR, ".inventory_item"]
    product_name = [By.CSS_SELECTOR, ".inventory_item_name"]
    add_to_cart = [By.CSS_SELECTOR, ".btn_primary"]
    cart = [By.CSS_SELECTOR, ".shopping_cart_badge"]

    def __init__(self, driver):
        self.driver = driver

    def get_product_list(self):
        return self.driver.find_elements(*CataloguePage.product_list)

    def get_product_name(self, parent):
        return parent.find_element(*CataloguePage.product_name)

    def get_add_to_cart(self, parent):
        return parent.find_element(*CataloguePage.add_to_cart)

    def verify_cart(self, count):
        cart_icon = self.driver.find_element(*CataloguePage.cart)
        assert cart_icon.text == count
        cart_icon.click()
        cart_page = CartPage(self.driver)
        return cart_page
