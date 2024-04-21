from Utils.driver_manager import DriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
class BasePage:
    
    def  Open_url(self,url):
         self.driver.get(url)
    def find_element_(self,locator,ele):
         return self.driver.find_element(locator,ele)
    def find_elements_(self,locator,ele):
         return self.driver.find_elements(locator,ele)
    def click_element(self,ele):
         
         ele.click()
         self.alert()
    def text_enter(self,ele,data):
         ele1=self.find_element_(ele)
         ele1.send_keys(data)
    def alert(self):
         a1=Alert(self.driver)
         a1.dismiss
    def is_element_displayed(self, by, value):
        try:
            element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located((by, value)))
            return element.is_displayed()
        except:
            return False
    def frame(self):
      
    # Check for the presence of the ad iframe
     try:
        ad_frame = self.driver.find_element(By.XPATH, "//iframe[@id='ad_frame']")
        # Switch to the ad frame
        self.driver.switch_to.frame(ad_frame)

        # Find and interact with the close button (assuming it's an element within the iframe)
        close_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((By.LINK_TEXT, "Close")))
        close_button.click()  # Click to close the ad frame

        # Switch back to the default content (outside the iframe)
        self.driver.switch_to.default_content()

     except NoSuchElementException:
        # If ad frame is not found, continue with other actions
        print("")