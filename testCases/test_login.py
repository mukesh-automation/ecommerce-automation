from pageObjects.login_page import LoginPage
from utilities.logger import get_logger
from utilities.read_config import get_base_url, get_username, get_password

logger = get_logger()

def test_view_login(driver):
    driver.get(get_base_url())
    logger.info("Starting login test")

    login = LoginPage(driver)
    login.login(get_username(), get_password())

    logger.info("Login successful")

    assert "inventory" in driver.current_url