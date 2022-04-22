import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


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

all_listings = driver.find_element_by_css_selector("global-nav-icon--mercado__jobs--active")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

    # Try to locate the apply button, if can't locate then skip the job.
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys("+989357787252")

        submit_button = driver.find_element_by_css_selector("footer button")

        # If the submit_button is a "Next" button, then this is a multi-step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()



