import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class OrderPageScooter:
    root_element = [By.ID, "root"]
    cookie_close_button = [By.ID, 'rcc-confirm-button']
    first_name_input = [By.XPATH, "//input[@placeholder='* Имя']"]
    second_name_input = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    adress_input = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    phone_input = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    metro_button = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    metro_item = [By.XPATH, "//button[@class='Order_SelectOption__82bhS select-search__option']"]
    next_button = [By.CLASS_NAME, "Button_Middle__1CSJM"]
    date_input = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    datepicker = [By.CLASS_NAME, "react-datepicker"]
    datepicker_day = [By.CLASS_NAME, "react-datepicker__day"]
    rental_period_button = [By.CLASS_NAME, "Dropdown-control"]
    rental_dropdown_menu = [By.CLASS_NAME, "Dropdown-menu"]
    rental_period_option = [By.XPATH, "//div[@class='Dropdown-root is-open']//div[@class='Dropdown-option']"]
    color_scooter_checkbox = [By.CLASS_NAME, 'Checkbox_Input__14A2w']
    comment_input = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    order_button = [By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']"]
    order_modal = [By.CLASS_NAME, "Order_Modal__YZ-d3"]
    order_confirmation_button = [By.XPATH, "//button[text()='Да']"]
    order_modal_header = [By.CLASS_NAME, "Order_ModalHeader__3FDaJ"]
    check_status_button = [By.XPATH, "//button[text()='Посмотреть статус']"]
    logo_scooter = [By.XPATH, "//img[@alt='Scooter']"]
    logo_yandex = [By.XPATH, "//img[@alt='Yandex']"]
    
    def __init__(self, driver):
        self.driver = driver

    def waiting_page_upload(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "root")))
        
    def click_to_cookie_close_button(self):
        try:
            cookie_button = WebDriverWait(self.driver, 1).until(
                EC.element_to_be_clickable(self.cookie_close_button)
            )
            cookie_button.click()
        except TimeoutException:
            pass
        
    def enter_first_name(self, first_name):
        input = self.driver.find_element(*self.first_name_input)
        input.send_keys(first_name)
        
    def enter_second_name(self, second_name):
        input = self.driver.find_element(*self.second_name_input)
        input.send_keys(second_name)
        
    def enter_adress(self, adress):
        input = self.driver.find_element(*self.adress_input)
        input.send_keys(adress)
        
    def click_to_metro_button(self):
        button = self.driver.find_element(*self.metro_button)
        button.click()
        
    def select_metro(self):
        stations = self.driver.find_elements(*self.metro_item)
        stations[random.randint(1, len(stations))].click()
        
    def enter_phone(self, phone):
        input = self.driver.find_element(*self.phone_input)
        input.send_keys(phone)
    
    def click_to_next_button(self):
        self.driver.find_element(*self.next_button).click()
        
    def enter_date(self, date):
        date_input = self.driver.find_element(*self.date_input)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)
          
    def click_to_rental_period_button(self):
        button = self.driver.find_element(*self.rental_period_button)
        button.click()
        
    def select_rental_period(self):
        self.click_to_rental_period_button()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.rental_dropdown_menu)
        )
        periods = self.driver.find_elements(*self.rental_period_option)
        periods[random.randint(0, (len(periods) - 1))].click()
        
    def click_to_color_scooter_checkbox(self):
        checkboxs = self.driver.find_elements(*self.color_scooter_checkbox)
        checkboxs[random.randint(0, (len(checkboxs) - 1))].click()
        
    def enter_comment(self, comment):
        input = self.driver.find_element(*self.comment_input)
        input.send_keys(comment)
        
    def click_to_order_button(self):
        self.driver.find_element(*self.order_button).click()
        
    def click_to_order_confirmation_button(self):
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located(self.order_modal)
        )
        self.driver.find_element(*self.order_confirmation_button).click()
        
    def fill_order_form(self, user, date, comment):
        self.waiting_page_upload()
        self.click_to_cookie_close_button()
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
        
    def click_to_check_status_button(self):
        self.driver.find_element(*self.check_status_button).click()
        
    def click_to_logo_scooter(self):
        self.driver.find_element(*self.logo_scooter).click()
        
    def click_to_logo_yandex(self):
        self.driver.find_element(*self.logo_yandex).click()
    
        

    
