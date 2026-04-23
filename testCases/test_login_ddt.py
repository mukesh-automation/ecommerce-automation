import pytest
from pageObjects.login_page import LoginPage
from utilities.excel_reader import get_data
from selenium.webdriver.common.by import By

data = get_data("testData/testdata.xlsx", "Sheet1")

@pytest.mark.parametrize("username,password,expected", data)
def test_login_ddt(driver, username, password, expected):

    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.login(username, password)

    if expected == "success":
        assert "inventory" in driver.current_url

    else:
        error = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert error.is_displayed()