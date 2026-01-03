import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Ensure the data directory exists
os.makedirs("data", exist_ok=True)

driver = webdriver.Chrome()
query = "doctors"
file = 0

for i in range(1, 10):
    driver.get(f"https://www.yello.ae/category/{query}-and-clinics/{i}")

    # Locate elements (update the locator as needed)
    elems = driver.find_elements(By.CLASS_NAME, "company")
    print(f"{len(elems)} items found")

    for elem in elems:
        d = elem.get_attribute("outerHTML")
        with open(f"data/{query}_{file}.html", "w", encoding="utf-8") as f:
            f.write(d)
        file += 1

    time.sleep(2)

driver.close()