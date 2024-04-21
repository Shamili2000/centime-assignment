from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
# Function to add product to cartxfr
driver.get("https://practice.automationtesting.in/shop/")
driver.find_element(By.XPATH,'//a[@data-product_id = "170"]').click()
driver.find_element(By.XPATH,'//a[@data-product_id = "180"]').click()
driver.find_element(By.XPATH,'//a[@data-product_id = "169"]').click()
driver.find_element(By.XPATH,'//a[@data-product_id = "160"]').click()
driver.find_element(By.XPATH,'//a[@data-product_id = "165"]').click()
driver.find_element(By.XPATH,'//a[@data-product_id = "163"]').click()
driver.find_element(By.LINK_TEXT,"View Basket").click()
driver.find_element(By.XPATH,'//a[@class = "checkout-button button alt wc-forward"]').click()
driver.find_element(By.ID,"billing_first_name").send_keys("sampakumari")
driver.find_element(By.NAME,"billing_last_name").send_keys("vanga")
driver.find_element(By.ID,"billing_company").send_keys("infosys")
driver.find_element(By.ID,"billing_email").send_keys("sampakumari12@gmail.com")
driver.find_element(By.ID,"billing_phone").send_keys("9567893456")
driver.find_element(By.ID,"s2id_autogen1_search").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements(By.CSS_SELECTOR,"ul[role = 'listbox']div")
for country in countries:
    if country.text == 'India':
        country.click()
        break
driver.find_element(By.ID,"billing_address_1").send_keys("5-6/1,khammam")
driver.find_element(By.ID,"billing_address_2_field").send_keys("viharnagar")
driver.find_element(By.ID,"billing_city").send_keys("khammam")
dropdown = driver.find_element(By.ID,"select2-drop-mask")
driver.find_element(By.ID,"select2-drop").send_keys("Tel")
time.sleep(2)
states = driver.find_elements(By.CSS_SELECTOR,'div[class = "select2-results"')
for state in states:
    if state.text == 'Telangana':
        state.click()
        break
driver.find_element(By.ID,"billing_postcode").send_keys("507189")
payment = driver.find_elements(By.CSS_SELECTOR,"ul[class='wc_payment_methods payment_methods methods']")
for paymentmethod in payment:
    if paymentmethod.get_attribute("value")=="Cash on Delivery":
        paymentmethod.click()
driver.find_element(By.ID,"place_order").click()












