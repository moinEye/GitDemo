from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\s\\PycharmProjects\\pythontest\\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")

login_username = "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input"
driver.find_element_by_xpath(login_username).send_keys("Admin")

time.sleep(1)

login_pass = "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input"
elm = driver.find_element_by_xpath(login_pass)
elm.send_keys("admin123")

time.sleep(1)

elm.submit()

time.sleep(1)

admin = "/html/body/div[1]/div[2]/ul/li[1]/a/b"
driver.find_element_by_xpath(admin).click()

search_username = "searchSystemUser_userName"
username = driver.find_element_by_id(search_username)
username.send_keys("Aravind")
username.submit()

time.sleep(1)

search_employeename = "#searchSystemUser_employeeName_empName"
employee = driver.find_element_by_css_selector(search_employeename)
employee.send_keys("Dominic Chase")
employee.submit()






