import unittest
from selenium import webdriver


class SeleniumTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.addCleanup(self.driver.quit)

    def test_page_title(self):
        self.driver.get("https://selenium.dev")
        self.assertIn("Selenium", self.driver.title)