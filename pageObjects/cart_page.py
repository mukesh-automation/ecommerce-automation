from selenium.webdriver.common.by import By
from pageObjects.base_page import BasePage

class CartPage(BasePage):

    checkout_btn = (By.ID, "checkout")

    def click_checkout(self):
        self.click(self.checkout_btn)


