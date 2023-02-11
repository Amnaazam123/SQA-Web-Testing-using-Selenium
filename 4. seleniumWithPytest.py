import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    print("setup")
    driver=webdriver.Chrome()
    yield driver
    print("teardown")
    driver.quit()

def test_search(browser):
    browser.get("https://www.google.com")
    search_bar = browser.find_element(By.NAME,"q")
    search_bar.send_keys("hello")
    
