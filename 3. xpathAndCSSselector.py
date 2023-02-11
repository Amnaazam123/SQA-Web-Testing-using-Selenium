from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)


# Xpath method to locate elements in web.

# search_bar = driver.find_element(By.XPATH, "//input[@name='q']")
# search_bar = driver.find_element(By.CSS_SELECTOR, "input[name='q']")
# search_bar = driver.find_element(By.CLASS_NAME,"gLFyf")
# search_bar = driver.find_element(By.ID,"gLFyf")
# search_bar = driver.find_element(By.NAME,"q")
# search_bar = driver.find_element(By.XPATH,"//input[@name='q'][@type='text']")
# search_bar = driver.find_element(By.CSS_SELECTOR,"input[name='q'][type='text']")


# to access the third field of form
# first_field = driver.find_element(By.XPATH, "/html/body/form/input[2]")
# print(first_field)

button = driver.find_element(By.XPATH,"//button[@id='myButton']")
button.click()
button = driver.find_element(By.XPATH,"//a[text()='click me']")
button.click()



#several CSS selectors
search_bar = driver.find_element(By.CSS_SELECTOR, "#elementID")
search_bar = driver.find_element(By.CSS_SELECTOR, ".elementClass")
search_bar = driver.find_element(By.CSS_SELECTOR, "p")
search_bar = driver.find_element(By.CSS_SELECTOR, "input[name='q']")
search_bar = driver.find_element(By.CSS_SELECTOR, "p:first-child")
email = driver.find_element(By.CSS_SELECTOR, "input#email")
inputs_with_prefix = driver.find_element(By.CSS_SELECTOR,"input[name^='sub']")
inputs_with_suffix = driver.find_element(By.CSS_SELECTOR,"input[name$='mit']")
inputs_with_substring = driver.find_element(By.CSS_SELECTOR,"input[name*='bmi']")
password_input = driver.find_element(By.CSS_SELECTOR,"input#password[name^='pass']")




    


