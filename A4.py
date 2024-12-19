from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Initialize WebDriver
driver = webdriver.Firefox()
driver.maximize_window()

# Step 1: Open the URL and Login
driver.get("https://demo.opencart.com.gr/")
time.sleep(5)
driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Login')]").click()
time.sleep(5)
driver.find_element(By.ID, "input-email").send_keys("satwikkatamaraju@gmail.com")  # Replace with your email
driver.find_element(By.ID, "input-password").send_keys("2003@Democart")  # Replace with your password
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(5)

# Step 2: Navigate to Components -> Monitors
driver.find_element(By.XPATH, "//a[contains(text(),'Components')]").click()
driver.find_element(By.XPATH, "//a[contains(text(),'Monitors')]").click()
time.sleep(5)

# Step 3: Select '25' from 'Show' dropdown
select_show = Select(driver.find_element(By.ID, "input-limit"))
select_show.select_by_visible_text("25")
time.sleep(5)

# Step 4: Click on 'Add to cart' for the first item
driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[1]/div/div[2]/div[2]/button[1]').click()
time.sleep(5)

# Step 5: Click on 'Specification' tab
driver.find_element(By.XPATH, "//a[text()='Specification']").click()
time.sleep(5)

# Step 6: Verify details present on the page
specifications = driver.find_element(By.XPATH, "//div[@id='tab-specification']").text
assert specifications != "", "Specifications are missing!"

# Step 7: Click on 'Add to Wish list' button
driver.find_element(By.XPATH, "//button[@data-original-title='Add to Wish List']").click()
time.sleep(5)

# Step 8: Verify success message
success_message = driver.find_element(By.XPATH, "//div[contains(@class, 'alert-success')]").text
assert "Success: You have added" in success_message, "Wish list success message not found!"

# Step 9: Enter 'Mobile' in 'Search' text box
driver.find_element(By.NAME, "search").send_keys("Mobile")

# Step 10: Click on 'Search' button
driver.find_element(By.XPATH, '//*[@id="search"]/span/button/i').click()
time.sleep(5)

# Step 11: Click on 'Search in product descriptions' checkbox
driver.find_element(By.NAME, "description").click()
time.sleep(5)

driver.find_element(By.XPATH,"//input[@id='button-search']").click()

# Step 12: Click on link 'HTC Touch HD'
driver.find_element(By.XPATH, '//*[@id="content"]/div[3]/div[1]/div/div[2]/div[1]/h4/a').click()
time.sleep(5)

# Step 13: Clear '1' from 'Qty' and enter '3'
quantity = driver.find_element(By.ID, "input-quantity")
quantity.clear()
quantity.send_keys("3")

# Step 14: Click on 'Add to Cart' button
driver.find_element(By.ID, "button-cart").click()
time.sleep(10)

# Step 15: Verify success message for HTC Touch HD
success_message = driver.find_element(By.XPATH, "//div[contains(@class, 'alert-success')]").text
assert "Success: You have added HTC Touch HD" in success_message, "HTC Touch HD success message not found!"

# Step 16: Click on 'View cart' button adjacent to search button
driver.find_element(By.XPATH, "//a[@title='Shopping Cart']").click()
time.sleep(2)

# Step 17: Verify Mobile name added to the cart
cart_items = driver.find_element(By.XPATH, "//div[@id='content']").text
assert "HTC Touch HD" in cart_items, "HTC Touch HD not found in cart!"

# Step 18: Click on 'Checkout' button
driver.find_element(By.XPATH, "//a[contains(text(),'Checkout')]").click()
time.sleep(2)

# Step 19: Click on 'My Account' dropdown
driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]").click()

# Step 20: Select 'Logout' from dropdown
driver.find_element(By.XPATH, "//a[contains(text(),'Logout')]").click()
time.sleep(2)

# Step 21: Verify 'Account Logout' heading
expected_title = "Account Logout"
actual_title = driver.title
assert expected_title == actual_title, f"Page title mismatch! Expected: {expected_title}, Got: {actual_title}"

# Step 22: Click on 'Continue' button
driver.find_element(By.XPATH, "//a[contains(text(),'Continue')]").click()
time.sleep(2)

# Close the browser
driver.quit()
