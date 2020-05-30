from selenium import webdriver
import time
import pytest
import logging

@pytest.fixture(scope="class")
def OneTimeSetUp(request):
    logging.debug("Intializing the chrome driver....")
    driver = webdriver.Chrome(
        "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/resources/drivers/chromedriver")
    logging.debug("Launcing the amazon website....")
    driver.get("https://www.amazon.in")
    logging.debug("Maximizing the browser window....")
    driver.maximize_window()
    time.sleep(4)
    request.cls.driver = driver
    yield driver
    time.sleep(3)
    logging.debug("Closing the browser window....")
    driver.close()
    logging.debug("Quiting the chrome driver....")
    driver.quit()


@pytest.fixture(scope="class")
def SetUp(request):
    driver = webdriver.Chrome(
        "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/resources/drivers/chromedriver")
    driver.get("https://www.amazon.in")
    driver.maximize_window()
    time.sleep(4)
    request.cls.driver = driver
    yield driver
    time.sleep(3)
    driver.close()
    driver.quit()
