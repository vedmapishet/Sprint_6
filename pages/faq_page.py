import allure

from pages.base_page import BasePage
from locators import FaqLocators


class FaqPage(BasePage):

    @allure.step(" Проверка текста при клике на вопрос о важном")
    def check_the_questions(self, number):
        questions_formated = self.format_locators(FaqLocators.questions, number)
        panel_locator_formated = self.format_locators(FaqLocators.panel_locator, number)

        self.find_element_located_click(questions_formated)
        return self.find_element_located(panel_locator_formated).text