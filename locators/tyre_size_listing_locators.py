from selenium.webdriver.common.by import By

class TyreSizeListingLocators():
    def set_choosen_width(self,value):
        return (By.XPATH,("//select[@name=\"Width\"]/option[@value=\"{}\"]").format(value))

    def set_choosen_height(self,value):
        return (By.XPATH,("//select[@name=\"CrossSections\"]/option[@value=\"{}\"]").format(value))

    def set_choosen_diameter(self,value):
        return (By.XPATH,("//select[@name=\"Size\"]/option[@value=\"{}\"]").format(value))
