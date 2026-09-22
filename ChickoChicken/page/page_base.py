from abc import ABC, abstractmethod

import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(ABC):
    
    def __init__(self, driver):
        self.driver = driver
    
    @abstractmethod
    def open_page(self):
        pass
    
    # WAIT until at least ONE visible element exists first(max 10sec), 
    # THEN fetch clean data again
    def get_visible_elements(self, locator):
        elements = WebDriverWait(self.driver, 10).until(
            lambda d: [e for e in d.find_elements(*locator)
                    if e.is_displayed()]
        )
        assert len(elements) > 0, "No visible elements found"
        return elements
        
    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    # Use if you want to use locator works with class name
    def click_element_by_index(self, locator, index):
        elements = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(locator)
        )
        text = elements[index].text.strip()
        elements[index].click()
        return text
    
    def click_random_element(self, locator):
        elements = self.get_visible_elements(locator)
        element = random.choice(elements)
        text = element.text.strip()
        element.click()
        return text

    def type_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)
        return text
        
    def type_text_random_list(self, locator, text_list):
        assert len(text_list) > 0, "Text list is empty"
        
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )
        
        random_text = random.choice(text_list)
        self.type_text(locator, random_text)
        return random_text

    # def click_random_element(self, locator):
    #     elements = WebDriverWait(self.driver, 10).until(
    #         EC.presence_of_all_elements_located(locator)
    #     )
    #     assert len(elements) > 0, "No elements found"
    #     random_index = random.randint(0, len(elements) - 1)
    #     elements[random_index].click()
    #     return random_index
    