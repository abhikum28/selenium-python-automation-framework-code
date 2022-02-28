from selenium.webdriver.common.by import By


class ConfirmationPage:

    success_mssg = [By.CSS_SELECTOR, ".complete-header"]
    menu = [By.CSS_SELECTOR, "#react-burger-menu-btn"]
    logout = [By.CSS_SELECTOR, "#logout_sidebar_link"]
    logout_locator = "#logout_sidebar_link"

    def __init__(self, driver):
        self.driver = driver

    def check_success_mssg(self):
        return self.driver.find_element(*ConfirmationPage.success_mssg)

    def get_menu(self):
        return self.driver.find_element(*ConfirmationPage.menu)

    def get_logout(self):
        return self.driver.find_element(*ConfirmationPage.logout)
