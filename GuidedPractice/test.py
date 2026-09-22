from selenium import webdriver
## from selenium.webdriver.common.by import By
import unittest
import time

""" 
# non-class test

driver = webdriver.Chrome()

driver.get("https://selenium.dev/documentation")
assert "Selenium" in driver.title
time.sleep(2)

elem = driver.find_element(By.ID, "m-documentationwebdriver")
elem.click()
assert "WebDriver" in driver.title

driver.quit()

print("Done")
"""

class SeleniumTestOfficialHomepage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def testGetPage(self):
        self.driver.get("https://selenium.dev/documentation")
        assert "Selenium" in self.driver.title
        time.sleep(2) # not an ideal way
    
    # def testGetElementDocumentation(self):
    #     elem = self.driver.find_element(By.ID, "m-documentationwebdriver")
    #     elem.click()
    #     assert "WebDriver" in self.driver.title
    
    def testGetElementLinkText(self):
        self.driver.get("https://www.selenium.dev/documentation/")
        elem = self.driver.find_element(By.PARTIAL_LINK_TEXT, "WebDriver")
        elem.click()
        assert "WebDriver" in self.driver.title
    
    def tearDown(self):
        self.driver.quit()
        print("Done")
    
if __name__=='__main__':
    unittest.main()

