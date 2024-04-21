
from pages.loginpage import LoginPage
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

def test_valid_login(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.Open_url("https://practice.automationtesting.in/")
    login_page.Myaccount()
    login_page.Enter_username("user1231@gmail.com")
    login_page.Enter_password("Admin132@2")
    login_page.Login_button()
   
    assert setup_driver.find_element(By.LINK_TEXT,"Dashboard").text=="Dashboard" 

    
def test_empty_password_login(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.Open_url("https://practice.automationtesting.in/")
    login_page.Myaccount()
    login_page.Enter_username("user")
    login_page.Enter_password("")
    login_page.Login_button()
   
    assert login_page.message() == "Error: Password is required."
    

def test_invalidusername_and_password_login(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.Open_url("https://practice.automationtesting.in/")
    login_page.Myaccount()
    login_page.Enter_username("user")
    login_page.Enter_password("1234")
    login_page.Login_button()
    
    assert login_page.message() == "Error: The password you entered for the username user is incorrect. Lost your password?"
def test_empty_username_login(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.Open_url("https://practice.automationtesting.in/")
    login_page.Myaccount()
    login_page.Enter_username("")
    login_page.Enter_password("Admin132@2")
    login_page.Login_button()
    assert login_page.message() == "Error: Username is required."
    
def test_empty_username_password_login(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.Open_url("https://practice.automationtesting.in/")
    login_page.Myaccount()
    login_page.Enter_username("")
    login_page.Enter_password("")
    login_page.Login_button()
    
    assert login_page.message() == "Error: Username is required."
def password__login(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.Open_url("https://practice.automationtesting.in/")
    login_page.Myaccount()
    login_page.Enter_username("user")
    login_page.Enter_password("hello")
    
    password_input=setup_driver.find_Element(By.ID,"password")
    # Verify the displayed value in the password field is masked (asterisks or bullets)
    actual_masked_password = password_input.get_attribute('value')
    expected_masked_password = '*' * 5  # Generate expected masked string
    assert actual_masked_password == expected_masked_password,f"Password input field does not display masked characters as expected. Actual: {actual_masked_password}"

    
def test_changedcase2_login(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.Open_url("https://practice.automationtesting.in/")
    login_page.Myaccount()
    login_page.Enter_username("USER132@2")
    login_page.Enter_password("aDMIN132@2")
    login_page.Login_button()
    
    assert setup_driver.find_element(By.LINK_TEXT,"Dashboard").text=="Dashboard" 
    #assert login_page.get_current_url() == "https://example.com/dashboard"
def test_chagedcase_login(setup_driver):
    login_page = LoginPage(setup_driver)
    login_page.Open_url("https://practice.automationtesting.in/")
    login_page.Myaccount()
    login_page.Enter_username("USER132@2")
    login_page.Enter_password("aDMIN132@2")
    login_page.Login_button()
    
    assert setup_driver.find_element(By.LINK_TEXT,"Dashboard").text=="Dashboard" 
      