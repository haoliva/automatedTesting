import pytest
import time

#import requests
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.OrgSetupPage import OrgSetup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_021_OrgSetupForm:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()

    password = ReadConfig.getPassword()


    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.order(20)
    def test_orgSetupForm(self, setup):
        self.logger.info("****************** Test_021_OrgSetupPage **********************")
        self.driver = setup

        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login successful **********************")

        self.logger.info("****************** Starting Org Setup Form Test **********************")

        self.orgSetup = OrgSetup(self.driver)
        self.orgSetup.clickOnAdministrationMenu()
        self.orgSetup.clickOnOrgAdmMenu()
        self.orgSetup.clickOnOrgSetupItem()
        time.sleep(2)

        self.logger.info("****************** Providing pagination information **********************")

        self.orgSetup.setPagination()

        self.orgSetup.clickOnSave()

        self.logger.info("****************** Saving Organization information **********************")

        self.logger.info("****************** Org Setup validation started **********************")

        self.body_tagName = "body"
        time.sleep(1)
        self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text

        if 'saved successfully' in self.msg:
            assert True
            self.logger.info("********* Org Setup Form Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_orgSetupForm_scr.png")  # Screenshot
            self.logger.error("********* Org Setup Form Test Failed ***************")
            assert False

        self.driver.close()
        self.logger.info("****************** End Test_021_OrgSetupForm **********************")
