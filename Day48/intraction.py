from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrom_driver_path = "D:\chromDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrom_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# number = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# number.click()
search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)
