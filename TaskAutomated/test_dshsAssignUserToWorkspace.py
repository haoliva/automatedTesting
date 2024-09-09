import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddWorkspacePage import AddWorkspace
from pageObjects.ConfigureWorkspacePage import ConfigureWorkspace
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_AssignUserToWorkspace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    path = ".//TasksData/user-per-workspace.xlsx"

#    @pytest.mark.regression
#    @pytest.mark.order(15)

    def test_dshsAssignUserToWorkspace(self, setup):
        self.logger.info("****************** dshsAssignUserToWorkspace **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login successful **********************")

        self.logger.info("****************** Starting Open Workspace By URL **********************")

        self.rows = XLUtils.getRowCount(self.path, 'user-per-workspace')
        print("Number of Rows in a Excel:", self.rows)

        for r in range(2, self.rows + 1):
            self.url = XLUtils.readData(self.path, 'user-per-workspace', r, 1)
            self.userName = XLUtils.readData(self.path, 'user-per-workspace', r, 4)

            self.logger.info("****************** Open Workspace Auth area by URL **********************")
            self.logger.info("URL: "+self.url)
            self.driver.get(self.url)
            self.cnfworkspace = ConfigureWorkspace(self.driver)
            time.sleep(5)
            self.cnfworkspace.clickOnAdd()
            time.sleep(1)
            self.cnfworkspace.setUser(self.userName)
            time.sleep(1)
            self.cnfworkspace.clickOnSaveGrant()
            time.sleep(2)

            self.logger.info("*************** Assign User to a Workspace validation started *******************")
            self.body_tagName = "body"
            self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text

            if 'Authorization Granted Successfully' in self.msg:
                assert True
                self.logger.info("********* Assign User to Workspace Test Passed ***************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_assignUserToWorkspace_scr.png")  # Screenshot
                self.logger.error("********* Assign User to Workspace Failed ***************")
                assert False
                break

        self.driver.close()
        self.logger.info("****************** End Test_AssignUserToWorkspace **********************")



