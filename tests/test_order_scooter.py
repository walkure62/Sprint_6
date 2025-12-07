import time
import pytest
from selenium import webdriver
from pages.main_page import MainPageScooter
from pages.order_page import OrderPageScooter
from const import BASE_URL

class TestOrderScooter:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        
    main_page = MainPageScooter(driver)
    
    @pytest.mark.parametrize("element", 
                             [(main_page.top_order_button),
                             (main_page.middle_order_button),
                             ])    
    def test_order_scooter_success(self, element, user, date, comment):
        self.driver.get(BASE_URL)
        main_page = MainPageScooter(self.driver)
        order_page = OrderPageScooter(self.driver)
        main_page.waiting_page_upload()
        main_page.click_to_cookie_close_button()
        main_page.click_to_order_button(element)
        order_page.fill_order_form(user, date, comment)
        
        assert len(self.driver.find_elements(*order_page.order_modal)) != 0
        assert 'Заказ оформлен' in self.driver.find_element(*order_page.order_modal_header).text
        
    def test_click_to_logo_scooter_success(self):
        self.driver.get(BASE_URL)
        order_page = OrderPageScooter(self.driver)
        order_page.click_to_logo_scooter()
        assert "https://qa-scooter.praktikum-services.ru/" in self.driver.current_url
        
    def test_click_to_logo_yandex_success(self):
        self.driver.get(BASE_URL)
        order_page = OrderPageScooter(self.driver)
        order_page.click_to_logo_yandex()
        window_handles = self.driver.window_handles
        new_window_handle = window_handles[-1]
        self.driver.switch_to.window(new_window_handle)
        time.sleep(5)
        assert "https://dzen.ru/" in self.driver.current_url
        
    
    @classmethod
    def teardown_class(cls):
        cls.driver.quit() 
    