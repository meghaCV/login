from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://google.com")
print(driver.title)

search_bar = driver.find_element_by_name("q")
search_bar.send_keys("Selenium WebDriver Interview questions")
search_bar.submit()
lists = driver.find_elements_by_id("rcnt")
print("Found " + str(len(lists)) + " searches:")
i=0
for listitem in lists:
   print (listitem.get_attribute("innerHTML"))
   i=i+1
   if(i>10):
      break
time.sleep(5)
driver.quit()
