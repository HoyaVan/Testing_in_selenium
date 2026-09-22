from selenium.webdriver.common.by import By
from page.page_base import BasePage as BP
from selenium import webdriver
import pytest

class ChooseRestaurant(BP):
    
    TEST_CITIES = [
        "Vancouver", "Burnaby", "Coquitlam", "Richmond",
        "Surrey", "Langley", "New Westminster", "Port Coquitlam",
        "North Vancouver", "Kelowna", "Edmonton", "Kamloops", "Prince George",
        "Tronto", "Grande Prairie", "Vernon", "Okotoks", "Airdrie", "Medicine Hat",
        "Quesnel"
    ]
    
    URL = "https://chickochicken.ca/choose_restaurant"

    CITY_INPUT = (By.NAME, "city")
    ORDER_BUTTON = (By.CSS_SELECTOR, "span.order")
    CITY_DROPDOWN = (By.CLASS_NAME, "title")
    
    # inheritance from Base Page (abstract class)
    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self):
        self.driver.get(self.URL)

    def type_city(self, city):
        return self.type_text(self.CITY_INPUT, city)
                
    def click_first_order_button(self):
        return self.click_element_by_index(self.ORDER_BUTTON, 0)
        
    def click_first_city_dropdown(self):
        return self.click_element_by_index(self.CITY_DROPDOWN, 0)

    # 'Return' random values when the test needs to know what was chosen.
    def type_city_random(self):
        return self.type_text_random_list(self.CITY_INPUT, self.TEST_CITIES)

    def click_random_drop_down_city(self):
        return self.click_random_element(self.CITY_DROPDOWN)
    
    def click_random_order_button(self):
        return self.click_random_element(self.ORDER_BUTTON)
