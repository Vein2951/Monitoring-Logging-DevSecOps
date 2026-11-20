from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:5000")

    page_title = driver.find_element(By.TAG_NAME, "h1").text

    print("Page heading:", page_title)

    assert "Dashboard Enabled" in page_title

    print("Selenium test passed!")

finally:
    driver.quit()
