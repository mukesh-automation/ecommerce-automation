from pageObjects.login_page import LoginPage
from pageObjects.inventory_page import InventoryPage
from pageObjects.cart_page import CartPage

def test_add_to_cart(driver):
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    assert "checkout" in driver.current_url