from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()  # Change the path to your ChromeDriver executable
driver.get("https://practice.automationtesting.in/")  # Replace "example.com" with the actual website URL

driver.find_element(By.LINK_TEXT,"My Account").click()
email = driver.find_element(By.ID,"reg_email").send_keys("johnpete@gmail.com")
driver.find_element(By.ID,"reg_password").send_keys("JOHN@PET@123 ")
register_button = driver.find_element(By.XPATH,"//input[@type ='submit'")
register_button.click()
time.sleep(10)

# Verify the error message displayed due to duplicate registration attempt
error_message = driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']").text
expected_error_message = "An account is already registered with your email address. Please login"
assert error_message == expected_error_message, f"Expected: {expected_error_message}, Actual: {error_message}"

# Close the browser window
driver.quit()
