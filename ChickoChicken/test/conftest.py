import pytest
from selenium import webdriver

# Before yield  = setup
# yield driver  = give driver to the test
# After yield   = cleanup after the test finishes
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()
    