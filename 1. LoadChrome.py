from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)
search_bar = driver.find_element("name","q")
search_bar.send_keys("abc")
#search_bar.clear()
#search_bar.submit()
search_bar.send_keys(Keys.RETURN)
