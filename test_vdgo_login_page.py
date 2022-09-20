import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from urllib3 import Timeout
# from .pages.main_page import MainPage
from .pages.login_page import LoginPage

link = "http://dev-brigada.mosoblgaz.ru:81/"

def test_should_be_login_field(browser):

    LoginPage = LoginPage(browser, link)   
    LoginPage.open()                      
    LoginPage.should_be_login_field()          

def test_should_be_pass_field(browser):

    LoginPage = LoginPage(browser, link)   
    LoginPage.open()                      
    LoginPage.should_be_pass_field()

# def test_guest_should_see_login_link(browser):

#     Mainpage = MainPage(browser, link)
#     Mainpage.open()
#     Mainpage.should_be_login_link()

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