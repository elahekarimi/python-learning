import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrom_driver_path = "D:\chromDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrom_driver_path)


driver.get("https://www.linkedin.com/")
time.sleep(5)
email = driver.find_element_by_xpath('//*[@id="session_key"]')
email.send_keys("elikarimi7019@gmail.com")
password= driver.find_element_by_xpath('//*[@id="session_password"]')
password.send_keys("5080034890")
submit = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/div/form/button')
submit.send_keys(Keys.ENTER)
time.sleep(5)
apply_button = driver.find_element_by_xpath('//*[@id="ember20"]/svg/use')
apply_button.click()
time.sleep(5)
phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys("+989357787252")

#Submit the application
submit_button = driver.find_element_by_css_selector("footer button")
submit_button.click()




