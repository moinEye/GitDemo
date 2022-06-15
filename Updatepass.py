from selenium import webdriver
import time

sec = 1

driver = webdriver.Chrome(executable_path="C:\\Users\\s\\PycharmProjects\\pythontest\\chromedriver.exe")

driver.get("https://dev.zicharge.com/")

Phone = "/html/body/div/div/div/div[1]/form/div[3]/div[1]/input"
driver.find_element_by_xpath(Phone).send_keys("1798798087")

time.sleep(sec)

password = "/html/body/div/div/div/div[1]/form/div[3]/div[2]/input"
elm = driver.find_element_by_xpath(password)
elm.send_keys("Msi@1234")
elm.submit()

time.sleep(sec)

Currentpass = "/html/body/div/div[3]/div[2]/div/div[2]/div/div[1]/div[1]/div/div[2]/form/div[1]/div/input"
elmc = driver.find_element_by_xpath(Currentpass)
elmc.send_keys("Msi@1234")

Newpass = "password"
elmn = driver.find_element_by_name(Newpass)
elmn.send_keys("Msi@1234")

Repass = "password_confirmation"
elmr = driver.find_element_by_name(Repass)
elmr.send_keys("Msi@1234")
elmr.submit()
