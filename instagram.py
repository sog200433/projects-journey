import selenium
print("selenium is installed")
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
SIMILAR_ACCOUNT="https://www.instagram.com/iliatopuria/"
USERNAME="saw199033"
PASSWORD="Tpri9801$"

chrome_options=webdriver.ChromeOptions()
additional=chrome_options.add_experimental_option("detach",True)


class InstaFollower:
    def __init__(self):
        print("opening chrome")
    
        self.driver=webdriver.Chrome(options=chrome_options)

        print("webpage loaded succesfully")
       

    def login(self):
        try:
            self.driver.get("https://www.instagram.com/accounts/login/")
            print("waiting for username element")
            # Wait for the login form to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME ,"email")
            ))
            print("element found")
            user = self.driver.find_element(By.NAME,value="email")
            print("found username")
            password = self.driver.find_element(By.NAME,value="pass")
            print("found password")
            user.send_keys(USERNAME)
            print("filled username")
            password.send_keys(PASSWORD)
            print("password filled")
            login = self.driver.find_element(By.XPATH,value='//*[@id="login_form"]/div/div[1]/div/div[3]/div/div/div/div[1]/div/span/span')
            print("login button found")
            login.click()
            cookie=self.driver.find_element(By.XPATH,'//*[@id="mount_0_0_MM"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/section/div/button')
            print("cookie has been found")
            cookie.click()
            time.sleep(6)
        except Exception as e:
            print(f"Error: {e}")
       

    def find_followers(self):
        pass
    def follow(self):
        pass
insta=InstaFollower()
print("instance created")
insta.login()