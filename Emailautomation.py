"""
E-Mail program
"""
import time
from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class setUP():

    
    def openbrowser(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.tle = self.driver.title
        if (self.tle == self.driver.title):
            self.driver.get("https://login.yahoo.com/")
            self.enterlogindetails()
        else:
            print("Not on the right page")
            self.driver.close()
    
    def enterlogindetails(self):
        self.usr_name = self.driver.find_element_by_xpath("//input[@id='login-username']")
        self.usr_name.send_keys('raghava_n@yahoo.com')
        self.usr_button = self.driver.find_element_by_xpath("//input[@value='Next']")
        self.usr_button.click()
        time.sleep(1)
        
        #self.usr_pwd = self.driver.find_element_by_xpath("//input[@id='login-passwd']")
        #print(self.usr_pwd)
        #self.usr_pwd.send_keys("ragattribute")
        
        #self.element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"login-passwd")))
        #self.element.send_keys("ragattribute")

        self.tle1 = self.driver.title
        if (self.tle1 == self.driver.title):
            self.element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,"login-passwd")))
            self.element.send_keys("ragattribute")
            self.usr_button1 = self.driver.find_element_by_xpath("//button[@id='login-signin']")
            self.usr_button1.click()
            self.mail = self.driver.find_element_by_xpath("//span[text()='Mail']")
            self.mail.click()
            self.comp = self.driver.find_element_by_xpath("//a[text()='Compose']")
            self.comp.click()
            self.toadd = self.driver.find_element_by_xpath("//input[@id='message-to-field']")
            self.toadd.send_keys("raghava.nelabhotla@gmail.com")
            #self.sub = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.NAME,"Subject")))
            #self.sub = self.driver.find_element_by_xpath("//input[@data-test-id='compose-suject']")
            #self.sub.send_keys("Test Mail")
            self.sub = self.driver.find_element_by_xpath("//input[@aria-label='Subject']")
            self.sub.send_keys("Test Mail")
            self.msg = self.driver.find_element_by_xpath("//div[@aria-label='Message body']")
            self.msg.send_keys("This is Test Mail for Automation test")
            self.senmail = self.driver.find_element_by_xpath("//button[@data-test-id='compose-send-button']")
            self.senmail.click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//span[text()='Raghava']").click()
            time.sleep(2)
            self.logout = self.driver.find_element_by_xpath("//a[contains(@href,'/logout')]").click()
                  
            #self.driver.name.click()
            #self.signout = self.driver.find_element_by_xpath("//span[text()='Sign out']")
            #self.signout.click()
            #time.sleep(1)
            #self.driver.close()
            
                      
#//span[text()='Sign out']
#//span[text()='Raghava']
        else:
            print("Bye")

if __name__ == "__main__":
    s1 = setUP()
    s1.openbrowser()