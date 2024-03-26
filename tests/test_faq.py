import pytest
import allure
from pages.faq_page import FaqPage
from data import TestData as Data
from locators import FaqLocators
from locators import UrlsLocators as Url


class TestFaq:
    @allure.title('Проверка  выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('На главной странице перейти к разделу "Вопросы о важном", нажать на вопрос и проверить текст ответа')
    @pytest.mark.parametrize(
            'number, answer',
            [
                Data.faq_0,
                Data.faq_1,
                Data.faq_2,
                Data.faq_3,
                Data.faq_4,
                Data.faq_5,
                Data.faq_6,
                Data.faq_7
            ]
        )
    def test_check_answer_text(self, driver, number, answer):
        faq_page = FaqPage(driver)
        faq_page.go_to_site(Url.url)
        faq_page.scrolldown(FaqLocators.questions_section_head)

        assert faq_page.check_the_questions(number) == answer