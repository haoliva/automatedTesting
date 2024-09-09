import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddBIAdataPage import AddBIAdata
from selenium.webdriver.common.by import By

from utilities import XLUtils
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_ActivateFilterAtWorkspace_OoS:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    path = ".//TasksData/inputSections-HR-filters-per-workspace.xlsx"

#    @pytest.mark.regression
#    @pytest.mark.order(17)
    def test_dshsActivateFilterAtWorkspace_OoS(self, setup):
        self.logger.info("****************** dshsActivateFilterAtWorkspace **********************")
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

        self.rows = XLUtils.getRowCount(self.path, 'inpSection-per-workspace')
        print("Number of Rows in a Excel:", self.rows)

        for r in range(2, self.rows + 1):
            self.url = XLUtils.readData(self.path, 'inpSection-per-workspace', r, 1)

            self.addBIA = AddBIAdata(self.driver)

            self.logger.info("************* Open Workspace BIA area by URL *****************")
            self.logger.info("URL: " + self.url)
            self.driver.get(self.url)

            self.addBIA.clickOnNew()    # click on New
            time.sleep(1)
            self.addBIA.clickOnWorking()  # click on Working
            time.sleep(1)
            self.addBIA.clickOnAdd()  # click on Add
            time.sleep(5)

            filters = 0
            x = range(1, 5)
            for t in x:
                if t == 1:
                    self.addBIA.clickOnFilterNotSelected_1()
                elif t == 2:
                    self.addBIA.clickOnFilterNotSelected()
                elif t == 3:
                    self.addBIA.clickOnFilterNotSelected_5()
                elif t == 4:
                    self.addBIA.clickOnFilterNotSelected_2()

                time.sleep(1)
                self.addBIA.clickOnSelectAFilter()
                time.sleep(1)
                self.addBIA.clickOnFilter()
                time.sleep(1)
                self.addBIA.clickOnOk()
                time.sleep(3)
                self.body_tagName = "body"
                self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text

                if 'Filter information updated successfully' in self.msg:
                    filters += 1

#                print("Filters activated:", filters)

#            self.body_tagName = "body"
#            self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text
            #        print(self.msg)
            if filters == 4:
                assert True
                self.logger.info("********* Activate a Filter at Workspace OoS Passed ***************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_activateFilter_OoS_scr.png")  # Screenshot
                self.logger.error("********* Activate a Filter at Workspace OoS Failed ***************")
                assert False

            time.sleep(1)
            self.addBIA.clickOnCloseForm()
            time.sleep(1)
            self.addBIA.clickOnWorking1()
            time.sleep(1)
            self.addBIA.clickOnReleased()
            time.sleep(1)

        self.driver.close()
        self.logger.info("****************** End test_dshsActivateFilterAtWorkspace_OoS **********************")