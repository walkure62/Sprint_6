import random
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def wait_and_find_elements(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)
    
    def scroll_to_the_end_of_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    def click_to_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()
        
    def click_to_element_with_script(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
        
    def get_element_locator_by_id(self, locators, name, id):
        element = getattr(locators, f'{name}_{id}')
        return element
        
    def get_text_from_element(self, locator):
        element = self.wait_and_find_element(locator)
        return element.text
    
    def send_keys_to_element(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.send_keys(text)
        
    def select_random_element_in_multiple_menu(self, locator):
        elements = self.wait_and_find_elements(locator)
        elements[random.randint(0, (len(elements) - 1))].click()
        
    def enter_to_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.send_keys(Keys.ENTER)
        
    def switch_to_new_tab(self):
        window_handles = self.driver.window_handles
        new_window_handle = window_handles[-1]
        self.driver.switch_to.window(new_window_handle)
        time.sleep(5)
        
    def get_current_url(self):
        return self.driver.current_url
        
    