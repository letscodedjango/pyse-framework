class Home:

    def __init__(self, driver):
        self.driver = driver

    search_box = "twotabsearchtextbox"
    search_icon = "//input[@type='submit']"

    def getSearchBox(self):
        return self.driver.find_element_by_id(self.search_box)

    def getSearchIcon(self):
        return self.driver.find_element_by_xpath(self.search_icon)

    def enterTextIntoSearchBox(self, product_name):
        self.getSearchBox().send_keys(product_name)

    def clickSearchIcon(self):
        self.getSearchIcon().click()

    def getPageTitle(self):
        return self.driver.title
