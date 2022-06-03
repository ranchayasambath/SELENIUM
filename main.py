# using webdriver with selenium
from selenium import webdriver


# path to the chrome webdriver exe file that controls the code
PATH = "C:\chromedriver.exe"
PATH2 = "C:\chromedriver2.exe"



# set driver to path of chromedriver
driver = webdriver.Chrome(PATH)
# assign the passed in url
url = 'https://share.hsforms.com/1DXiqHMY_Sie_ud0bcep1VQ1odv5?__hstc=241689437.dd647fa92316e2c182cc877f6b41a72b.1552417543081.1631030947093.1631039819157.252&__hssc=241689437.1.1631039819157&__hsfp=988172843&utm_medium=email&_hsmi=156987797&_hsenc=p2ANqtz-9DRFQ53QBgBj-SF2JxoYDHPadh6Xo04fjwykDHB6eBtFg3a1N5BIwinDQCB_zHGdMfCK3OF2trzIFLqou9ou3sPyjDzySx5QQ7j6Lx8SZ7N6id0Gk&utm_content=156987797&utm_source=hs_email'

# open first url
driver.get(url)

driver.execute_script("window.open('');")
# Switch to the new window and open new URL
driver.switch_to.window(driver.window_handles[1])
driver.get(url)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get(url)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[3])
driver.get(url)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[4])
driver.get(url)
