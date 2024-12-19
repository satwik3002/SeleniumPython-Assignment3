from selenium import webdriver
from pom import RegisterAccountPage, AddressBookPage  # Correct import statement
import time

def test_register_account():
    driver = webdriver.Chrome()
    driver.get("https://demo.opencart.com.gr/")
    driver.maximize_window()
    time.sleep(5)

    # Step 1: Login
    register_account_page = RegisterAccountPage(driver)
    register_account_page.verify_main_page_header()
    register_account_page.go_to_register_account_page()
    register_account_page.verify_warning_message()
    register_account_page.enter_first_name("Satwik Katamaraju the Great Master")
    register_account_page.verify_first_name_error()
    register_account_page.clear_and_enter_first_name("Katamaraju")
    register_account_page.enter_last_name("Satwik Katamaraju the Great Master")
    register_account_page.verify_last_name_error()
    register_account_page.clear_and_enter_last_name("Satwik")
    register_account_page.enter_email()
    register_account_page.enter_telephone("8919447382")
    register_account_page.enter_password("2003@Democart")
    register_account_page.select_yes_opt()
    register_account_page.click_agree()
    register_account_page.click_continue_button()
    time.sleep(3)
    register_account_page.verify_account_creation()
    register_account_page.click_continue_button2()
    time.sleep(3)
    register_account_page.click_order_history()
    # Step 2: Address
    address_page = AddressBookPage(driver)
    address_page.select_address_book_opt()
    address_page.select_new_address()
    time.sleep(3)
    address_page.enter_first_name("Katamaraju")
    time.sleep(3)
    address_page.enter_last_name("Satwik")
    address_page.enter_input_address("nagole")
    address_page.enter_city("Hyderabad")
    address_page.enter_postal_code("500038")
    time.sleep(3)
    address_page.select_country_and_state()
    address_page.click_continue_button()


if __name__ == "__main__":
    test_register_account()