from selenium import webdriver
import pytest
import time
from pages.homepage import Home
from pages.productspage import Products


class TestProductDetailsPage:

    @pytest.fixture
    def setUp(self):
        self.driver = webdriver.Chrome(
            "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/resources/drivers/chromedriver")
        self.driver.get("https://www.amazon.in")
        self.driver.maximize_window()
        time.sleep(4)
        yield
        time.sleep(3)
        self.driver.close()
        self.driver.quit()

    def test_website_title(self, setUp):
        self.driver.save_screenshot(
            "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "homepage.png")
        # pageTitle = self.driver.title
        home_object = Home(self.driver)
        pageTitle = home_object.getPageTitle()
        assert pageTitle == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"

    def test_search_functionality(self, setUp):
        # search_box = self.driver.find_element_by_id("twotabsearchtextbox")
        # search_box.send_keys("Macbook pro")
        home_object = Home(self.driver)
        home_object.enterTextIntoSearchBox("Macbook pro")
        self.driver.save_screenshot(
            "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "afterenteringproduct.png")
        # search_icon = self.driver.find_element_by_xpath("//input[@type='submit']")
        # search_icon.click()
        home_object.clickSearchIcon()
        time.sleep(5)
        self.driver.save_screenshot(
            "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "productlisting.png")
        # searched_product = self.driver.find_element_by_xpath("(//a[@class='a-link-normal a-text-normal'])[1]")
        product_page = Products(self.driver)
        assert product_page.isProductDisplayed() == True
