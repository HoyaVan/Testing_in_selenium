import random

from selenium.webdriver.common.by import By
from page.page_base import BasePage as BP

class ChooseRestaurant(BP):
    
    TEST_LOCATION = [
        "Vernon", "Kelowna (Lakeshore)", "Kelowna (Downtown Ellis)",
        "Vancouver (Robson)", "Vancouver (Joyce)", "Vancouver (Kingsway)",
        "Burnaby (Market Crossing)", "Burnaby (Edmonds)", "Burnaby (Hastings)",
        "Coquitlam", "Richmond", "Surrey (Fleetwood)", "Langley (Aldergrove)",
        "New Westminster (Sapperton)", "Port Coquitlam", "North Vancouver", 
        "White Rock", "Edmonton", "Markham"
    ]
    
    URL = "https://chickochicken.ca/dashboard/home"

    LOCATION_INPUT = (By.LINK_TEXT, "TEST_LOCATION")
    ORDER_BUTTON = (By.CLASS_NAME, "order")
    PICKUP_AT_BUTTON = (By.CLASS_NAME, "")

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.URL)
        assert "Selenium" in driver.title
        
    def click_location(self, city):
        city_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOCATION_INPUT)
        )
        city_input.clear()
        city_input.send_keys(city)

    def click_pickUpAt(self):
        self.click_element(self.PICKUP_AT_BUTTON)
        self.click_element(self.ORDER_BUTTON)
    