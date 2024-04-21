from .basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
class HomePage(BasePage):
    def __init__(self,driver):
       self.driver=driver
    def click_shop_menu(self):
        ele=self.find_element_(By.LINK_TEXT,"Shop")
        self.click_element(ele)
    def click_home_button(self):
        self.alert()
        ele=self.find_element_(By.LINK_TEXT,"Home")
        self.click_element(ele)
        
    def count_arrivals(self):
        self.frame()
        return len(self.find_elements_(By.CLASS_NAME, "woocommerce-LoopProduct-link"))

    def click_arrival_image(self, book_name):
        
        ele=self.find_element_(By.XPATH, book_name)
        self.click_element(ele)
    def is_book_in_basket(self):
        return self.is_element_displayed(By.CLASS_NAME, "product-name")
    def open_basket(self):
        ele=self.find_element_(By.XPATH, "//*[@id='wpmenucartli']/a")
        ele.click()
        self.alert()
    def add_to_basket(self,name):
        ele=self.find_element_(By.XPATH,name)
        ele.click()

    def button_add_to_basket(self):
        ele=self.find_element_(By.XPATH,"//button[@type='submit']")
        ele.click()

    
