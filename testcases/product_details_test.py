from selenium import webdriver
import pytest
import time
from pages.homepage import Home
from pages.productdetailspage import ProductDetails
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

    def test_product_title(self, setUp):
        self.driver.save_screenshot(
            "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "homepage.png")
        home_object = Home(self.driver)
        home_object.enterTextIntoSearchBox("Macbook pro")
        self.driver.save_screenshot(
            "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "afterenteringproduct.png")
        home_object.clickSearchIcon()
        time.sleep(5)
        self.driver.save_screenshot(
            "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "productlisting.png")

        parent_window = self.driver.current_window_handle
        print(parent_window)

        product_page = Products(self.driver)
        product_page.clickFirstSearchedProduct()

        time.sleep(3)
        windows_set = self.driver.window_handles
        print(windows_set)

        for window in windows_set:
            if (window != parent_window):
                self.driver.switch_to.window(window)
                self.driver.save_screenshot(
                    "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "childtab.png")

        product_detail_object = ProductDetails(self.driver)
        assert product_detail_object.getProductTitle() == "Macbook pro"

    def test_product_price(self, setUp):
        self.driver.save_screenshot(
            "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "homepage.png")
        home_object = Home(self.driver)
        home_object.enterTextIntoSearchBox("Macbook pro")
        self.driver.save_screenshot(
            "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "afterenteringproduct.png")
        home_object.clickSearchIcon()
        time.sleep(5)
        self.driver.save_screenshot(
            "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "productlisting.png")

        parent_window = self.driver.current_window_handle
        print(parent_window)

        product_page = Products(self.driver)
        product_page.clickFirstSearchedProduct()

        time.sleep(3)
        windows_set = self.driver.window_handles
        print(windows_set)

        for window in windows_set:
            if (window != parent_window):
                self.driver.switch_to.window(window)
                self.driver.save_screenshot(
                    "/Users/gaurnitai/Desktop/Programming/Python/PySeFramework/screenshots/" + "childtab.png")

        product_detail_object = ProductDetails(self.driver)
        product_price = product_detail_object.getProductPrice()

        assert product_price == "₹ 1,27,990.00"
