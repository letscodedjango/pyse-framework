from selenium import webdriver
import time
import pytest


@pytest.fixture(scope="class")
def setUpDriver():
    driver = webdriver.Chrome(
        "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/resources/drivers/chromedriver")
    driver.get("https://www.amazon.in")
    driver.maximize_window()
    time.sleep(4)
    yield
    time.sleep(3)
    driver.close()
    driver.quit()
