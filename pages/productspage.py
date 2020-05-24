class Products:
    def __init__(self, driver):
        self.driver = driver

    first_product = "(//a[@class='a-link-normal a-text-normal'])[1]"

    def getFirstProductFromProductsPage(self):
        return self.driver.find_element_by_xpath(self.first_product)

    def clickFirstSearchedProduct(self):
        self.getFirstProductFromProductsPage().click()

    def isProductDisplayed(self):
        return self.getFirstProductFromProductsPage().is_displayed()
