import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPageScooter
from data import AccordionData

class TestAccordion:
    
    @pytest.mark.parametrize("button_id, expected_text", AccordionData.ACCORDION_DATA)
    @allure.step("Проверка пункта {button_id} из списка вопросов на главной странице")
    def test_text_in_accordion(self, driver, button_id, expected_text):
        allure.dynamic.description(f"Проверка пункта {button_id} из списка вопросов на главной странице на соответствие текста")
        main_page = MainPageScooter(driver)
        main_page.scroll_to_the_end_of_page()
        main_page.click_to_cookie_close_button()
        main_page.click_to_accordion_buttons(button_id)
    
        assert main_page.get_text_in_accordion(button_id) == expected_text
    
    