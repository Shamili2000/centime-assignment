 
from pages.loginpage import LoginPage
from Utils import driver_manager
# tests/test_login_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
import time
from selenium.webdriver.common.by import By
from pages.homepage import HomePage
@pytest.fixture
def setup_driver():
    driver = driver_manager.DriverManager.create_driver("chrome")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# def test_add_book_to_basket(setup_driver):
#     # Initialize HomePage with the WebDriver instance
#     home_page = HomePage(setup_driver)

#     # Open the URL
#     home_page.Open_url("http://practice.automationtesting.in/")

#     # Click on the Shop menu
#     home_page.click_shop_menu()

#     # Click on the Home button
#     home_page.click_home_button()
#     time.sleep(2)
    
#     # Verify that the Home page contains exactly three Arrivals
#     assert home_page.count_arrivals() == 3, "Home page does not display exactly three Arrivals"

#     # Click on the image of the specified book within Arrivals
#     home_page.click_arrival_image("//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[1]")

#     # Add the book to the basket
#     home_page.button_add_to_basket()

#     home_page.open_basket()

#     # Verify that the book is added to the basket
#     assert home_page.is_book_in_basket(), "Book is not found in the Basket"
# def test_add_book_to_basket(setup_driver):
#     # Initialize HomePage with the WebDriver instance
#     home_page = HomePage(setup_driver)

#     # Open the URL
#     home_page.Open_url("http://practice.automationtesting.in/")

#     # Click on the Shop menu
#     home_page.click_shop_menu()

#     # Click on the Home button
#     home_page.click_home_button()
#     time.sleep(2)
    
#     # Verify that the Home page contains exactly three Arrivals
#     assert home_page.count_arrivals() == 3, "Home page does not display exactly three Arrivals"

#     # Click on the image of the specified book within Arrivals
#     home_page.click_arrival_image("//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[1]")

#     # Add the book to the basket
#     home_page.button_add_to_basket()

#     home_page.open_basket()

#     # Verify that the book is added to the basket
#     assert home_page.is_book_in_basket(), "Book is not found in the Basket"

#     quantity_input = home_page.find_element_(By.NAME, "cart[b73ce398c39f506af761d2277d853a92][qty]")
#     quantity_input.clear()
#     quantity_input.send_keys("21")

#     # Click the add to basket button
#     add_to_basket_button_3 = home_page.find_element_(By.NAME, "update_cart")
#     add_to_basket_button_3.click()

#     # Verify the error message for exceeding the stock limit
#     error_message = WebDriverWait(setup_driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "woocommerce-message")))
#     assert "must be less than or equal to 20" in error_message.text, "Expected error message not displayed"



# def test_add_more_book_to_basket(setup_driver):
#     # Initialize HomePage with the WebDriver instance
#     home_page = HomePage(setup_driver)

#     # Open the URL
#     home_page.Open_url("http://practice.automationtesting.in/")

#     # Click on the Shop menu
#     home_page.click_shop_menu()

#     # Click on the Home button
#     home_page.click_home_button()
#     time.sleep(2)
    
#     # Verify that the Home page contains exactly three Arrivals
#     assert home_page.count_arrivals() == 3, "Home page does not display exactly three Arrivals"

#     # Click on the image of the specified book within Arrivals
#     home_page.click_arrival_image("//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[1]")

#     # Add the book to the basket
#     home_page.button_add_to_basket()
    
#     home_page.open_basket()

#     # Verify that the book is added to the basket
#     item_link = WebDriverWait(setup_driver, 10).until(ec.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
#     item_link.click()

#     # 10) Verify navigation to the checkout page
#     checkout_heading = WebDriverWait(setup_driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "entry-title")))
#     assert checkout_heading.text == "Checkout", "Not navigated to the Checkout page"

#     print("All steps executed successfully!")

def  test_remove_from_basket(setup_driver):
        home_page = HomePage(setup_driver)

       # Open the URL
        home_page.Open_url("http://practice.automationtesting.in/")

    # Click on the Shop menu
        home_page.click_shop_menu()
        home_page.frame()
    # Click on the Home button
        home_page.click_home_button()
        time.sleep(2)
        home_page.frame()
    
    # Verify that the Home page contains exactly three Arrivals
        assert home_page.count_arrivals() == 3, "Home page does not display exactly three Arrivals"

    # Click on the image of the specified book within Arrivals
        home_page.click_arrival_image("//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[1]")

    # Add the book to the basket
        home_page.button_add_to_basket()
    
        home_page.open_basket()
        home_page.frame()
    

   
    # 11) Click on the Remove icon in the Checkout page to remove the book from the grid
        remove_icon = home_page.find_element_(By.XPATH, "//td[@class='product-remove']/a")
        remove_icon.click()

    # 12) Verify that the book is removed from the grid
        empty_cart_message = home_page.find_element_(By.XPATH, "//p[contains(text(), 'Your basket is currently empty')]")
        assert "Your basket is currently empty" in empty_cart_message.text, "Book was not removed from the grid"

        print("All steps executed successfully!")



# def test_add_book_to_basket(setup_driver):
#     # Initialize HomePage with the WebDriver instance
#     home_page = HomePage(setup_driver)

#     # Open the URL
#     home_page.Open_url("http://practice.automationtesting.in/")

#     # Click on the Shop menu
#     home_page.click_shop_menu()

#     # Click on the Home button
#     home_page.click_home_button()
#     time.sleep(2)
    
#     # Verify that the Home page contains exactly three Arrivals
#     assert home_page.count_arrivals() == 3, "Home page does not display exactly three Arrivals"

#     # Click on the image of the specified book within Arrivals
#     home_page.click_arrival_image("//*[@id='text-22-sub_row_1-0-2-0-0']/div/ul/li/a[1]")

#     # Add the book to the basket
#     home_page.button_add_to_basket()

#     home_page.open_basket()

#     # Verify that the book is added to the basket
#     assert home_page.is_book_in_basket(), "Book is not found in the Basket"

#     quantity_input = home_page.find_element_(By.NAME, "cart[b73ce398c39f506af761d2277d853a92][qty]")
#     quantity_input.clear()
#     quantity_input.send_keys("21")

#     # Click the add to basket button
#     add_to_basket_button_3 = home_page.find_element_(By.NAME, "update_cart")
#     add_to_basket_button_3.click()

#     # Verify the error message for exceeding the stock limit
#     error_message = WebDriverWait(setup_driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, "woocommerce-message")))
#     assert "must be less than or equal to 20" in error_message.text, "Expected error message not displayed"



def test_remove_all_book_to_basket(setup_driver):
    # Initialize HomePage with the WebDriver instance
    home_page = HomePage(setup_driver)

    # Open the URL
    home_page.Open_url("http://practice.automationtesting.in/")

    # Click on the Shop menu
    home_page.click_shop_menu()

    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "170"]').click()
    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "180"]').click()
    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "169"]').click()
    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "160"]').click()
    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "165"]').click()
    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "163"]').click()
    setup_driver.find_element(By.LINK_TEXT,"View Basket").click()
    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "165"]').click()
    setup_driver.find_element(By.XPATH,'//input[@type = "submit"]').click()
    # setup_driver.find_element(By.XPATH,'//a[@class = "checkout-button"').click()

    # Click on the image of the specified book within Arrivals
    

    
    
    home_page.open_basket()

    remove_icon = home_page.find_elements_(By.XPATH, "//td[@class='product-remove']/a")
    for i in remove_icon:
         i.click()

    # Verify that the book is added to the basket
    item_link = WebDriverWait(setup_driver, 10).until(ec.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
    item_link.click()

    # 10) Verify navigation to the checkout page
    checkout_heading = WebDriverWait(setup_driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "entry-title")))
    assert checkout_heading.text == "Checkout", "Not navigated to the Checkout page"

    print("All steps executed successfully!")

def test_add_more_book_to_basket(setup_driver):
    # Initialize HomePage with the WebDriver instance
    home_page = HomePage(setup_driver)

    # Open the URL
    home_page.Open_url("http://practice.automationtesting.in/")

    # Click on the Shop menu
    home_page.click_shop_menu()

    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "170"]').click()
    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "180"]').click()
    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "169"]').click()
    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "160"]').click()
    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "165"]').click()
    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "163"]').click()
    setup_driver.find_element(By.LINK_TEXT,"View Basket").click()
    setup_driver.find_element(By.XPATH,'//a[@data-product_id = "165"]').click()
    setup_driver.find_element(By.XPATH,'//input[@type = "submit"]').click()
    # setup_driver.find_element(By.XPATH,'//a[@class = "checkout-button"').click()

    # Click on the image of the specified book within Arrivals
    

    
    
    home_page.open_basket()

    # Verify that the book is added to the basket
    item_link = WebDriverWait(setup_driver, 10).until(ec.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
    item_link.click()

    # 10) Verify navigation to the checkout page
    checkout_heading = WebDriverWait(setup_driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "entry-title")))
    assert checkout_heading.text == "Checkout", "Not navigated to the Checkout page"

    print("All steps executed successfully!")