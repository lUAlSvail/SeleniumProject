from .base_page import BasePage
from locators.main_tyres_locators import MainTyresLocators
from .tyre_size_listing import TyresSizeListing
class MainTyresPage(BasePage):

    def close_cookies(self):
        self.find_element(MainTyresLocators.COOKIES).click()
        return MainTyresPage
    def set_width(self,width):
        self.find_element(MainTyresLocators.TYRES_WIDTH).click()
        self.find_element(MainTyresLocators.size_value(self, "form_Width", width)).click()
        return MainTyresPage

    def set_height(self,height):
        self.find_element(MainTyresLocators.TYRES_HEIGHT).click()
        self.find_element(MainTyresLocators.size_value(self,"form_CrossSections",height)).click()
        return MainTyresPage

    def set_diameter(self,diameter):
        self.find_element(MainTyresLocators.TYRES_DIAMETER).click()
        self.find_element(MainTyresLocators.size_value(self, "form_Size", diameter)).click()
        return MainTyresPage

    def default_search(self,width,height,diameter):
        self.set_width(width)
        self.set_height(height)
        self.set_diameter(diameter)
        self.find_element(MainTyresLocators.SEARCH_BUTTON_TYRES).click()
        return TyresSizeListing

