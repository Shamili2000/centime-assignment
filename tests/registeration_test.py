
from pages.RegistrationPage import Registerpage
from Utils import driver_manager
# tests/test_login_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import time
from selenium.webdriver.common.by import By


@pytest.fixture
def setup_driver():
    driver = driver_manager.DriverManager.create_driver("chrome")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_valid_registration(setup_driver):
    register_page =Registerpage(setup_driver)
    register_page .Open_url("https://practice.automationtesting.in/")
    register_page .Myaccount()
    register_page .Enter_username("user1231@gmail.com")
    register_page .Enter_password("Admin132@2")
    register_page.register_button()
    assert setup_driver.find_element(By.LINK_TEXT,"Dashboard").text=="Dashboard"
   

def test_invalidemail_registration(setup_driver):
    register_page =Registerpage(setup_driver)
    register_page .Open_url("https://practice.automationtesting.in/")
    register_page .Myaccount()
    register_page .Enter_username("user131@jhon.com")
    register_page .Enter_password("Admin132@2")
    register_page.register_button()
    time.sleep(10)
    assert register_page.message() == "Error: Please provide a valid email address."

def test_empty_email_registration(setup_driver):
    register_page =Registerpage(setup_driver)
    register_page .Open_url("https://practice.automationtesting.in/")
    register_page .Myaccount()
    register_page .Enter_username("")
    register_page .Enter_password("Admin132@2")
    register_page.register_button()
    
    
    time.sleep(10)
    # Assertion or further actions on the new page
    assert register_page.message() == "Error: Please provide a valid email address."

  

def test_empty_password_registration(setup_driver):
    register_page =Registerpage(setup_driver)
    register_page .Open_url("https://practice.automationtesting.in/")
    register_page .Myaccount()
    register_page .Enter_username("user231@gmail.com")
    register_page .Enter_password("")
    register_page.register_button()
    
    time.sleep(10)
    assert register_page.message() == "Error: Please enter an account password."
   
def test_empty_email_and_password_registration(setup_driver):
    register_page =Registerpage(setup_driver)
    register_page .Open_url("https://practice.automationtesting.in/")
    register_page .Myaccount()
    register_page .Enter_username("")
    register_page .Enter_password("")
    register_page.register_button()
    
    assert register_page.message() == "Error: Please provide a valid email address."
   