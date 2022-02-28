from selenium.webdriver.common.by import By

from page_objects.CataloguePage import CataloguePage


class LoginPage:

    user_name = [By.CSS_SELECTOR, "#user-name"]
    password = [By.CSS_SELECTOR, "#password"]
    submit = [By.CSS_SELECTOR, "#login-button"]

    def __init__(self, driver):
        self.driver = driver

    def get_user_name(self):
        return self.driver.find_element(*LoginPage.user_name)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def submit_login_data(self):
        self.driver.find_element(*LoginPage.submit).click()
        catalogue_page = CataloguePage(self.driver)
        return catalogue_page
