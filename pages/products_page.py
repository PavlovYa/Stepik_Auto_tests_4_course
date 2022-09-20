from .base_page import BasePage
from .locators import ProductsPageLocators
from selenium import webdriver
import math
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

class ProductsPage(BasePage):

    def add_to_basket(self):
        add_to_basket = self.browser.find_element(*ProductsPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def should_be_correct_add_success_message(self):
        
        book = self.browser.find_element(*ProductsPageLocators.BOOK_NAME)
        bookMessage = self.browser.find_element(*ProductsPageLocators.ADD_SUCCESS_MESSAGE)
        assert bookMessage is book, "Incorrect add success message"

    def should_be_correct_price_message(self):

        price_message = self.browser.find_element(*ProductsPageLocators.PRICE_MESSAGE)
        price = self.browser.find_element(*ProductsPageLocators.PRICE)
        assert price_message is price, "Incorrect price message"

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")