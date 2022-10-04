from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGO = (By.CSS_SELECTOR, "#root > div > div > div.header > div.client-logo")
    CREATE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/div[3]/div[1]/div/div[2]/div[1]/div[1]')
    TASK = (By.CSS_SELECTOR, "#root > div > div > div.view-content > div.view-list-wrapper > table > tbody > tr:nth-child(1)")
class LoginPageLocators():
    LOGIN_FIELD = (By.CSS_SELECTOR, "#root > div > div.content > form > div:nth-child(2) > div.input-block > input")
    PASS_FIELD = (By.CSS_SELECTOR, "#root > div > div.content > form > div:nth-child(3) > div.input-block > input[type=password]")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#root > div > div.content > form > div.login-btn-block > div")

class ProductsPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BOOK_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    ADD_SUCCESS_MESSAGE = (By.CSS_SELECTOR, '//*[@id="messages"]/div[1]/div/strong')
    PRICE_MESSAGE = (By.CSS_SELECTOR, '//*[@id="messages"]/div[3]/div/p[1]/strong')
