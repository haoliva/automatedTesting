import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddWorkspacePage import AddWorkspace
from pageObjects.ConfigureWorkspacePage import ConfigureWorkspace
from selenium.webdriver.common.by import By

from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_EditLGroupNamesAtWorkspace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    path = ".//TasksData/edit-localGroups.xlsx"

#    @pytest.mark.regression
#    @pytest.mark.order(17)
    def test_dshsEditLGroupNamesAtWorkspace(self, setup):
        self.logger.info("****************** dshsEditLGroupAtWorkspace **********************")
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

        self.rows = XLUtils.getRowCount(self.path, 'edit-lGroup')
        print("Number of Rows in a Excel:", self.rows)

        for r in range(2, self.rows + 1):
            self.url = XLUtils.readData(self.path, 'edit-lGroup', r, 1)
#            self.shortName = XLUtils.readData(self.path, 'users-per-localGroup', r, 2)
            self.groupName = XLUtils.readData(self.path, 'edit-lGroup', r, 3)
#            self.role = XLUtils.readData(self.path, 'users-per-localGroup', r, 5)

            self.cnfworkspace = ConfigureWorkspace(self.driver)

            self.logger.info("************* Open Workspace Auth Group area by URL *****************")
            self.logger.info("URL: " + self.url)
            self.driver.get(self.url)
            time.sleep(3)
            self.logger.info("************* Edit LG Name *****************")
            self.cnfworkspace.editLGroupName(self.groupName)
            time.sleep(2)

            self.cnfworkspace.clickOnSaveGrant()
            time.sleep(3)

            self.logger.info("*************** Edit LG name in a Workspace validation started *******************")
            self.body_tagName = "body"
            self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text

            if 'Local group was saved successfully' in self.msg:
                assert True
                self.logger.info("********* Edit LG name in a Workspace Test Passed ***************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_dshsEditLGroupNamesAtWorkspace.png") # Screenshot
                self.logger.error("********* Edit LG name in a Workspace Failed ***************")
                assert False
                break

        self.driver.close()
        self.logger.info("****************** End Test_EditLGroupNamesAtWorkspace **********************")