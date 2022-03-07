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


class ConnexionPageTest(LiveServerTestCase):
    def testConnexion(self):
        selenium = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        selenium.get('http://127.0.0.1:8000/accountslogin')
        assert 'Se connecter' in selenium.page_source
        selenium.close()


class RegisterPageTest(LiveServerTestCase):
    def testConnexion(self):
        selenium = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        selenium.get('http://127.0.0.1:8000/accountssignup')
        assert "S'enregistrer" in selenium.page_source
        selenium.close()


class ContactPageTest(LiveServerTestCase):
    def testConnexion(self):
        selenium = webdriver.Chrome(executable_path="C:\chromedriver.exe")
        selenium.get('http://127.0.0.1:8000/contactpage')
        assert "Contactez" in selenium.page_source
        selenium.close()


if __name__ == "__main__":
    unittest.main()
