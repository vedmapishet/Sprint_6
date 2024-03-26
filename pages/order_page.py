import allure
from pages.base_page import BasePage
from locators import OrderLocators


class OrderPage(BasePage):

    @allure.step("Ввод данных в первой форме + переход на вторую")
    def data_entry_form_one(self, name, surname, address, metro, phone):
        self.find_element_located(OrderLocators.name_input_field).send_keys(name)
        self.find_element_located_input(OrderLocators.family_name_input_field, surname)
        self.find_element_located_input(OrderLocators.address_input_field, address)
        self.find_element_located_input(OrderLocators.metro_station_input_field, metro)
        self.find_element_located_click(OrderLocators.name_metro)
        self.find_element_located_input(OrderLocators.phone_input_field, phone)
        self.find_element_located_click(OrderLocators.submit_button)

    @allure.step("Ввод данных во второй форме + подтверждение заказа")
    def data_entry_form_two(self, date_order, comment):
        self.find_element_located_input(OrderLocators.date_input_field, date_order)
        self.find_element_located_click(OrderLocators.grey_color_checkbox)
        self.find_element_located_click(OrderLocators.rent_duration_dropdown_options)
        self.find_element_located_click(OrderLocators.rent_day)
        self.find_element_located_input(OrderLocators.comment_input_field, comment)
        self.find_element_located_click(OrderLocators.order_button)
        self.find_element_located_click(OrderLocators.yes_button)


    @allure.step("Проверка всплывающего окна с сообщением об успешном создании заказа")
    def order_confirmation(self):
        return self.find_element_located(OrderLocators.order_status).text

    @allure.step(" Клик на кнопку Заказать")
    def click_order(self, button):
        self.find_element_located_click(button)