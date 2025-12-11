import time
import allure
from selenium.common.exceptions import TimeoutException
from data import AccordionData
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPageScooter(BasePage):
    
    @allure.step("Клик по пункту {button_id} из списка вопросов")   
    def click_to_accordion_buttons(self, button_id):
        button = self.get_element_locator_by_id(MainPageLocators, AccordionData.ACCORDION_ELEMENTS['button'], button_id)
        self.click_to_element_with_script(button)
    
    @allure.step("Получаем текст ответа {button_id} из списка вопросов")    
    def get_text_in_accordion(self, button_id):
        panel = self.get_element_locator_by_id(MainPageLocators, AccordionData.ACCORDION_ELEMENTS['panel'], button_id)
        self.wait_and_find_element(panel)
        time.sleep(5)
        return self.get_text_from_element(panel)
    
    @allure.step("Кликаем по кнопке 'Заказать")      
    def click_to_order_button(self, element):
        self.click_to_element(element)
    
    @allure.step("Кликаем по кнопке согласия на передачу cookie")    
    def click_to_cookie_close_button(self):
        try:
            self.click_to_element(MainPageLocators.COOKIE_CLOSE_BUTTON)
        except TimeoutException:
            pass
        

    
