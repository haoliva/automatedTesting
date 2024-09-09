import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddWorkspacePage import AddWorkspace
from pageObjects.ConfigureWorkspacePage import ConfigureWorkspace
from selenium.webdriver.common.by import By

from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_CreateFilterAtWorkspace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    path = ".//TasksData/hrData-filters-per-workspace.xlsx"

#    @pytest.mark.regression
#    @pytest.mark.order(17)
    def test_dshsCreateFilterAtWorkspace(self, setup):
        self.logger.info("****************** dshsCreateFilterAtWorkspace **********************")
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

        self.rows = XLUtils.getRowCount(self.path, 'filter-per-workspace')
        print("Number of Rows in a Excel:", self.rows)

        for r in range(2, self.rows + 1):
            self.url = XLUtils.readData(self.path, 'filter-per-workspace', r, 1)
            self.dept1 = XLUtils.readData(self.path, 'filter-per-workspace', r, 3)
            self.filterName = XLUtils.readData(self.path, 'filter-per-workspace', r, 4)
            self.resourceType = XLUtils.readData(self.path, 'filter-per-workspace', r, 5)
            self.employeeID = XLUtils.readData(self.path, 'filter-per-workspace', r, 6)
            self.firstName = XLUtils.readData(self.path, 'filter-per-workspace', r, 7)
            self.lastName = XLUtils.readData(self.path, 'filter-per-workspace', r, 8)
            self.deptID = XLUtils.readData(self.path, 'filter-per-workspace', r, 9)
            self.workspace = XLUtils.readData(self.path, 'filter-per-workspace', r, 10)
            self.sortBy = XLUtils.readData(self.path, 'filter-per-workspace', r, 12)

            self.cnfworkspace = ConfigureWorkspace(self.driver)

            self.logger.info("************* Open Workspace Filter area by URL *****************")
            self.logger.info("URL: " + self.url)
            self.driver.get(self.url)

            self.cnfworkspace.clickOnAdd()    # click to add a new filter
            self.logger.info("****************** Add New Filter **********************")
            self.cnfworkspace.setFilterName(self.filterName)
            self.cnfworkspace.setResourceType(self.resourceType)
            time.sleep(1)
            self.cnfworkspace.clickOnAddResType()
            time.sleep(1)

            for t in range(1,5):
                self.logger.info("****************** Adding fields to the filter **********************")
                if t == 1:
                    self.cnfworkspace.setFilterFields(self.employeeID)
                elif t == 2:
                    self.cnfworkspace.setFilterFields(self.firstName)
                elif t == 3:
                    self.cnfworkspace.setFilterFields(self.lastName)
                elif t == 4:
                    self.cnfworkspace.setFilterFields(self.deptID)
                self.cnfworkspace.clickOnAddFilterField()

            self.cnfworkspace.setWorkspace(self.workspace)
            time.sleep(2)
            self.cnfworkspace.setLookupScope()
            time.sleep(1)
            self.cnfworkspace.clickOnAddCondition()
            time.sleep(1)
            self.cnfworkspace.setFieldOnCondition(self.deptID)
            time.sleep(1)
            self.cnfworkspace.setCondition()
            time.sleep(1)
            self.cnfworkspace.setWhereStatement(self.dept1)
            time.sleep(1)
            self.cnfworkspace.setSortByOption(self.sortBy)
            time.sleep(1)
            self.cnfworkspace.clickOnAddForSorting()
            time.sleep(1)

            self.cnfworkspace.clickOnSaveFilter()
            time.sleep(3)

            status = self.cnfworkspace.searchFilterByFilterName(self.filterName)
            time.sleep(1)
            #        print("status:" + str(status))

            if status:
                assert True
                self.logger.info("*************** Create Filter in a Workspace validation started *******************")
                self.body_tagName = "body"
                self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text
                if 'The filter has been enabled successfully' in self.msg:
                    self.logger.info("************* Creating Filter At Workspace passed *********************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_createFilterAtWorkspace.png")
                self.logger.error("************* Creating Filter At Workspace failed *********************")
                assert False

        self.driver.close()
        self.logger.info("****************** End Test_CreateLGroupAtWorkspace **********************")