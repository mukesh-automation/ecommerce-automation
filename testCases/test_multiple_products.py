from selenium.webdriver.common.by import By

from pageObjects.login_page import LoginPage
from pageObjects.inventory_page import InventoryPage

def test_add_multiple_products(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_multiple_products()

    assert driver.find_elements(By.XPATH, "//button[normalize-space()='Remove']")