from selenium import webdriver
chrom_driver_path = "D:\chromDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrom_driver_path)
driver.get("https://www.python.org/")
event_times = driver.find_elements_by_css_selector(".event-widget time")
event_where = driver.find_elements_by_css_selector(".event-widget li a")
my_dic = {}
for n in range(len(event_times)):
    my_dic[n] = {
        "time": event_times[n].text,
        "name": event_where[n].text,
    }
print(my_dic)
