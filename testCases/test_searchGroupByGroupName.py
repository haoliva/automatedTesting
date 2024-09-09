import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddGroupPage import AddGroup
from pageObjects.SearchGroupPage import SearchGroup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_007_SearchGroupByGroupName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    @pytest.mark.regression
    @pytest.mark.order(7)
    def test_searchGroupByGroupName(self, setup):
        self.logger.info("****************** Test_007_SearchGroupByGroupName **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
#        self.driver.implicitly_wait(30)
        self.logger.info("****************** Login successful **********************")

        self.logger.info("****************** Starting Search Group By GroupName **********************")

        self.addGroup = AddGroup(self.driver)
        self.addGroup.clickOnAdministrationMenu()
        self.addGroup.clickOnSecAdminMenu()
        self.addGroup.clickOnGroupsItem()

#        self.driver.implicitly_wait(30)

        self.logger.info("****************** Searching Group By GroupName **********************")
        self.searchgroup = SearchGroup(self.driver)
        self.searchgroup.setSearch("Automation Group")
        time.sleep(5)
        status = self.searchgroup.searchGroupByGroupName("Automation Group", "edit")
        time.sleep(5)
#        print("status:" + str(status))

        if status:
            assert True
            self.driver.close()
            self.logger.info("************* Searching Group By GroupName is passed *********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchGroupByGroupName.png")
            self.driver.close()
            self.logger.error("************* Searching Group By GroupName is failed *********************")
            assert False

        self.logger.info("****************** Test_007_SearchGroupByGroupName Finished **********************")

