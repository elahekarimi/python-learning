from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrom_driver_path = "D:\chromDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrom_driver_path)
driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element_by_name("fName")
first_name.send_keys("eli")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("karimi")
email = driver.find_element_by_name("email")
email.send_keys("eljkbhdnls")

submit = driver.find_element_by_xpath("/html/body/form/button")
submit.send_keys(Keys.ENTER)