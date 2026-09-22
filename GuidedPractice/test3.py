import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_page_title(driver):
    driver.get("https://selenium.dev")
    assert "Selenium" in driver.title