import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.audible.in/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,"a.bc-link.ui-it-sign-in-link.bc-color-base").click()
time.sleep(5)
driver.find_element(By.ID,"ap_email").send_keys("dommetna+test-tipocaqbUT1718955669176@amazon.com")
driver.find_element(By.CSS_SELECTOR,"input#continue").click()
driver.find_element(By.NAME,"password").send_keys("nafb%z$2vt38a!qs")
driver.find_element(By.CSS_SELECTOR,"input.a-button-input[aria-labelledby=auth-signin-button-announce").click()
time.sleep(20)
driver.quit()
