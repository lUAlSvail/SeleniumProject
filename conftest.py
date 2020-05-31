import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path='/home/svail/PycharmProjects/drivers/chromedriver')
    driver.maximize_window()
    yield driver
    driver.quit()