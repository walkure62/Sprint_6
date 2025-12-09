import allure
import pytest
from data import Urls
from pages.main_page import MainPageScooter
from pages.order_page import OrderPageScooter
from locators.main_page_locators import MainPageLocators

class TestOrderScooter:
    
    @pytest.mark.parametrize("element", 
                             [(MainPageLocators.TOP_ORDER_BUTTON),
                             (MainPageLocators.MIDDLE_ORDER_BUTTON),
                             ])    
    def test_order_scooter_success(self, driver, element, user, date, comment):
        allure.dynamic.description(f"Заполнение формы валидными данными и успешное оформление заказа через {element}")
        main_page = MainPageScooter(driver)
        order_page = OrderPageScooter(driver)
    
        main_page.click_to_cookie_close_button()
        main_page.click_to_order_button(element)
        order_page.fill_order_form(user, date, comment)
        
        assert 'Заказ оформлен' in order_page.get_text_from_order_modal()
    
    @allure.description("Переход на главную страницу по клику на логотип сервиса Самокат")    
    def test_click_to_logo_scooter_success(self, driver):
        order_page = OrderPageScooter(driver)
        order_page.click_to_logo_scooter()
        assert Urls.BASE_URL in order_page.get_current_url()
    
    @allure.description("Переход на главную страницу https://dzen.ru по клику на логотип сервиса Yandex")    
    def test_click_to_logo_yandex_success(self, driver):
        order_page = OrderPageScooter(driver)
        order_page.click_to_logo_yandex()
        order_page.switch_to_new_tab()
        assert Urls.DZEN_URL in order_page.get_current_url()
        

    