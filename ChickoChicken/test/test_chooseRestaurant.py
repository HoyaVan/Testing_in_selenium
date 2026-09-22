from page.page_chooseRestaurant import ChooseRestaurant

# pytest will automatically look for this fixture
def test_choose_restaurant(driver):
    print("TEST STARTED")
    
    page = ChooseRestaurant(driver)

    page.open_page()
    assert "choose_restaurant" in driver.current_url

    typed_city = page.type_city_random()
    assert typed_city in page.TEST_CITIES
    
    selected_city = page.click_first_city_dropdown()
    assert typed_city == selected_city
    
    selected_last_element = page.click_random_order_button()
        
    print(f"""selected_last_element : {selected_last_element}
            Typed City: {typed_city}
            Selected City: {selected_city}""")
    
#--------------------------------Unit Testing--------------------------------------#
# import unittest
# from selenium import webdriver
# from choose_restaurant import ChooseRestaurant


# class ChooseRestaurantTest(unittest.TestCase):

#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.page = ChooseRestaurant(self.driver)

#     def tearDown(self):
#         self.driver.quit()

#     def test_choose_restaurant(self):
#         self.page.open_page()
#         self.assertIn("choose_restaurant", self.driver.current_url)

#         selected_city = self.page.enter_city_random()
#         self.assertIn(selected_city, self.page.TEST_CITIES)

#         selected_index = self.page.click_random_order_button()
#         self.assertGreaterEqual(selected_index, 0)

#         print(selected_city)


# if __name__ == "__main__":
#     unittest.main()