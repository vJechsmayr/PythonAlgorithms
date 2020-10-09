from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time
import sys
import  random

class InstagramBot() :
    def __init__(self,username,password):
        self.username = username
        self.password = password
        # CHANGE THE LOCATION OF CHROMEDRIVER BELOW #
        self.driver = webdriver.Chrome("D:\chromedriver\chromedriver.exe")

    def closeBrowser(self):
        self.driver.close()

    def Login(self):
        driver = self.driver
        driver.get("https://instagram.com")
        time.sleep(2)

        login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')

        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.send_keys(self.username)

        time.sleep(2)

        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.send_keys(self.password)
        # password_elem.send_keys(Keys.ENTER)
        time.sleep(3)

        login_button.click()

        time.sleep(5)

        not_now = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        not_now.click()
        
        notification_not_now=driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        notification_not_now.click()

    def go_home(self):
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a")\
        .click()
        time.sleep(3)
        self.search = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        self.search.send_keys("###PROFILE TO LIKE POSTS####")
        self.driver.implicitly_wait(3)
        name=self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a')
        name.click()
        self.driver.implicitly_wait(18)
        self.like()
    def like(self):
        self.driver.implicitly_wait(4)
        time.sleep(2)
        start = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div[3]")
        
        a=0
        self.driver.execute_script('arguments['+str(a)+'].scrollIntoView()',start)
        
        for i in range(10):
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            sleep(3)
            pics=self.driver.find_elements_by_class_name("v1Nh3")
            sleep(1)
            for p in pics:
                if(a==0):
                    p.click()
                    self.driver.implicitly_wait(4)
                like=self.driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[3]/section[1]/span[1]/button")
                like.click()
                time.sleep(2)
                if(a==0):
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a").click()
                else:
                    self.driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/a[2]").click()
                a+=1
                print(a)

    def FollowWithUsername(self,username):
        self.driver.get('https://www.instagram.com/' + username + '/')

        time.sleep(3)

        follow_button = self.driver.find_element_by_css_selector('button')
        follow_button.click()
        time.sleep(2)
    
        self.driver.back()
        time.sleep(2)



    def UnFollowWithUsername(self,username):
        self.driver.get('https://www.instagram.com/' + username + '/')

        time.sleep(2)

        follow_button = self.driver.find_element_by_class_name("_5f5mN")
        follow_button.click()

        time.sleep(2)
        unfollow = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[1]")
        unfollow.click()
        time.sleep(2)



username = 'username'
password = 'password'

ig = InstagramBot(username, password)
ig.Login()
time.sleep(2)
ig.FollowWithUsername('abcnews')
time.sleep(2)
ig.UnFollowWithUsername('abcnews')
time.sleep(2)
ig.go_home()
ig.closeBrowser()