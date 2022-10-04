from lib2to3.pgen2 import driver
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from .base_page import BasePage
from .locators import MainPageLocators

browser = webdriver.Chrome()

class MainPage(BasePage): 

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click() 

    def should_be_main_page(self):
        assert self.is_element_present(*MainPageLocators.LOGO), "Not Main Page after login"

    def create_button_should_be_clickable(self):
        browser.implicitly_wait(5)
        assert self.is_element_present(*MainPageLocators.TASK), "There is no Create button"
        # MainPageLocators.TASK.click()
