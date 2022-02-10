from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome
import unittest


class HomePageTest(LiveServerTestCase):
    def testdescription(self):
        selenium = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        # Choose your url to visit
        selenium.get('http://127.0.0.1:8000/')
        assert 'Remy' in selenium.page_source
        selenium.close()


if __name__ == "__main__":
    unittest.main()
