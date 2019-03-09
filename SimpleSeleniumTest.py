"""
To Write Simple selinium test - Open Browser
navigating to QA Interview page
Entering Integer Value and closing the Browser
"""

from selenium import webdriver
import time
#Creating instance of Browser
#Navigating to QA interview page
#Verify the title off the page

class sim_Sel_test():

    def setup(self):
        self.browser = webdriver.Firefox()
        self.browser.get("https://qainterview.pythonanywhere.com/")
        if (self.browser.title == "Factoriall"):
            print("QA interview page Matching title")
        else:
            self.browser.close()
            print("Not Matching title")
    def testfactorial(self):
        self.name = self.browser.find_element_by_xpath("//input[@type='text']")
        self.button = self.browser.find_element_by_xpath("//button[@type='submit']")
        self.name.send_keys(5)
        self.button.click()
        time.sleep(2)
    def testtermslink(self):
        self.link = self.browser.find_element_by_xpath("//a[text()='Terms and Conditions']")
        self.link.click()
        self.privacy = self.browser.find_element_by_xpath("//body[text()='This is the privacy document. We are not yet ready with it. Stay tuned!']")
        print(self.privacy.text)
        if (self.privacy.text == 'This is the privacy document. We are not yet ready with it. Stay tuned!'):
            self.browser.get("https://qainterview.pythonanywhere.com/")
            self.link1 = self.browser.find_element_by_xpath("//a[text()='Privacy']")
            self.link1.click()
            self.privacy1 = self.browser.find_element_by_xpath("//body[text()='This is the terms and conditions document. We are not yet ready with it. Stay tuned!']")
            print(self.privacy1.text)
            
    def testprivacylink(self):
        if (self.privacy1.text == 'This is the terms and conditions document. We are not yet ready with it. Stay tuned!'):
            self.browser.get("https://qainterview.pythonanywhere.com/")
            self.browser.close()
        else:   
            self.browser.close()

if __name__ == "__main__":
    s1 = sim_Sel_test()
    s1.setup()
    s1.testfactorial()
    s1.testtermslink()
    s1.testprivacylink()
        

        



