class ProductDetails:

    def __init__(self, driver):
        self.driver = driver

    product_title = "productTitle"
    product_price = "priceblock_ourprice"

    def getProductTitleFromProductDetailPage(self):
        return self.driver.find_element_by_id(self.product_title)

    def getProductPriceFromProductDetailPage(self):
        return self.driver.find_element_by_id(self.product_price)

    def getProductTitle(self):
        return self.getProductTitleFromProductDetailPage().text

    def getProductPrice(self):
        return self.getProductPriceFromProductDetailPage().text
