from selenium.webdriver.common.by import By

class MainTyresLocators():

    COOKIES = (By.XPATH,"//div[@class=\"block-cookies__close\"]")
    TYRES_WIDTH = (By.CSS_SELECTOR,"select#form_Width")
    TYRES_HEIGHT = (By.CSS_SELECTOR,"select#form_CrossSections")
    TYRES_DIAMETER = (By.CSS_SELECTOR,"select#form_Size")
    SEARCH_BUTTON_TYRES = (By.CSS_SELECTOR, "a#tyres_search")

    def size_value(self,type_size,value):
        return (By.XPATH,("//select[@id=\"{}\"]//option[@value=\"{}\"]").format(type_size,value))