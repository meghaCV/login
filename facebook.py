from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path = "/Users/chandrashekarbasavaraj/Documents/chromeDriversSelenium/chromedriver-1")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://facebook.com")
print(driver.title)
#print(driver.current_url)
#print(driver.page_source)
search_bar = driver.find_element_by_name("email")
search_bar.send_keys("megha.cv27@gmail.com")

search_bar = driver.find_element_by_name("pass")
search_bar.send_keys("decemberdecember27")
driver.find_element_by_id("u_0_b").click()

time.sleep(5)
#driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div/div[1]/div[2]/div[4]")
#driver.find_element_by_xpath("//div[@id='userNavigationLabel']").click()
#driver.find_element_by_id("userNavigationLabel").click()
#driver.find_elements_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[4]/div[1]/span/div/div[1]/div")
'''search_bar = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/label/input")
search_bar.send_keys("market place stockholm")
search_bar.send_keys(Keys.RETURN)
search_bar = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div/div[1]/div[2]/div[4]/div[1]/span/div/div[1]")
search_bar.send_keys(Keys.RETURN)
search_bar = driver.find_element_by_xpath("//*[@id="mount_0_0"]/div/div/div[1]/div[2]/div[3]/div/div[1]/div[1]")

driver.find_elements_by_class_name("hu5pjgll lzf7d6o1").click()

#print("count is: listofelements.size()")
#listofelements.send_keys(Keys.RETURN)
#time.sleep(5)'''

nb = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div/div[1]/div[2]/div[4]")
acc = driver.find_element_by_xpath("//*[@id='mount_0_0']/div/div/div[1]/div[2]/div[4]/div[1]/span/div/div[1]/img")
logout = driver.find_element_by_xpath("//*[@id='jsc_c_9w']/div/div/span")

actions = ActionChains(driver)
actions.move_to_element(nb).move_to_element(acc).move_to_element(logout).click().perform()

#driver.close()
