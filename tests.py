from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class HomePageTest(LiveServerTestCase):
    def testdescription(self):
        selenium = webdriver.Chrome()

        # Choose your url to visit
        selenium.get('http://127.0.0.1:8000')
