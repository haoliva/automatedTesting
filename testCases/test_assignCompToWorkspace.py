import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddWorkspacePage import AddWorkspace
from pageObjects.ConfigureWorkspacePage import ConfigureWorkspace
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_014_AssignCompToWorkspace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    @pytest.mark.regression
    @pytest.mark.order(14)
    def test_assignCompToWorkspace(self, setup):
        self.logger.info("****************** Test_014_AssignCompToWorkspace **********************")
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

        self.logger.info("*************** Assign Components to a Workspace validation started *******************")

#        self.cnfworkspace.clickOnFemaBCPComponentToggle()

        self.cnfworkspace.searchAndEnableComponent("FEMA BCP")
        time.sleep(1)
        self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text
        bcp_pass = component_validation(self.msg)

#        self.cnfworkspace.clickOnBIAComponentToggle()
        self.cnfworkspace.searchAndEnableComponent("BIA Implementation")
        time.sleep(1)
        self.msg = 0
        self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text
        bia_pass = component_validation(self.msg)

        test_pass = 0
        test_pass = bcp_pass + bia_pass

        if test_pass == 2:
            self.logger.info("********* Assign Components to a Workspace Test Passed ***************")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_assignCompToWorkspace_scr.png")  # Screenshot
            self.logger.error("********* Assign Cmp to a workspace Test Failed ***************")
            assert False

        self.driver.close()
        self.logger.info("****************** End Test_014_AssignCompToWorkspace **********************")


def component_validation(msg):
    if 'Successfully added Component' in msg:
        return 1
    else:
        return 0


