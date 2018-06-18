from selenium.webdriver import Chrome,Firefox,Ie
import pytest

def get_browser_instance():
    browser_type = pytest.config.option.browser
    env = pytest.config.option.env
    if env == "remote":
        if browser_type == "firefox":
            browser = Firefox(executable_path='e:/geckodriver.exe')
        elif browser_type == "chrome":
            browser = Chrome("e:/chromedriver.exe")
        elif browser_type == "Ie":
            browser = Ie("e:/IEDriverServer.exe")            
    browser.maximize_window()
    browser.implicitly_wait(30)
    browser.get("https://us.castlighthealth.com")
    return browser
        # else:
