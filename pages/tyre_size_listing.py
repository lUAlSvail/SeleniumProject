from .base_page import BasePage
from locators.tyre_size_listing_locators import TyreSizeListingLocators
class TyresSizeListing(BasePage):


    def selector_field(self, width, height, diameter):
        if (self.find_element(TyreSizeListingLocators.set_choosen_width(self,width)).is_selected())\
                and (self.find_element(TyreSizeListingLocators.set_choosen_height(self, height)).is_selected())\
                and (self.find_element(TyreSizeListingLocators.set_choosen_diameter(self, diameter)).is_selected()==True):
            return "Correct parameters"
        else:
            return  "Wrong parameters"

