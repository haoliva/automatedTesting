import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddWorkspacePage import AddWorkspace
from pageObjects.ConfigureWorkspacePage import ConfigureWorkspace
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_CreateRolesAtWorkspace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    path = ".//TasksData/roles-per-workspace.xlsx"

#    @pytest.mark.regression
#    @pytest.mark.order(15)

    def test_dshsCreateRolesAtWorkspace(self, setup):
        self.logger.info("****************** dshsCreateRolesAtWorkspace **********************")
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

        self.rows = XLUtils.getRowCount(self.path, 'roles-per-workspace')
        print("Number of Rows in a Excel:", self.rows)

        for r in range(2, self.rows + 1):
            self.url = XLUtils.readData(self.path, 'roles-per-workspace', r, 1)
            self.role1 = XLUtils.readData(self.path, 'roles-per-workspace', r, 2)
            self.desc1 = XLUtils.readData(self.path, 'roles-per-workspace', r, 3)
            self.role2 = XLUtils.readData(self.path, 'roles-per-workspace', r, 4)
            self.desc2 = XLUtils.readData(self.path, 'roles-per-workspace', r, 5)

            self.cnfworkspace = ConfigureWorkspace(self.driver)

            x = range(1, 3)
            for t in x:
                self.logger.info("****************** Open Workspace Auth area by URL **********************")
                self.logger.info("URL: "+self.url)
                self.driver.get(self.url)

                time.sleep(3)
                if t == 1:
                    self.logger.info("****************** Add Workspace Admin Role **********************")
                    self.cnfworkspace.setRoleName(self.role1)
                    self.cnfworkspace.setRoleDesc(self.desc1)
                    time.sleep(1)
                    self.cnfworkspace.clickOnWsWrite()
                elif t == 2:
                    self.logger.info("****************** Add Workspace Editor Role **********************")
                    self.cnfworkspace.setRoleName(self.role2)
                    self.cnfworkspace.setRoleDesc(self.desc2)
                    time.sleep(1)
                    self.cnfworkspace.clickOnExpandWS()
                    time.sleep(1)
                    self.cnfworkspace.clickOnComponentsWrite()

                time.sleep(1)
                self.cnfworkspace.clickOnSaveGrant()
                time.sleep(3)

                self.logger.info("*************** Create Role in a Workspace validation started *******************")
                self.body_tagName = "body"
                self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text

                if 'Role saved successfully' in self.msg:
                    assert True
                    self.logger.info("********* Create Role in a Workspace Test Passed ***************")
                else:
                    self.driver.save_screenshot(".\\Screenshots\\" + "test_createRoleAtWorkspace_scr.png")  # Screenshot
                    self.logger.error("********* Create a Role in a Workspace Failed ***************")
                    assert False
                    break

                if t == 2:
                    if self.cnfworkspace.getRoleTableNoOfRows() != 3:
                        break

        self.driver.close()
        self.logger.info("****************** End Test_Create Role at a Workspace **********************")



