import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddWorkspacePage import AddWorkspace
from pageObjects.ConfigureWorkspacePage import ConfigureWorkspace
from selenium.webdriver.common.by import By

from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_AddUsersToLGroupAtWorkspace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    path = ".//TasksData/users-per-localGroup.xlsx"

#    @pytest.mark.regression
#    @pytest.mark.order(17)
    def test_dshsAddUsersToLGroupAtWorkspace(self, setup):
        self.logger.info("****************** dshsAddUsersToLGroupAtWorkspace **********************")
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

        self.rows = XLUtils.getRowCount(self.path, 'users-per-localGroup')
        print("Number of Rows in a Excel:", self.rows)

        for r in range(2, self.rows + 1):
            self.url = XLUtils.readData(self.path, 'users-per-localGroup', r, 1)
#            self.shortName = XLUtils.readData(self.path, 'users-per-localGroup', r, 2)
            self.userName = XLUtils.readData(self.path, 'users-per-localGroup', r, 4)
#            self.role = XLUtils.readData(self.path, 'users-per-localGroup', r, 5)

            self.cnfworkspace = ConfigureWorkspace(self.driver)

            self.logger.info("************* Open Workspace Auth Group area by URL *****************")
            self.logger.info("URL: " + self.url)
            self.driver.get(self.url)
            time.sleep(3)
#
#            self.logger.info("****************** Update LG Name **********************")
#            if self.role == "Admins":
#                v_groupName = "Admins of this workspace ("+self.shortName+")"
#            elif self.role == "Editors":
#                v_groupName = "Editors of this workspace (" + self.shortName + ")"

#            self.cnfworkspace.editLGroupName(v_groupName)
#            time.sleep(1)

            self.logger.info("****************** Add user to LG **********************")
            self.cnfworkspace.clickOnAddUserLG()
            time.sleep(1)
            v_user = "//div[contains(text(),"+"'"+self.userName+"')]"
            print(v_user)
            self.cnfworkspace.setUserInLG(v_user)

            self.cnfworkspace.clickOnAddMember()
            time.sleep(2)

            self.cnfworkspace.clickOnSaveGrant()
            time.sleep(3)

            self.logger.info("*************** Add user to LG in a Workspace validation started *******************")
            self.body_tagName = "body"
            self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text

            if 'Local group was saved successfully' in self.msg:
                assert True
                self.logger.info("********* Add user to LG in a Workspace Test Passed ***************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_addUserToLGroupAtWorkspace_scr.png") # Screenshot
                self.logger.error("********* Add User at LG in a Workspace Failed ***************")
                assert False
                break

        self.driver.close()
        self.logger.info("****************** End Test_AddUsersToLGroupAtWorkspace **********************")