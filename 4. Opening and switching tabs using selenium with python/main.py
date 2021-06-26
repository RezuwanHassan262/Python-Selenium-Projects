from  selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\\Users\\user\\PycharmProjects\\OpeningAndSwitchingTabsUsingSelenium\\Drivers\\chromedriver.exe")
driver.get("http://www.google.com")
time.sleep(2)
driver.maximize_window()
time.sleep(2)

driver.execute_script("window.open('');") #Opening new tab
driver.switch_to.window(driver.window_handles[1]) #Switching to new tab
driver.get("https://brainstation-23.com")
time.sleep(5)

driver.execute_script("window.open('');") #Opening new tab
driver.switch_to.window(driver.window_handles[2]) #Switching to new tab
driver.get("https://www.linkedin.com")
time.sleep(5)

driver.execute_script("window.open('');") #Opening new tab
driver.switch_to.window(driver.window_handles[3]) #Switching to new tab
driver.get("http://www.facebook.com")
time.sleep(5)

driver.execute_script("window.open('');") #Opening new tab
driver.switch_to.window(driver.window_handles[4]) #Switching to new tab
driver.get("https://stackoverflow.com/")
time.sleep(5)

driver.execute_script("window.open('');") #Opening new tab
driver.switch_to.window(driver.window_handles[5]) #Switching to new tab
driver.get("https://github.com/")
time.sleep(5)

#SerialSwitchingBetweenTabs
driver.switch_to.window(driver.window_handles[0]) #Switching to new tab
time.sleep(2)
driver.switch_to.window(driver.window_handles[1]) #Switching to new tab
time.sleep(2)
driver.switch_to.window(driver.window_handles[2]) #Switching to new tab
time.sleep(2)
driver.switch_to.window(driver.window_handles[3]) #Switching to new tab
time.sleep(2)
driver.switch_to.window(driver.window_handles[4]) #Switching to new tab
time.sleep(2)
driver.switch_to.window(driver.window_handles[5]) #Switching to new tab
time.sleep(2)

#RandomSwitchingBetweenTabs
driver.switch_to.window(driver.window_handles[3]) #Switching to new tab
time.sleep(2)
driver.switch_to.window(driver.window_handles[2]) #Switching to new tab
time.sleep(2)
driver.switch_to.window(driver.window_handles[5]) #Switching to new tab
time.sleep(2)
driver.switch_to.window(driver.window_handles[1]) #Switching to new tab
time.sleep(2)
driver.switch_to.window(driver.window_handles[4]) #Switching to new tab
time.sleep(2)
driver.switch_to.window(driver.window_handles[0]) #Switching to new tab
time.sleep(2)

driver.quit()