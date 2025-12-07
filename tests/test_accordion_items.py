import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPageScooter
from const import ACCORDION_DATA, BASE_URL

class TestAccordion:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
    
    @pytest.mark.parametrize("button_id, expected_text", ACCORDION_DATA)
    def test_text_in_accordion(self, button_id, expected_text):
        self.driver.get(BASE_URL)
        main_page = MainPageScooter(self.driver)
        main_page.waiting_page_upload()
        main_page.scroll_to_the_end_of_page()
        main_page.click_to_cookie_close_button()
        button = getattr(main_page, f'accordion_button_{button_id}')
        panel = getattr(main_page, f'accordion_panel_{button_id}')
        main_page.click_to_accordion_button(button)
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(panel)
        )
    
        assert self.driver.find_element(*panel).get_attribute('hidden') != 'true'
        assert main_page.get_text_in_accordion(panel) == expected_text
    
    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 
    