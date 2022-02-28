from selenium.webdriver.common.by import By

from page_objects.ConfirmationPage import ConfirmationPage


class CheckoutPage:

    product_name = [By.CSS_SELECTOR, ".inventory_item_name"]
    finish_btn = [By.CSS_SELECTOR, "#finish"]

    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self):
        return self.driver.find_element(*CheckoutPage.product_name)

    def finish_shopping(self):
        self.driver.find_element(*CheckoutPage.finish_btn).click()
        confirmation_page = ConfirmationPage(self.driver)
        return confirmation_page
