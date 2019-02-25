from selenium.webdriver import Chrome, Firefox, Ie
import pytest

# url= "https://us.castlighthealth.com/"

def get_browser_instance():
    browser_type = pytest.config.option.browser
    env = pytest.config.option.env
    url = pytest.config.option.url

    if env == "remote":
        if browser_type == "firefox":
            browser = Firefox(executable_path='e:/geckodriver.exe')
        elif browser_type == "chrome":
            browser = Chrome(executable_path='e:/chromedriver.exe')
        elif browser_type == "Ie":
            browser = Ie(executable_path='e:/IEDriverServer.exe')
    browser.maximize_window()
    browser.get(url)
    return browser
    # else
