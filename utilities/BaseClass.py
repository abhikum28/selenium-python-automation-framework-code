import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def wait_for_element_by_css(self, locator):
        web_driver_wait = WebDriverWait(self.driver, 5)
        web_driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))

    def get_log(self):

        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")

        file_handler = logging.FileHandler("logs.log")
        file_handler.setFormatter(formatter)

        if logger.hasHandlers():
            logger.handlers.clear()

        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)

        return logger
