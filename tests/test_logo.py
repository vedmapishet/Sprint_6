import allure

from pages.logo_page import YaPage
from locators import UrlsLocators as Url
from locators import OrderLocators as Order


class TestLogo:
    @allure.title(' Проверка перехода на главную страницу "Самокат"')
    @allure.description('Нажимаем на логотип "Самокат" и проверяем , что произошёл переход главную страницу "Самоката"')
    def test_samokat_logo_link(self, driver):
        logo_page = YaPage(driver)
        logo_page.go_to_site(Url.url + Order.path)
        logo_page.transition_logo_scooter()
        current_url = logo_page.current_url()
        assert current_url == Url.url



    def test_yandex_logo_link(self, driver):
        logo_page = YaPage(driver)
        logo_page.go_to_site(Url.url)
        logo_page.transition_logo_yandex()
        logo_page.switch_dzen()
        current_url = logo_page.current_url()
        assert 'dzen.ru/' in current_url