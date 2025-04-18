from selenium import webdriver
import pytest
from time import sleep
from pages.sale_page import SalePage
from pages.customer_login import CustomerLogin
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    chrome_driver = webdriver.Chrome(options=options)
    # sleep(3)
    return chrome_driver


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)