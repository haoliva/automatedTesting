import pytest
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        #version = "116_0_5845_0"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = "C:/Users/haoli/PycharmProjects/Tools/chrome-win64/chrome.exe"


        chrome_driver_path = "C:/Users/haoli/PycharmProjects/Tools/chromedriver.exe"
        service_options = webdriver.ChromeService(executable_path=chrome_driver_path)

        driver = webdriver.Chrome(options=chrome_options, service=service_options)

        #driver.maximize_window()

        print("Launching Chrome browser...........")
    elif browser == 'firefox':
        profile_path = r'C:\Users\haoli\AppData\Roaming\Mozilla\Firefox\Profiles\v5ymq8by.default'
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