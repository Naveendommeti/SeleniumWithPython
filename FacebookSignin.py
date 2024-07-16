import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.maximize_window()
#Find element using CSS selector-tag and id
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("122")
time.sleep(5)
#tag and class
#driver.find_element(By.CSS_SELECTOR,"input.inputtext _55r1 _6luy").send_keys("7097763071")
#tag and attribute (without quotes)
driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_pass]").send_keys("xyz")
#tag,class and attribute
driver.find_element(By.CSS_SELECTOR,"button._42ft").click()
time.sleep(5)
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))
time.sleep(5)