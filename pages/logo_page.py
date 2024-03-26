import allure

from pages.base_page import BasePage
from locators import LogoLocators as Logo

class YaPage(BasePage):


    @allure.step(" Переход по логотипу Самокат")
    def transition_logo_scooter(self):
        self.find_element_located_click(Logo.samokat_logo)
        return self.driver.current_url

    @allure.step("Переход по логотипу Яндекс")
    def transition_logo_yandex(self):
        self.find_element_located_click(Logo.yandex_logo)

    @allure.step("Переход на вторую вкладку")
    def switch_dzen(self):
        self.switch_window(Logo.dzen_logo, 1)