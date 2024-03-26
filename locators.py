from selenium.webdriver.common.by import By


class FaqLocators:
    questions_section_head = [By.XPATH, './/div[text()="Вопросы о важном"]']
    questions = 'accordion__heading-{}'
    panel_locator = 'accordion__panel-{}'

class OrderLocators:

    main_page_message_part = [By.XPATH, './/div[text() ="Привезём его прямо к вашей двери,"']
    accept_cookies_button = [By.XPATH, './/button[text()="да все привыкли"]']
    order_button_in_header = [By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text()="Заказать"]']
    order_button_in_lower_part = [By.XPATH, '//div[@class="Home_ThirdPart__LSTEE"]//button[text()="Заказать"]']
    path = 'order'
    form_heading = [By.XPATH, '//div[text()="Для кого самокат"]']
    name_input_field = [By.XPATH, './/input[@placeholder="* Имя"]']
    family_name_input_field = [By.XPATH, './/input[@placeholder="* Фамилия"]']
    address_input_field = [By.XPATH, './/input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_station_input_field = [By.XPATH, './/input[@placeholder="* Станция метро"]']
    name_metro = [By.XPATH, ".//li[@class='select-search__row']"]
    dropdown_metro_stations = [By.XPATH, '//div[@class="select-search__select"]/ul/li']
    metro_option = [By.XPATH, './/div[@class="select-search__select][1]']
    phone_input_field = [By.XPATH, './/input[@placeholder="* Телефон: на него позвонит курьер"]']
    submit_button = [By.XPATH, '//button[text()= "Далее"]']

    details_form_heading = [By.XPATH, '//div[text()="Про аренду"]']

    date_input_field = [By.XPATH, './/input[@placeholder="* Когда привезти самокат"]']
    rent_duration_dropdown_options = [By.XPATH, ".//div[text()='* Срок аренды']"]
    rent_day = [By.XPATH, ".//div[@class = 'Dropdown-menu']/div[text() = 'сутки']"]
    rent_duration_input_field = [By.XPATH, './/div[@class="Dropdown-root"]']
    black_color_checkbox = [By.ID, 'black']
    grey_color_checkbox = [By.XPATH, ".//input[@id='grey']"]
    comment_input_field = [By.XPATH, './/input[@placeholder="Комментарий для курьера"]']
    order_status = [By.XPATH, ".//*[text()='Посмотреть статус']"]
    order_button = [By.XPATH, ".//*[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    order_created_message = [By.XPATH, './/div[text()="Заказ оформлен"]']
    yes_button = [By.XPATH, './/button[text()="Да"]']


class UrlsLocators:
    url = 'https://qa-scooter.praktikum-services.ru/'
    ya_url = 'https://dzen.ru/?yredirect=true'
    order_url = "https://qa-scooter.praktikum-services.ru/order/"


class LogoLocators:
    dzen_logo = [By.CLASS_NAME, 'desktop-base-header__logoLink-aE']
    samokat_logo = [By.XPATH, './/img[@alt="Scooter"]']
    yandex_logo = [By.XPATH, './/img[@alt="Yandex"]']
