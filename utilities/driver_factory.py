from selenium import webdriver

def get_driver(browser):

    if browser == "chrome":
        return webdriver.Chrome()

    elif browser == "edge":
        return webdriver.Edge()

    else:
        raise Exception("Browser not supported")