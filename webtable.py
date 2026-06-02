from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome
options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# Load URL
driver.get("https://leafground.com/table.xhtml")

# Implicit wait
driver.implicitly_wait(15)

# Number of Rows
rows = driver.find_elements(By.XPATH, "//div[@class='ui-datatable-scrollable-body']/table/tbody/tr")
print("The Row count is:", len(rows))

# Number of Columns
columns = driver.find_elements(By.XPATH, "//div[@class='ui-datatable-scrollable-body']/table/tbody/tr[1]/td")
print("Column count is:", len(columns))

# Print row 2
row2 = driver.find_elements(By.XPATH, "//div[@class='ui-datatable-scrollable-body']/table/tbody/tr[2]/td")
for cell in row2:
    print("Row 2 Value:", cell.text)

# Print all data
all_data = driver.find_elements(By.XPATH, "//div[@class='ui-datatable-scrollable-body']/table/tbody/tr/td")
for data in all_data:
    print("Table Data:", data.text)

# Close browser
driver.quit()
