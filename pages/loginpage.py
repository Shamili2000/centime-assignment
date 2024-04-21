from .basepage import BasePage
from .basepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
class LoginPage(BasePage):
    driver=None
    def __init__(self,driver):
        
        self.driver=driver
    def Myaccount(self):
        ele=self.find_element_(By.LINK_TEXT,"My Account")
        self.click_element(ele)
    def Enter_username(self,name):
        ele=self.find_element_(By.NAME,"username")
        ele.send_keys(name)
    def Enter_password(self,password):
         ele=self.find_element_(By.NAME,"password")
         ele.send_keys(password)
    def Login_button(self):
         ele=self.find_element_(By.NAME,"login")
         self.click_element(ele)
    def Logout_button(self):#not implemented
         ele=self.find_element_(By.NAME,"logout")
         self.click_element(ele)
    def back_button(self):
        pass
    def get_current_url(self):
         
         return self.driver.current_url
    
    def message(self):
        return self.find_element_(By.XPATH,"//*[@id='page-36']/div/div[1]/ul/li").text
        