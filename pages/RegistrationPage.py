from .basepage import BasePage
from .basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

class Registerpage(BasePage):
    def __init__(self,driver):
        
        self.driver=driver
    def Myaccount(self):
        ele=self.find_element_(By.LINK_TEXT,"My Account")
        self.click_element(ele)
    def Enter_username(self,name):
        ele=self.find_element_(By.ID,"reg_email")
        ele.send_keys(name)
    def Enter_password(self,password):
         ele=self.find_element_(By.ID,"reg_password")
         ele.send_keys(password)
    def register_button(self):
         ele=self.find_element_(By.NAME,"register")
         self.click_element(ele)
    def get_current_url(self):
         
         return self.driver.current_url
    def message(self):
        return self.find_element_(By.XPATH,"//*[@id='page-36']/div/div[1]/ul/li").text