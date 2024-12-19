import random
import string
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class RegisterAccountPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.my_account=(By.XPATH,"//a[@title='My Account']")
        self.register_opt = (By.XPATH, "//a[normalize-space()='Register']")
        self.warning_message=(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']")
        self.continue_button = (By.XPATH, "//input[@value='Continue']")
        self.continue_button2 = (By.XPATH, "//a[normalize-space()='Continue']")
        self.first_name=(By.XPATH,"//input[@id='input-firstname']")
        self.last_name = (By.XPATH, "//input[@id='input-lastname']")
        self.email = (By.XPATH, "//input[@id='input-email']")
        self.first_name_error_message = (By.XPATH, "//div[contains(text(),'First Name must be between 1 and 32 characters!')]")
        self.last_name_error_message = (By.XPATH, "//div[contains(text(),'Last Name must be between 1 and 32 characters!')]")
        self.telephone = (By.XPATH, "//input[@id='input-telephone']")
        self.password = (By.XPATH, "//input[@id='input-password']")
        self.confirm = (By.XPATH, "//input[@id='input-confirm']")
        self.yes = (By.XPATH, "//label[normalize-space()='Yes']")
        self.agree = (By.XPATH, "//input[@name='agree']")
        self.view_order_history=(By.XPATH,"//div[@id='content']//a[normalize-space()='Order History']")
        self.account_creation = (By.XPATH, "//p[contains(text(),'Congratulations! Your new account has been success')]")
    def verify_main_page_header(self):
        # Step 21: Verify 'Account Logout' heading
        expected_title = "Your Store"
        actual_title = self.driver.title
        assert expected_title == actual_title, f"Page title mismatch! Expected: {expected_title}, Got: {actual_title}"
    def go_to_register_account_page(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.my_account)).click()
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.register_opt)).click()
    def verify_register_page_header(self):
        # Step 21: Verify 'Account Logout' heading
        time.sleep(3)
        expected_title = "Register Account"
        actual_title = self.driver.title
        assert expected_title == actual_title, f"Page title mismatch! Expected: {expected_title}, Got: {actual_title}"
    def verify_warning_message(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_button)).click()
        time.sleep(5)
        element = self.driver.find_element(*self.warning_message)
        expected_message="Warning: You must agree to the Privacy Policy!"
        # Extract the text of the warning message
        actual_message = element.text.strip()
        assert expected_message == actual_message, f"Warning message mismatch! Expected: {expected_message}, Got: {actual_message}"
    def enter_first_name(self,firstname):
        time.sleep(3)
        self.driver.find_element(*self.first_name).send_keys(firstname)
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_button)).click()
    def verify_first_name_error(self):
            expected_message = "First Name must be between 1 and 32 characters!"
            error_message_element = self.driver.find_element(*self.first_name_error_message)
            # Verify if the error message is displayed and matches the expected text
            assert error_message_element.is_displayed(), "Error message not displayed."
            assert error_message_element.text == expected_message, f"Expected error message: '{expected_message}', but got: '{error_message_element.text}'"
    def enter_last_name(self,lastname):
        time.sleep(3)
        self.driver.find_element(*self.last_name).send_keys(lastname)
        time.sleep(3)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.continue_button)).click()
    def verify_last_name_error(self):
            expected_message = "Last Name must be between 1 and 32 characters!"
            error_message_element = self.driver.find_element(*self.last_name_error_message)
            # Verify if the error message is displayed and matches the expected text
            assert error_message_element.is_displayed(), "Error message not displayed."
            assert error_message_element.text == expected_message, f"Expected error message: '{expected_message}', but got: '{error_message_element.text}'"
    def enter_email(self):
        time.sleep(4)
        random_name = ''.join(random.choices(string.ascii_letters, k=10))  # Generates a random name of 10 letters
        random_email = f"{random_name}@example.com"  # Create an email from the name
        self.driver.find_element(*self.email).send_keys(random_email)
    def enter_telephone(self, number):
        # Wait for the telephone field to be clickable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.telephone)
        )
        self.driver.find_element(*self.telephone).send_keys(number)
    def clear_and_enter_last_name(self, lastname):
        last_name_field = self.driver.find_element(*self.last_name)
        last_name_field.clear()  # Clear the field
        last_name_field.send_keys(lastname)  # Send the new last name
    def clear_and_enter_first_name(self, firstname):
            time.sleep(2)
            first_name_field = self.driver.find_element(*self.first_name)
            first_name_field.clear()  # Clear the field
            first_name_field.send_keys(firstname)
    def enter_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)
        time.sleep(1)
        self.driver.find_element(*self.confirm).send_keys(password)
        time.sleep(1)
    def select_yes_opt(self):
        self.driver.find_element(*self.yes).click()
    def click_agree(self):
        self.driver.find_element(*self.agree).click()
        time.sleep(2)
    def click_continue_button(self):
        # Find the continue button and click it
        continue_button_element = self.driver.find_element(*self.continue_button)
        continue_button_element.click()

    def click_continue_button2(self):
        # Find the continue button and click it
        continue_button_element = self.driver.find_element(*self.continue_button2)
        continue_button_element.click()

    def verify_account_creation(self):
        time.sleep(5)
        element = self.driver.find_element(*self.account_creation)
        expected_message = "Congratulations! Your new account has been successfully created!"
        # Extract the text of the warning message
        actual_message = element.text.strip()
        assert expected_message == actual_message, f"Warning message mismatch! Expected: {expected_message}, Got: {actual_message}"
    def click_order_history(self):
        order_history=self.driver.find_element(*self.view_order_history)
        order_history.click()

class AddressBookPage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.address_book_option = (By.XPATH, "//a[@class='list-group-item'][normalize-space()='Address Book']")
        self.new_address = (By.XPATH, "//a[normalize-space()='New Address']")
        self.first_name = (By.XPATH, "//input[@id='input-firstname']")
        self.last_name = (By.XPATH, "//input[@id='input-lastname']")
        self.input_address = (By.XPATH, "//input[@id='input-address-1']")
        self.city=(By.XPATH,"//input[@id='input-city']")
        self.postal_code=(By.XPATH,"//input[@id='input-postcode']")
        self.continue_button = (By.XPATH, "//input[@value='Continue']")
    def select_address_book_opt(self):
        address = self.driver.find_element(*self.address_book_option)
        address.click()
    def select_new_address(self):
        new_address = self.driver.find_element(*self.new_address)
        new_address.click()
    def enter_first_name(self,first_name):
        self.driver.find_element(*self.first_name).send_keys(first_name)
    def enter_last_name(self,last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)
    def enter_input_address(self,address):
        self.driver.find_element(*self.input_address).send_keys(address)
    def enter_city(self,city):
        self.driver.find_element(*self.city).send_keys(city)
    def enter_postal_code(self,postalcode):
        self.driver.find_element(*self.postal_code).send_keys(postalcode)
    def select_country_and_state(self):
        country_dropdown = self.driver.find_element("id", "input-country")
        Select(country_dropdown).select_by_value("99")
        time.sleep(3)
        zone_dropdown = self.driver.find_element("xpath", "//select[@id='input-zone']")
        Select(zone_dropdown).select_by_value("4231")
    def click_continue_button(self):
        # Find the continue button and click it
        continue_button_element = self.driver.find_element(*self.continue_button)
        continue_button_element.click()



