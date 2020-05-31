
from nose.tools import assert_true


from pages.google_search_page import GoogleSearchPage
from pages.main_tyres_page import MainTyresPage
from pages.tyre_size_listing import TyresSizeListing

class TestSuite():

    def test_google(self,browser):
        google_page = GoogleSearchPage(browser)
        google_page.go_to_site("https://google.com/")
        google_page.enter_search_word("gbsfo")


    def test_selector(self,browser):
        main_tyres_page = MainTyresPage(browser)
        tyre_size_listing = TyresSizeListing(browser)
        main_tyres_page.go_to_site("https://tyres.buycarparts.co.uk/")
        main_tyres_page.close_cookies()
        main_tyres_page.default_search("215","40","16")
        assert_true(tyre_size_listing.selector_field("215","40","16"), "Correct parameters")
