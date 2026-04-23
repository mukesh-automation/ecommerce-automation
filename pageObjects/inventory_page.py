from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.base_page import BasePage

class InventoryPage(BasePage):

    add_to_cart_btn = (By.XPATH, "//button[text()='Add to cart']")
    remove_btn = (By.XPATH, "//button[text()='Remove']")
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    add_all_products = (By.CLASS_NAME, 'btn_inventory')

    def add_product_to_cart(self):
        self.click(self.add_to_cart_btn)

    def remove_product(self):
        self.click(self.remove_btn)

    def go_to_cart(self):
        self.click(self.cart_icon)

    def add_multiple_products(self):
        buttons = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.add_all_products))

        for btn in buttons:
               btn.click()