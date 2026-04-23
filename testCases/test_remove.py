from pageObjects.login_page import LoginPage
from pageObjects.inventory_page import InventoryPage

def test_remove_from_cart(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart()
    inventory.remove_product()

    assert "Remove" not in driver.page_source