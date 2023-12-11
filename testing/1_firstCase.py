import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.implicitly_wait(10)

#1)Login
driver.find_element(By.NAME,"username").clear()
driver.find_element(By.NAME,"username").send_keys("Admin")

driver.find_element(By.NAME,"password").clear()
driver.find_element(By.NAME,"password").send_keys("admin123")

driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']").click()

#2)Add Employee
driver.find_element(By.XPATH,"//span[normalize-space()='PIM']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Add']").click()
driver.find_element(By.XPATH,"//button[@class='oxd-icon-button oxd-icon-button--solid-main employee-image-action']").send_keys("C://Users//Suraj//Downloads//image.png")
driver.find_element(By.NAME,"firstName").send_keys("Amar")
driver.find_element(By.NAME,"middleName").send_keys("D")
driver.find_element(By.NAME,"lastName").send_keys("Gupta")
driver.find_element(By.XPATH,"//button[normalize-space()='Save']").click()
time.sleep(1)
driver.save_screenshot("C:\Screenshot\success1.png")

#3)Personal Details
driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[1]/div[1]/div[2]/input[1]").send_keys("bau")
driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[2]/div[1]/div[2]/div[1]/div[2]/input[1]").send_keys("9090")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input").send_keys("12345")
driver.find_element(By.XPATH,"//body/div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']/div[@class='orangehrm-background-container']/div[@class='orangehrm-card-container']/div[@class='orangehrm-edit-employee']/div[@class='orangehrm-edit-employee-content']/div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/form[@class='oxd-form']/div[@class='oxd-form-row']/div[@class='oxd-grid-3 orangehrm-full-width-grid']/div[2]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("2025-10-12")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input").send_keys("456787654")
driver.find_element(By.XPATH,"(//input)[11]").send_keys("2345432")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input").send_keys("1998-12-01")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span").click()
driver.find_element(By.XPATH,"//div[4]//div[1]//div[1]//div[1]//div[2]//input[1]").send_keys("No")
driver.find_element(By.XPATH,"//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//button[@type='submit'][normalize-space()='Save']").click()
time.sleep(1)
driver.save_screenshot("C:\Screenshot\success4.png")

#4)Search Employee
driver.find_element(By.XPATH,"//a[normalize-space()='Employee List']").click()
driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("Amar Gupta")
driver.find_element(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys("0305")
driver.find_element(By.XPATH,"//button[normalize-space()='Search']").click()

#5)Delete Emplyee
driver.find_element(By.XPATH,"//a[normalize-space()='Employee List']").click()
driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]").send_keys("Amar Gupta")
driver.find_element(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys("0305")
driver.find_element(By.XPATH,"//i[@class='oxd-icon bi-trash']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Yes, Delete']").click()
time.sleep(1)
driver.save_screenshot("C:\Screenshot\delete.png")

driver.close()