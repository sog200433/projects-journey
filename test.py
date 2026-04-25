import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
link=r"https://secure-retreat-92358.herokuapp.com/"

fill_form=webdriver.ChromeOptions()
keep_open=fill_form.add_experimental_option("detach",True)

FIRST_NAME="Samuel"
LAST_NAME="Garcia"
EMAIL="saw199033@outlook.com"
class Fillform:
    def __init__(self):
        self.driver=webdriver.Chrome(fill_form)
        self.driver.get(link)
        print("opened web succesfully")
        wait=WebDriverWait(self.driver,timeout=10)
        first_name=self.driver.find_element(By.NAME,value="fName")
        print("fname input found")
        last_name=self.driver.find_element(By.NAME,value="lName")
        print("found last name")
        email=self.driver.find_element(By.NAME,value="email")
        print("email input found")
        first_name.send_keys(FIRST_NAME)
        print("filled successfully")
        last_name.send_keys(LAST_NAME)
        print("sent successfully")
        email.send_keys(EMAIL)
        print("sent succesfully")
        sign_up=self.driver.find_element(By.XPATH,'/html/body/form/button')
        sign_up.click()
Fillform()    