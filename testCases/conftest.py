import pytest
from utilities.driver_factory import get_driver
import os
from datetime import datetime

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser name")

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("browser")
    driver = get_driver(browser)

    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # only take screenshot on failure
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            if not os.path.exists("screenshots"):
                os.mkdir("screenshots")

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"screenshots/{item.name}_{timestamp}.png"

            driver.save_screenshot(file_name)
