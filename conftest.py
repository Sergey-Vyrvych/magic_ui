from selenium import webdriver
import pytest
from time import sleep
from pages.sale_page import SalePage
from pages.customer_login import CustomerLogin


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    sleep(3)
    return chrome_driver


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def login_page(driver):
    return CustomerLogin(driver)