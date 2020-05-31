from selenium.webdriver.common.by import By


class GoogleSearchLocators:

    SEARCH_FIELD = (By.XPATH, "//input[@role=\"combobox\"][@type=\"text\"]")
    SEARCH_BUTTON = (By.XPATH, "//form/child::div/div/div/center/input[@type=\"submit\"]")
    PASSIVE = (By.XPATH,"//div/img[@alt=\"Google\"]")