import unittest

from selenium import webdriver

from pageobjects.loginpage import LoginPage


class TestBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(r'C:\Users\Plkkin\AppData\Local\Google\Chrome\Application\chromedriver.exe')
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()


