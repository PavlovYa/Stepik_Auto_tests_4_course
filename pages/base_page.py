import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class BasePage():

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):

        self.browser.get(self.url)