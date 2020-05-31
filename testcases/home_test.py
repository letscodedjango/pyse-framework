import random
import datetime

from selenium import webdriver
import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.homepage import Home
from pages.productspage import Products
import logging


# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL


@pytest.mark.usefixtures("OneTimeSetUp")
class TestProductDetailsPage:
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
                        filename='test_execution.log',
                        filemode='w')

    # define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    # set a format which is simpler for console use
    formatter = logging.Formatter('%(asctime)s %(name)-12s: %(levelname)-8s %(message)s')
    # tell the handler to use this format
    console.setFormatter(formatter)
    # add the handler to the root logger
    logging.getLogger('').addHandler(console)

    # @pytest.fixture
    # def setUp(self):
    #     self.driver = webdriver.Chrome(
    #         "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/resources/drivers/chromedriver")
    #     self.driver.get("https://www.amazon.in")
    #     self.driver.maximize_window()
    #     time.sleep(4)
    #     yield
    #     time.sleep(3)
    #     self.driver.close()
    #     self.driver.quit()

    @pytest.fixture
    def setUp(self):
        logging.debug("Taking screenshot before test execution...")
        self.driver.save_screenshot(
            "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" +
            str(time.time()).split('.')[0] + ".png")
        yield
        logging.info("Taking screenshot after test execution...")
        self.driver.save_screenshot(
            "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" +
            str(time.time()).split('.')[0] + ".png")

    def test_website_title(self, setUp):
        # self.driver.save_screenshot("/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "homepage.png")
        # pageTitle = self.driver.title
        home_object = Home(self.driver)
        logging.info("Getting the page title...")
        pageTitle = home_object.getPageTitle()
        logging.info("Comparing the page title with expected title...")
        assert pageTitle == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"

    def test_search_functionality(self, setUp):
        # search_box = self.driver.find_element_by_id("twotabsearchtextbox")
        # search_box.send_keys("Macbook pro")
        home_object = Home(self.driver)
        logging.info("Entering the text into serch box....")
        home_object.enterTextIntoSearchBox("Macbook Pro")
        # self.driver.save_screenshot("/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "afterenteringproduct.png")
        # search_icon = self.driver.find_element_by_xpath("//input[@type='submit']")
        # search_icon.click()
        logging.debug("Clicking on serch icon....")
        home_object.clickSearchIcon()
        # self.driver.save_screenshot("/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "productlisting.png")
        # searched_product = self.driver.find_element_by_xpath("(//a[@class='a-link-normal a-text-normal'])[1]")

        product_page = Products(self.driver)
        logging.info("Checking the searched product ...")
        assert product_page.isProductDisplayed() == True
