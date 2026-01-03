from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://yello.ae/search?q=doctors+clinics")
time.sleep(5)  # Initial load

# ✅ Wait + Find companies
companies = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "campany"))
)

print(f"✅ Total companies mile: {len(companies)}")

# ✅ Loop me print karo
for i, company in enumerate(companies[:5]):  # Pehle 5 test ke liye
    try:
        name = company.find_element(By.CLASS_NAME, "company_name").text
        print(f"{i+1}. {name}")
    except Exception as e:
        print(f"Error in company {i+1}: {e}")

time.sleep(5)
driver.quit()
