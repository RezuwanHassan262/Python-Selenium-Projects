from selenium import webdriver
import time
channel_id = '/user/programmingwithmosh' #channel id
driver = webdriver.Chrome(r"C:\\Users\\user\\PycharmProjects\\YoutubeRankCheckBot\\Drivers\\chromedriver.exe")
driver.get("http://youtube.com")
driver.maximize_window()

search_bar = driver.find_element_by_id("search")
search_bar.send_keys("React JS") #Inserting text input in a automation way
search_button = driver.find_element_by_id("search-icon-legacy")
search_button.click()

time.sleep(5)


video_list = driver.find_elements_by_xpath('//a[@class="style-scope ytd-video-renderer"]') #Gives all the element of 'a' tag
#print(video_list)
video_url = [video_list.get_attribute('href').replace('https://www.youtube.com', '') for video_list in video_list] #Finds all the href elements or the complete video urls from the "video_list" list, replaces the "https://www.youtube.com" part and extracting into video_url
#print(video_url)

for index, channel in enumerate(video_url): #Enumerate with video_url
    if channel == channel_id:
        print("Video rank: ", index+1) #Index+1 because index starts from 0
        print("Note: Playlist's doesn't count")
        break #We just want to see the first rank number, Not all the other ones
