import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddWorkspacePage import AddWorkspace
from pageObjects.ConfigureWorkspacePage import ConfigureWorkspace
from pageObjects.AddBIAdataPage import AddBIAdata
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_022_AddDataToBIA:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    @pytest.mark.regression
    @pytest.mark.order(21)
    def test_addDataToBIA(self, setup):
        self.logger.info("****************** Test_022_AddDataToBIA **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(30)
        self.logger.info("****************** Login successful **********************")

        self.logger.info("****************** Starting Search Workspace By WSName **********************")

        self.addWorkspace = AddWorkspace(self.driver)
        self.addWorkspace.clickOnAdministrationMenu()
        self.addWorkspace.clickOnOrgAdmMenu()
        self.addWorkspace.clickOnWorkspacesItem()

        self.logger.info("****************** Searching Workspace By WSName **********************")
        self.cnfworkspace = ConfigureWorkspace(self.driver)
        #self.cnfworkspace.setSearch("North Region")
        self.cnfworkspace.setSearch("Biochemistry")

        time.sleep(5)
        self.cnfworkspace.contextClick()

        self.addbiadata = AddBIAdata(self.driver)
        self.addbiadata.clickOnViewWorkspace()
        time.sleep(2)
        self.addbiadata.clickOnWorkBIA()
        time.sleep(2)
        self.addbiadata.clickOnChangesAnticipated()
        time.sleep(2)
        self.addbiadata.clickOnReleased()
        time.sleep(2)
        self.addbiadata.clickOnWorking()
        time.sleep(2)
        self.addbiadata.clickOnAdd()
        time.sleep(2)
        self.addbiadata.setAnticipatedChanges("Anticipated Change added by Automation Testing")
        self.addbiadata.setFinOperBusImpacts("Financial and Operations Business Impacts added by Automation Testing")
        self.addbiadata.setDiscussionIssues("Discussion Issues added by Automation Testing")
        time.sleep(1)
        self.addbiadata.clickOnSave()
        time.sleep(2)
        self.addbiadata.clickOnWorking1()
        self.addbiadata.clickOnReleased1()
        time.sleep(2)

        self.driver.close()
        self.logger.info("****************** End Test_022_AddDataToBIA **********************")