from selenium import webdriver as wd
import time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

#This will use the latest updated version of WebDriver
wd = wd.Chrome(ChromeDriverManager().install()) 

#Opens up Google
wd.get('https://google.com') 

#lets user see and loads element
time.sleep(2)
search = wd.find_elements_by_xpath('//*[@id="gb"]/div/div[1]/div/div[2]/a')

#clicks on images
search[0].click()

#Searches "Honda Civics" on the search bar
searchID = wd.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchID.send_keys("Honda Civics")

#Clicks on the search button
searchButton = wd.find_elements_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button')
searchButton[0].click()

#Closes Browser
wd.close() 