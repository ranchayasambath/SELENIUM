import subprocess
# using webdriver with selenium
from selenium import webdriver
import time

# path to the chrome webdriver exe file 
PATH = "C:\chromedriver.exe"

# Set chromedriver's path
driver = webdriver.Chrome(PATH)
driver.maximize_window() # For maximizing window
driver.implicitly_wait(20) # gives an implicit wait for 20 seconds
# Store url inside variable
url = 'https://share.hsforms.com/1DXiqHMY_Sie_ud0bcep1VQ1odv5?__hstc=241689437.dd647fa92316e2c182cc877f6b41a72b.1552417543081.1631030947093.1631039819157.252&__hssc=241689437.1.1631039819157&__hsfp=988172843&utm_medium=email&_hsmi=156987797&_hsenc=p2ANqtz-9DRFQ53QBgBj-SF2JxoYDHPadh6Xo04fjwykDHB6eBtFg3a1N5BIwinDQCB_zHGdMfCK3OF2trzIFLqou9ou3sPyjDzySx5QQ7j6Lx8SZ7N6id0Gk&utm_content=156987797&utm_source=hs_email'

#Initial page load
# driver.get(url)

 #Identify user input fields through id's
# input_fname = driver.find_element_by_id('firstname-input')

# input_lname = driver.find_element_by_id('lastname-input')

# input_email = driver.find_element_by_id('email-input')

# input_cohort = driver.find_element_by_id('cohort_accepted-input')

# input_job_source = driver.find_element_by_id('job_source_-input')

# # automated information filling out
# input_fname.send_keys('Ranchaya')

# input_lname.send_keys('Sambath')

# input_email.send_keys('ranchayasambath@gmail.com')

# input_cohort.send_keys('Sirius')

# input_job_source.send_keys('Independent Search')

# #checkbox for email copy
# agreed = driver.find_element_by_id("copy_of_form_submission-input")
# if agreed.get_attribute("checked") != "true":
#     agreed.click()

# # Consecutive tabs
# driver.execute_script("window.open('');")

# driver.switch_to.window(driver.window_handles[1])

# driver.get(url)

# input_fname = driver.find_element_by_id('firstname-input')

# input_lname = driver.find_element_by_id('lastname-input')

# input_email = driver.find_element_by_id('email-input')

# input_cohort = driver.find_element_by_id('cohort_accepted-input')

# input_job_source = driver.find_element_by_id('job_source_-input')

# input_fname.send_keys('Ranchaya')

# input_lname.send_keys('Sambath')

# input_email.send_keys('ranchayasambath@gmail.com')

# input_cohort.send_keys('Sirius')

# input_job_source.send_keys('Independent Search')
# # --------------------------------------------------------------------
# driver.execute_script("window.open('');")

# driver.switch_to.window(driver.window_handles[2])

# driver.get(url)

# input_fname = driver.find_element_by_id('firstname-input')

# input_lname = driver.find_element_by_id('lastname-input')

# input_email = driver.find_element_by_id('email-input')

# input_cohort = driver.find_element_by_id('cohort_accepted-input')

# input_job_source = driver.find_element_by_id('job_source_-input')

# input_fname.send_keys('Ranchaya')

# input_lname.send_keys('Sambath')

# input_email.send_keys('ranchayasambath@gmail.com')

# input_cohort.send_keys('Sirius')

# input_job_source.send_keys('Independent Search')
# # --------------------------------------------------------------------
# driver.execute_script("window.open('');")

# driver.switch_to.window(driver.window_handles[3])

# driver.get(url)

# input_fname = driver.find_element_by_id('firstname-input')

# input_lname = driver.find_element_by_id('lastname-input')

# input_email = driver.find_element_by_id('email-input')

# input_cohort = driver.find_element_by_id('cohort_accepted-input')

# input_job_source = driver.find_element_by_id('job_source_-input')

# input_fname.send_keys('Ranchaya')

# input_lname.send_keys('Sambath')

# input_email.send_keys('ranchayasambath@gmail.com')

# input_cohort.send_keys('Sirius')

# input_job_source.send_keys('Independent Search')
# # --------------------------------------------------------------------
# driver.execute_script("window.open('');")

# driver.switch_to.window(driver.window_handles[4])

# driver.get(url)

# input_fname = driver.find_element_by_id('firstname-input')

# input_lname = driver.find_element_by_id('lastname-input')

# input_email = driver.find_element_by_id('email-input')

# input_cohort = driver.find_element_by_id('cohort_accepted-input')

# input_job_source = driver.find_element_by_id('job_source_-input')

# input_fname.send_keys('Ranchaya')

# input_lname.send_keys('Sambath')

# input_email.send_keys('ranchayasambath@gmail.com')

# input_cohort.send_keys('Sirius')

# input_job_source.send_keys('Independent Search')

# --------------------- Refactored Version ----------------------------------------------
for i in range (5):

    driver.execute_script("window.open(' ')")

    driver.switch_to.window(driver.window_handles[i])

    driver.get(url)

    input_fname = driver.find_element_by_id('firstname-input')

    input_lname = driver.find_element_by_id('lastname-input')

    input_email = driver.find_element_by_id('email-input')

    input_cohort = driver.find_element_by_id('cohort_accepted-input')

    input_job_source = driver.find_element_by_id('job_source_-input')

    input_fname.send_keys('Ranchaya')

    input_lname.send_keys('Sambath')

    input_email.send_keys('ranchayasambath@gmail.com')

    input_cohort.send_keys('Sirius')

    input_job_source.send_keys('Independent Search')

    agreed = driver.find_element_by_id("copy_of_form_submission-input")
    if agreed.get_attribute("checked") != "true":
        agreed.click()
time.sleep(5)
driver.quit()
 #Terminate all chromedrivers that built up to reclaim resources.   
subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")
#--------------------------------------------------------------------------------------------