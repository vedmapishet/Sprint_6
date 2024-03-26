import pytest
from selenium import webdriver

from locators import UrlsLocators as Url

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(Url.url)
    yield driver
    driver.quit()