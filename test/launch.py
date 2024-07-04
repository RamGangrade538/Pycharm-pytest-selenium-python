from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = '/home/ubuntu/Downloads/chromedriver-linux64/chromedriver'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://www.google.com")
search_box = driver.find_element("name", 'q')
search_box.send_keys('Selenium')
search_box.submit()

# Close the browser
driver.quit()
