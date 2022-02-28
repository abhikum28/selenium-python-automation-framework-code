import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.LoginPage import LoginPage
from test_data.E2E_01_Data import E2E_01_Data
from utilities.BaseClass import BaseClass


class TestE2E_01(BaseClass):

    def test_E2E_01(self, data_set):
        log = self.get_log()
        self.driver.get("https://www.saucedemo.com/")
        login_page = LoginPage(self.driver)

        login_page.get_user_name().send_keys("standard_user")
        login_page.get_password().send_keys("secret_sauce")
        catalogue_page = login_page.submit_login_data()
        log.info("Login successful")
        products = catalogue_page.get_product_list()
        for product in products:
            product_name = product.find_element(By.CSS_SELECTOR, value=".inventory_item_name").text
            if product_name == data_set["prod_name"]:
                product.find_element(By.CSS_SELECTOR, value=".btn_primary").click()

        cart_page = catalogue_page.verify_cart("1")
        log.info(data_set["prod_name"]+" is added to cart")

        product_name = cart_page.get_product_name().text
        assert product_name == data_set["prod_name"]

        address_page = cart_page.confirm_checkout()

        address_page.get_first_name().send_keys(data_set["first_name"])
        address_page.get_last_name().send_keys(data_set["last_name"])
        address_page.get_postal_code().send_keys(data_set["post_code"])
        checkout_page = address_page.confirm_address()
        log.info("Address details of "+data_set["first_name"]+" "+data_set["last_name"]+" entered successfully")
        product_name = checkout_page.get_product_name().text
        assert product_name == data_set["prod_name"]

        confirmation_page = checkout_page.finish_shopping()

        success_mssg = confirmation_page.check_success_mssg().text
        assert "THANK YOU FOR YOUR ORDER" in success_mssg
        log.info(data_set["prod_name"]+" is bought successfully")
        confirmation_page.get_menu().click()
        self.wait_for_element_by_css(confirmation_page.logout_locator)
        confirmation_page.get_logout().click()

        assert login_page.get_user_name().is_displayed()
        log.debug("Return back to home page successfully after logout")

    @pytest.fixture(params=E2E_01_Data.shop_data)
    def data_set(self, request):
        return request.param
