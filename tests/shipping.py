# tests/test_login_and_view_addresses.py

import pytest
from selenium import webdriver
from pages.loginpage import LoginPage
from pages.MyAccount import MyAccountPage

from selenium.webdriver.common.by import By
import time 
@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_login_and_view_addresses(browser):
    login_page = LoginPage(browser) 
    login_page.Open_url("https://practice.automationtesting.in/")
    login_page.Myaccount()
    login_page.Enter_username("user1231@gmail.com")
    login_page.Enter_password("Admin132@2")
    login_page.Login_button()
    my_account_page = MyAccountPage(browser)
    my_account_page.goto_dashboard()
    my_account_page.goto_addresses()
    login_page.frame()
    # Assert that we are on the Addresses page
    browser.find_element(By.LINK_TEXT,"Edit").click()
    login_page.frame()
    time.sleep(2)
    ele1=browser.find_element(By.ID,"billing_first_name")
    ele1.clear()
    ele1.send_keys("sreekanth")
    ele2=browser.find_element(By.ID,"billing_last_name")
    ele2.clear()
    ele2.send_keys("sreekanth")
    ele3=browser.find_element(By.ID,"billing_phone")
    ele3.clear()
    ele3.send_keys("8775445328")
    ele4=browser.find_element(By.Id,"billing_address_1")
    ele4.clear()
    ele4.send_keys("shantinagar street")
    ele5=browser.find_element(By.Id,"billing_city")
    ele5.clear()
    ele5.send_keys("Hyderbad")
    ele6=browser.find_element(By.Id,"billing_postcode")
    ele6.clear()
    ele6.send_keys("500060")
    time.sleep(2)
    ele7=browser.find_element(By.NAME,"save_address")
    ele7.clear()
    ele7.click()
    time.sleep(1)
    assert browser.find_element(By.CLASS_NAME,"woocommerce-message").text =="Address changed successfully."