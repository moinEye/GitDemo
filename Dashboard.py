from selenium import webdriver
import time

sec = 0
driver = webdriver.Chrome(executable_path="C:\\Users\\s\\PycharmProjects\\pythontest\\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/validateCredentials")

login_username = "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[2]/input"
driver.find_element_by_xpath(login_username).send_keys("Admin")
time.sleep(sec)
login_pass = "/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[3]/input"
elm = driver.find_element_by_xpath(login_pass)
elm.send_keys("admin123")
time.sleep(sec)
elm.submit()

# This time panel login successfully.

time.sleep(sec)

admin = "/html/body/div[1]/div[2]/ul/li[1]/a/b"
driver.find_element_by_xpath(admin).click()

time.sleep(sec)

PIM = "/html/body/div[1]/div[2]/ul/li[2]/a/b"
driver.find_element_by_xpath(PIM).click()

time.sleep(sec)

Leave = "#menu_leave_viewLeaveModule > b"
driver.find_element_by_css_selector(Leave).click()

time.sleep(sec)

Time = "#menu_time_viewTimeModule > b"
driver.find_element_by_css_selector(Time).click()

time.sleep(sec)

Rec = "/html/body/div[1]/div[2]/ul/li[5]/a/b"
driver.find_element_by_xpath(Rec).click()

time.sleep(sec)

My_info = "#menu_pim_viewMyDetails > b"
driver.find_element_by_css_selector(My_info).click()

time.sleep(sec)

# Per = "/html/body/div[1]/div[2]/ul/li[7]/a/b"
# driver.find_element_by_xpath(Per).click()
# Note: not working in the panel aslo

Dashboard = "/html/body/div[1]/div[2]/ul/li[8]/a/b"
driver.find_element_by_xpath(Dashboard).click()

time.sleep(sec)

Dir = "#menu_directory_viewDirectory > b"
driver.find_element_by_css_selector(Dir).click()

time.sleep(sec)

Main = "/html/body/div[1]/div[2]/ul/li[10]/a/b"
driver.find_element_by_xpath(Main).click()

time.sleep(sec)

Buzz = "/html/body/div[1]/div[2]/ul/li[11]/a/b"
driver.find_element_by_xpath(Buzz).click()

time.sleep(sec)

Marketplace = "#MP_link"
driver.find_element_by_css_selector(Marketplace).click()

time.sleep(sec)

profile = "welcome"
driver.find_element_by_id(profile).click()

time.sleep(sec)

about = "aboutDisplayLink"
driver.find_element_by_id(about).click()

time.sleep(sec)

support = "/html/body/div[1]/div[1]/div[9]/ul/li[2]/a"
driver.find_element_by_xpath(support).click()

time.sleep(sec)











