import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddWorkspacePage import AddWorkspace
from pageObjects.ConfigureWorkspacePage import ConfigureWorkspace
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_020_RemoveLGroupFromWorkspace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    @pytest.mark.regression
    @pytest.mark.order(19)
    def test_removeLGroupFromWorkspace(self, setup):
        self.logger.info("****************** Test_020_RemoveLGroupFromWorkspace **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login successful **********************")

        self.logger.info("****************** Starting Search Workspace By WSName **********************")

        self.addWorkspace = AddWorkspace(self.driver)
        self.addWorkspace.clickOnAdministrationMenu()
        self.addWorkspace.clickOnOrgAdmMenu()
        self.addWorkspace.clickOnWorkspacesItem()

        self.logger.info("****************** Searching Workspace By WSName **********************")
        self.cnfworkspace = ConfigureWorkspace(self.driver)
        self.cnfworkspace.setSearch("Automation Testing")
        time.sleep(5)
        self.cnfworkspace.contextClick()
        self.cnfworkspace.clickOnConfigureWorkspace()
        time.sleep(2)
        self.cnfworkspace.clickOnManageGroups()
        time.sleep(1)
        self.cnfworkspace.clickOnLocalGroups()
        time.sleep(1)

        self.cnfworkspace.clickOnRemoveGroup()
        time.sleep(2)

        self.logger.info("*************** Remove Local Group from a Workspace validation started *******************")
        self.body_tagName = "body"
        self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text

        if 'Local group was removed successfully' in self.msg:
            assert True
            self.logger.info("********* Remove Local Group from a Workspace Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_removeLGroupFromWorkspace_scr.png")  # Screenshot
            self.logger.error("********* Remove Local Group from Workspace Test Failed ***************")
            assert False

        self.driver.close()
        self.logger.info("****************** End Test_020_RemoveLGroupFromWorkspace **********************")