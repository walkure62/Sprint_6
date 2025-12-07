import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class MainPageScooter:
    top_order_button = [By.XPATH, "//div[@class='Header_Nav__AGCXC']//button[text()='Заказать']"]
    middle_order_button = [By.XPATH, "//div[@class='Home_FinishButton__1_cWm']//button[text()='Заказать']"]
    cookie_close_button = [By.ID, 'rcc-confirm-button']
    accordion_button_1 = [By.ID, 'accordion__heading-0']
    accordion_panel_1 = [By.XPATH, '//div[@id="accordion__panel-0"]/p']
    accordion_button_2 = [By.ID, 'accordion__heading-1']
    accordion_panel_2 = [By.XPATH, '//div[@id="accordion__panel-1"]/p']
    accordion_button_3 = [By.ID, 'accordion__heading-2']
    accordion_panel_3 = [By.XPATH, '//div[@id="accordion__panel-2"]/p']
    accordion_button_4 = [By.ID, 'accordion__heading-3']
    accordion_panel_4 = [By.XPATH, '//div[@id="accordion__panel-3"]/p']
    accordion_button_5 = [By.ID, 'accordion__heading-4']
    accordion_panel_5 = [By.XPATH, '//div[@id="accordion__panel-4"]/p']
    accordion_button_6 = [By.ID, 'accordion__heading-5']
    accordion_panel_6 = [By.XPATH, '//div[@id="accordion__panel-5"]/p']
    accordion_button_7 = [By.ID, 'accordion__heading-6']
    accordion_panel_7 = [By.XPATH, '//div[@id="accordion__panel-6"]/p']
    accordion_button_8 = [By.ID, 'accordion__heading-7']
    accordion_panel_8 = [By.XPATH, '//div[@id="accordion__panel-7"]/p']
    
    def __init__(self, driver):
        self.driver = driver

    def waiting_page_upload(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "root")))
        
    def scroll_to_the_end_of_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        
    def click_to_accordion_button(self, element):
        button = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].click();", button)
        
    def get_text_in_accordion(self, element):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(element))
        time.sleep(5)
        return self.driver.find_element(*element).text
        
    def click_to_order_button(self, element):
        self.driver.find_element(*element).click()
        
    def click_to_cookie_close_button(self):
        try:
            cookie_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.cookie_close_button)
            )
            cookie_button.click()
        except TimeoutException:
            pass
        

    
