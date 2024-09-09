import pytest
import time

from pageObjects.AddRolePage import AddRole
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchRolePage import SearchRole
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_012_SearchRoleByRoleDescAndEdit:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    @pytest.mark.regression
    @pytest.mark.order(12)
    def test_searchRoleByRoleDesc(self, setup):
        self.logger.info("****************** Test_012_SearchRoleByRoleDescAndEdit **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login successful **********************")

        self.logger.info("*************** Starting Search Role By Role Description and Edit it ******************")

        self.addRole = AddRole(self.driver)
        self.addRole.clickOnAdministrationMenu()
        self.addRole.clickOnSecAdminMenu()
        self.addRole.clickOnRolesItem()

        self.logger.info("****************** Searching Group By Role Desc **********************")
        self.searchrole = SearchRole(self.driver)
        self.searchrole.setSearch("Automation Role - App Read Access")
        time.sleep(5)
        status = self.searchrole.searchRoleByRoleDesc("Automation Role - App Read Access")
        time.sleep(5)
#        print("status:" + str(status))

        if status:
            assert True
            self.addRole.clickOnApplication()
            self.addRole.clickOnDashboardReadPermission()
            self.addRole.clickOnSave()
            self.driver.close()
            self.logger.info("************* Searching Role By Role Desc and Edit is passed *********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchRoleByRoleDescAndEdit.png")
            self.driver.close()
            self.logger.error("************* Searching Role By Role Desc and Edit is failed *********************")
            assert False

        self.logger.info("****************** Test_012_SearchRoleByRoleDescAndEdit Finished **********************")

