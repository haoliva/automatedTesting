import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.order(1)
    def test_homePageTitle(self, setup):
        self.logger.info("****************** Test_001_Login **********************")
        self.logger.info("************* Verifying Home Page Title ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "BConView":
            assert True
            self.driver.close()
            self.logger.info("************* Home Page Title test passed *********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************* Home Page Title test is failed *********************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("************* Verifying Login test  *********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(30)
#        home_ready = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.lp.home()))
#        home_ready = self.lp.home()
#        if home_ready.is_displayed():
#            assert True
#        else:
#            assert False
        self.lp.logout()
        self.driver.close()
