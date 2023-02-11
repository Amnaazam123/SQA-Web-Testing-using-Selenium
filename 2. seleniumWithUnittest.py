from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

driver = webdriver.Chrome()

class pythonOrgSearch(unittest.TestCase):
        def setUp(self):
            print("setup")
            driver.get("https://www.python.org")
            
        def test_search(self):
            self.assertIn("Python",driver.title)
            search_bar = driver.find_element("name","q")  # search_bar contains name="q".
            search_bar.send_keys("pycon")           # writing pycon in search bar
            search_bar.send_keys(Keys.RETURN)       # pressing enter
            assert "No result found" not in driver.page_source
            
        def tearDown(self):
            print("teardown")
            driver.close();
          
         
suite = unittest.TestSuite()
suite.addTest(pythonOrgSearch("test_search"))
unittest.TextTestRunner().run(suite)
