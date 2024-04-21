# pages/my_account_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.my_account_link = (By.LINK_TEXT, "My Account")
        self.address_link = (By.LINK_TEXT, "Addresses")

    def goto_dashboard(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.my_account_link)).click()

    def goto_addresses(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.address_link)).click()
