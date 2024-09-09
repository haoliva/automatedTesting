import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddWorkspacePage import AddWorkspace
from pageObjects.ConfigureWorkspacePage import ConfigureWorkspace
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_024_CreateInputSectionInAComponent:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    @pytest.mark.regression
    @pytest.mark.order(24)
    def test_createInputSectionInAComponent(self, setup):
        self.logger.info("****************** Test_024_CreateInputSectionInAComponent **********************")
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
        self.cnfworkspace.clickOnWorkspaceComponents()
        time.sleep(2)
        self.body_tagName = "body"

        self.logger.info("*************** Create an Input Section in BIA Component started *******************")

        self.cnfworkspace.searchAndSelectInputs("BIA Implementation")
        time.sleep(3)
        self.cnfworkspace.clickOnAddSection()
        time.sleep(1)
        self.cnfworkspace.clickOnSave()
        time.sleep(2)

        self.body_tagName = "body"
        self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text

        if 'Successfully created section' in self.msg:
            assert True
            self.logger.info("********* Create an Input Section Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addInputSection_scr.png")  # Screenshot
            self.logger.error("********* Create an Input Section Test Failed ***************")
            assert False

#        self.cnfworkspace.clickOnCloseSections()
        self.driver.close()
        self.logger.info("****************** End Test_024_CreateInputSectionInAComponent *******************")

