'''hello! this is an instagram  bot that automatically comments on people's post using hashtags
you can simple put your instagram username and passwordand choose your hashtag that you want to comment in and then just
wait for your likes and nteractions coming back to your account
this way is way better then doing it manually, this will alsosave a ot of time serfing instagrm and work by yourself, guys feel free
to use the code but tag my name soeverything will be ok'''

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import webbrowser
import random

PATH = "write here the path to webdriver on yor pc"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")
driver.delete_all_cookies()


#wait then execute
driver.implicitly_wait(5)

# username & password
userName = driver.find_element_by_name("username").send_keys("write username here")
passWord = driver.find_element_by_name("password")
passWord.send_keys("write password here")
passWord.send_keys(Keys.RETURN)
time.sleep(5)
save = driver.find_element_by_css_selector('.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm').click()
# notnow button
notnow= driver.find_element_by_css_selector('.aOOlW.HoLwm').click()
time.sleep(2)
def searchhashandlike(hashtag):
    driver.get(f'https://www.instagram.com/explore/tags/{hashtag}/')
    picture= driver.find_elements_by_css_selector("._9AhH0")
    picture[0].click()
    for i in range(0, 100):
        #like = driver.find_elements_by_css_selector('svg[aria-label="Like"]')
        #like[0].click()
        time.sleep(1)
        comment_btn= driver.find_element_by_css_selector('svg[aria-label="Comment"]')
        comment_btn.click()
        
        add_comment= driver.find_element_by_css_selector('.Ypffh')
        add_comment.send_keys('nice shot, you might follow my content')
        add_comment.send_keys(Keys.ENTER)
        
        #post_comment = driver.find_element_by_css_selector('.sqdOP.yWX7d.y3zKF')
        #post_comment.click()
        time.sleep(1)
        nextwindow = driver.find_element_by_css_selector('._65Bje.coreSpriteRightPaginationArrow')
        nextwindow.click()
        time.sleep(2)
        time.sleep(random.randint(2, 10)) # this make a random pause between each action so that you will not be banned , make sure it's between ('1,10") or graeter
searchhashandlike('cute')# here you replace 'cute' with the hashtag that you want to comment on 

'''making actions
action = ActionChains(driver)
action.click(userName)
action.click(passWord)
action.perform() '''

    

    
