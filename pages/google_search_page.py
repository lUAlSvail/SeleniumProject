from locators.google_search_locators import GoogleSearchLocators
from .base_page import BasePage

class GoogleSearchPage(BasePage):

    def enter_search_word(self,whatYouSearch):
        search_field = self.find_element(GoogleSearchLocators.SEARCH_FIELD)
        search_field.send_keys(whatYouSearch)
        passive_click = self.find_element(GoogleSearchLocators.PASSIVE)
        passive_click.click()
        search_button = self.find_element(GoogleSearchLocators.SEARCH_BUTTON)
        self.visibility_element(GoogleSearchLocators.SEARCH_BUTTON)
        search_button.click()



        return GoogleSearchPage


