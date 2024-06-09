#Run Drivers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver
driver = webdriver.Chrome()

# Navigate to Google
driver.get("https://www.google.com")

# Enter the search query
search_box = driver.find_element_by_name("q")
search_box.send_keys("Where am I")

# Submit the search query
search_box.submit()

# Wait for the search results to load
try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "res"))
    )
except:
    print("Failed to load search results")

# Close the browser
driver.quit()
