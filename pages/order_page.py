import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage

class OrderPageScooter(BasePage):
    
    @allure.step("Ввод имени в поле 'Имя'")    
    def enter_first_name(self, first_name):
        self.send_keys_to_element(OrderPageLocators.FIRST_NAME_INPUT, first_name)
    
    @allure.step("Ввод фамилии в поле 'Фамилия'")     
    def enter_second_name(self, second_name):
        self.send_keys_to_element(OrderPageLocators.SECOND_NAME_INPUT, second_name)
    
    @allure.step("Ввод адреса в поле 'Адрес'")     
    def enter_adress(self, adress):
       self.send_keys_to_element(OrderPageLocators.ADRESS_INPUT, adress)
    
    @allure.step("Клик по полю выбора станции метро для раскрытия селектора")     
    def click_to_metro_button(self):
        self.click_to_element(OrderPageLocators.METRO_BUTTON)
    
    @allure.step("Выбор станции метро в селекторе")    
    def select_metro(self):
        self.select_random_element_in_multiple_menu(OrderPageLocators.METRO_ITEM)
    
    @allure.step("Ввод номера телефона в поле 'Телефон'")    
    def enter_phone(self, phone):
        self.send_keys_to_element(OrderPageLocators.PHONE_INPUT, phone)
    
    @allure.step("Клик по кнопке 'Далее' для перехода к следующему шагу")
    def click_to_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
    
    @allure.step("Ввод даты в поле выбора даты")     
    def enter_date(self, date):
        self.send_keys_to_element(OrderPageLocators.DATE_INPUT, date)
        self.enter_to_element(OrderPageLocators.DATE_INPUT)
    
    @allure.step("Клик по полю выбора периода аренды для раскрытия селектора")      
    def click_to_rental_period_button(self):
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_BUTTON)
    
    @allure.step("Выбор периода аренды в селекторе")    
    def select_rental_period(self):
        self.click_to_rental_period_button()
        self.wait_and_find_element(OrderPageLocators.RENTAL_DROPDOWN_MENU)
        self.select_random_element_in_multiple_menu(OrderPageLocators.RENTAL_PERIOD_OPTION)
    
    @allure.step("Выбор цвета самоката через клик по чекбоксу")    
    def click_to_color_scooter_checkbox(self):
        self.select_random_element_in_multiple_menu(OrderPageLocators.COLOR_SCOOTER_CHECKBOX)
    
    @allure.step("Ввод номера телефона в поле 'Комментарий'")    
    def enter_comment(self, comment):
        self.send_keys_to_element(OrderPageLocators.COMMENT_INPUT, comment)
    
    @allure.step("Клик по кнопке 'Заказать'")    
    def click_to_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)
    
    @allure.step("Клик по кнопке 'Да' для подтверждения заказа")     
    def click_to_order_confirmation_button(self):
        self.click_to_element(OrderPageLocators.ORDER_CONFIRMATION_BUTTON)
    
    @allure.step("Заполняем форму заказа валидными данными")    
    def fill_order_form(self, user, date, comment):
        self.enter_first_name(user["first_name"])
        self.enter_second_name(user["second_name"])
        self.enter_adress(user["adress"])
        self.click_to_metro_button()
        self.select_metro()
        self.enter_phone(user["phone"])
        self.click_to_next_button()
        self.enter_date(date)
        self.select_rental_period()
        self.click_to_color_scooter_checkbox()
        self.enter_comment(comment)
        self.click_to_order_button()
        self.click_to_order_confirmation_button()
    
    @allure.step("Получаем текст из модального окна об успешном заказе")     
    def get_text_from_order_modal(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_MODAL_HEADER)
    
    @allure.step("Кликаем по кнопке для проверки статуса созданного заказа")    
    def click_to_check_status_button(self):
        self.click_to_element(OrderPageLocators.CHECK_STATUS_BUTTON)
    
    @allure.step("Клик по логотипу сервиса 'Самокат'")    
    def click_to_logo_scooter(self):
        self.click_to_element(OrderPageLocators.LOGO_SCOOTER)
    
    @allure.step("Клик по логотипу сервиса 'DZEN'")     
    def click_to_logo_yandex(self):
        self.click_to_element(OrderPageLocators.LOGO_YANDEX)
    
        

    
