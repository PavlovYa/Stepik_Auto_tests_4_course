from lib2to3.pgen2 import driver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):

        self.browser.get(self.url)
    
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
