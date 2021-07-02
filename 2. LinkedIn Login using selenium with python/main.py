from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(r"C:\\Users\\user\\PycharmProjects\\LinkedInLogin\\Drivers\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("LinkedIn login")
driver.find_element_by_name("q").send_keys(Keys.ENTER)
driver.find_element_by_partial_link_text("LinkedIn Login").click()
driver.find_element_by_id("username").send_keys("*YOUR MAIL ADDRESS*")
driver.find_element_by_id("password").send_keys("*YOUR PASSWORD*")
driver.find_element_by_tag_name("button").click()
print(driver.title)
print(driver.current_url)
driver.quit()
