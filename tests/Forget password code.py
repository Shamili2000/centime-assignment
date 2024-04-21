
from selenium import webdriver
from selenium.webdriver.common.by import By

driver =webdriver.Chrome()
driver.get("https://practice.automationtesting.in/my-account/")
driver.find_element(By.ID,"username").send_keys("johnpete@gmail.com")
driver.find_element(By.ID,"password").send_keys("JOHN@@123")
driver.find_element(By.ID,"rememberme").click()
driver.find_element(By.NAME,"login").click()
driver.find_element(By.LINK_TEXT,"Lost your password?").click()
driver.find_element(By.ID,"user_login").send_keys("johnpete@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[type='submit']").click()

