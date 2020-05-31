from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Products:
    def __init__(self, driver):
        self.driver = driver

    first_product = "(//a[@class='a-link-normal a-text-normal'])[1]"

    def getFirstProductFromProductsPage(self):
        return self.driver.find_element_by_xpath(self.first_product)

    def clickFirstSearchedProduct(self):
        self.getFirstProductFromProductsPage().click()

    def isProductDisplayed(self):
        explicit_wait = WebDriverWait(self.driver, 15, 1)
        first_product_locator = (By.XPATH, self.first_product)  # converting string to By locator
        explicit_wait.until(expected_conditions.presence_of_all_elements_located(first_product_locator))
        return self.getFirstProductFromProductsPage().is_displayed()
