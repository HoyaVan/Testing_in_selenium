from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait # wait
from selenium.webdriver.support import expected_conditions as EC # wait
import unittest
import time # bad practice

class GooglePageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_getGooglePage(self):
        self.driver.get("https://www.google.com")
        assert "Google" in self.driver.title
    
    def test_typeGoogleSearchBar(self):
        self.driver.get("https://www.google.com")
        
        search_bar = self.driver.find_element(By.NAME, "q")
        search_bar.send_keys("google" + Keys.ENTER)
        
        result = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "MjjYud"))
        ) # wait upto 3 sec, if it founds the element before then the test moves on right away
        
        found_text = "Google"
        expected_text = result.text
        
        self.assertEqual(found_text, expected_text) 
    
    def tearDown(self):
        self.driver.quit()
        print("Done")
    
if __name__=='__main__':
    unittest.main()

