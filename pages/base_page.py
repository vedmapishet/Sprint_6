from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import OrderLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        return self.driver.get(url)

    def scrolldown(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_locators(self, locators, number):
        locator = locators.format(number)
        loc = [By.ID, locator]
        return loc


    def find_element_located_click(self, locator):
        return WebDriverWait(self.driver, 10)\
            .until(EC.visibility_of_element_located(locator)).click()

    def find_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def find_elements_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    def current_url(self):
        return self.driver.current_url

    def find_element_located_input(self, locator, text):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)).send_keys(text)


    def apply_cookies(self):
        return self.find_element_located_click(OrderLocators.accept_cookies_button)

    def switch_window(self, locator, number):
        self.driver.switch_to.window(self.driver.window_handles[number])
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(locator))