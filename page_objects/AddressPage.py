from selenium.webdriver.common.by import By

from page_objects.CheckoutPage import CheckoutPage


class AddressPage:

    first_name = [By.CSS_SELECTOR, "#first-name"]
    last_name = [By.CSS_SELECTOR, "#last-name"]
    postal_code = (By.CSS_SELECTOR, "#postal-code")
    continue_btn = [By.CSS_SELECTOR, "#continue"]

    def __init__(self, driver):
        self.driver = driver

    def get_first_name(self):
        return self.driver.find_element(*AddressPage.first_name)

    def get_last_name(self):
        return self.driver.find_element(*AddressPage.last_name)

    def get_postal_code(self):
        return self.driver.find_element(*AddressPage.postal_code)

    def confirm_address(self):
        self.driver.find_element(*AddressPage.continue_btn).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
