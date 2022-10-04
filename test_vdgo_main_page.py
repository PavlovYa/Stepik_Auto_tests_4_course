import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from urllib3 import Timeout
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://dev-brigada.mosoblgaz.ru:81/"

def test_admin_can_login(browser):

    Mainpage = MainPage(browser, link)
    Loginpage = LoginPage(browser, link)
    Loginpage.open()
    Loginpage.admin_login()                    
    Mainpage.should_be_main_page()          

def test_admin_can_create_task(browser):

    Mainpage = MainPage(browser, link)
    Loginpage = LoginPage(browser, link)
    Loginpage.open()
    Loginpage.admin_login()                    
    Mainpage.should_be_main_page() 
    Mainpage.create_button_should_be_clickable() 

# def test_should_be_login_url(browser):

#     Mainpage = MainPage(browser, link)   
#     Loginpage = LoginPage(browser, link)
#     Mainpage.open()                      
#     Mainpage.go_to_login_page()         
#     Loginpage.should_be_login_url()

# def test_should_be_login_form(browser):

#     Mainpage = MainPage(browser, link)   
#     Loginpage = LoginPage(browser, link)
#     Mainpage.open()                      
#     Mainpage.go_to_login_page()
#     Loginpage.should_be_login_form()

# def should_be_register_form(browser):

#     Mainpage = MainPage(browser, link)
#     Loginpage = LoginPage(browser, link)
#     Mainpage.open()
#     Mainpage.go_to_login_page()
#     Loginpage.should_be_register_form()