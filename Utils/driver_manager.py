from selenium import webdriver
class DriverManager:
    driver=None
    @classmethod
    def create_driver(cls,driver):
          if driver.lower()=='chrome':
               cls.driver=webdriver.Chrome()
          elif driver.lower()=='firefox':
               cls.driver=webdriver.Firefox()
          elif driver.lower()=='edge':
               cls.driver=webdriver.Edge()
          return cls.driver
   
    @classmethod
    def quit(cls):
        if cls.driver:
             cls.driver.quit()
