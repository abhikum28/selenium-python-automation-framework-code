import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="option to choose browser type"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        s = Service("C:\\chromedriver.exe")
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        driver = webdriver.Chrome(options=chrome_options, service=s)
    elif browser_name == "firefox":
        s = Service("C:\\geckodriver.exe")
        driver = webdriver.Firefox(service=s)
        driver.maximize_window()
    elif browser_name == "edge":
        s = Service("C:\\msedgedriver.exe")
        driver = webdriver.Edge(service=s)
        driver.maximize_window()

    driver.implicitly_wait(3)
    request.cls.driver = driver
    yield
    driver.close()
