import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def setup(browser):

    if browser == 'chrome':
        options = Options()
        options.add_argument("start-maximized")
        s = Service('C:/Users/haoli/PycharmProjects/Tools/chromedriver.exe')
        driver = webdriver.Chrome(service=s, options=options)
        #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("Launching Chrome browser...........")
    elif browser == 'firefox':
        profile_path = r'C:\Users\xxx\AppData\Roaming\Mozilla\Firefox\Profiles\v5ymq8by.default'
        options = Options()
        options.set_preference('profile', profile_path)
        options.accept_insecure_certs = True

        driver = webdriver.Firefox(options=options)

        print("Launching Firefox browser...........")
    else:
        driver = webdriver.Edge()

    driver.maximize_window()
    return driver

def pytest_addoption(parser):       # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):           # This will return the Browser value to setup method
    return request.config.getoption("--browser")


##################### PyTest HTML Report #####################################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'BConView'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'H Oliva'

# It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionlhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)