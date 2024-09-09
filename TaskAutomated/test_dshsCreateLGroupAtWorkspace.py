import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddWorkspacePage import AddWorkspace
from pageObjects.ConfigureWorkspacePage import ConfigureWorkspace
from selenium.webdriver.common.by import By

from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_CreateLGroupAtWorkspace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    path = ".//TasksData/localGroups-per-workspace.xlsx"

#    @pytest.mark.regression
#    @pytest.mark.order(17)
    def test_createLGroupAtWorkspace(self, setup):
        self.logger.info("****************** dshsCreateLGroupAtWorkspace **********************")
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

        self.rows = XLUtils.getRowCount(self.path, 'lg-per-workspace')
        print("Number of Rows in a Excel:", self.rows)

        for r in range(2, self.rows + 1):
            self.url = XLUtils.readData(self.path, 'lg-per-workspace', r, 1)
            self.group1 = XLUtils.readData(self.path, 'lg-per-workspace', r, 4)
            self.desc1 = XLUtils.readData(self.path, 'lg-per-workspace', r, 5)
            self.group2 = XLUtils.readData(self.path, 'lg-per-workspace', r, 6)
            self.desc2 = XLUtils.readData(self.path, 'lg-per-workspace', r, 7)

            self.cnfworkspace = ConfigureWorkspace(self.driver)

            x = range(1, 3)
            for t in x:
                self.logger.info("************* Open Workspace Auth Group area by URL *****************")
                self.logger.info("URL: " + self.url)
                self.driver.get(self.url)

                time.sleep(3)
                if t == 1:
                    self.logger.info("****************** Add Admin LG **********************")
                    self.cnfworkspace.setLGroupName(self.group1)
                    self.cnfworkspace.setLGroupDescription(self.desc1)
                elif t == 2:
                    self.logger.info("****************** Add Editor LG **********************")
                    self.cnfworkspace.setLGroupName(self.group2)
                    self.cnfworkspace.setLGroupDescription(self.desc2)

                time.sleep(1)
                self.cnfworkspace.clickOnAddGrantLG()
                time.sleep(1)
                if t == 1:
                    self.cnfworkspace.setAdminRoleInLGroup()
                elif t == 2:
                    self.cnfworkspace.setEditorRoleInLGroup()

                time.sleep(1)
                self.cnfworkspace.clickOnSaveGrantLG()
                time.sleep(2)

                self.cnfworkspace.clickOnSaveGrant()
                time.sleep(3)

                self.logger.info("*************** Create LG in a Workspace validation started *******************")
                self.body_tagName = "body"
                self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text

                if 'Local Group created' in self.msg:
                    assert True
                    self.logger.info("********* Create LG in a Workspace Test Passed ***************")
                else:
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_createLGroupAtWorkspace_scr.png")  # Screenshot
                    self.logger.error("********* Create a LG in a Workspace Failed ***************")
                    assert False
                    break

                if t == 2:
                    if self.cnfworkspace.getRoleTableNoOfRows() != 3:
                        break

        self.driver.close()
        self.logger.info("****************** End Test_CreateLGroupAtWorkspace **********************")