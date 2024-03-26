import pytest
import allure

from pages.order_page import OrderPage
from locators import UrlsLocators as Url
from data import OrderTestData



class TestOrder:
    @allure.title('Заказ  самоката - вход через кнопку "Заказать" в шапке страницы- позитивный сценарий')
    @allure.description('Проверка позитивного сценария заказа самоката с корректным заполнением всех полей формы')
    @pytest.mark.parametrize('button, name, surname, address, station, phone, date, comment', OrderTestData.testDataSet)
    def test_order_via_button_in_header_correct_data(self, driver, button, name, surname, address, station, phone, date, comment):
        order_page = OrderPage(driver)
        order_page.go_to_site(Url.url)
        order_page.apply_cookies()
        order_page.click_order(button)
        order_page.data_entry_form_one(name, surname, address, station, phone)
        order_page.data_entry_form_two(date, comment)
        assert order_page.order_confirmation() == "Посмотреть статус"