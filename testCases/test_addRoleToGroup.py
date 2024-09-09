import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddGroupPage import AddGroup
from pageObjects.SearchGroupPage import SearchGroup
from pageObjects.ViewEditGroupPage import EditGroup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_008_AddRoleToGroup:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    @pytest.mark.regression
    @pytest.mark.order(8)
    def test_addRoleToGroup(self, setup):
        self.logger.info("****************** Test_008_AddRoleToGroup **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.driver.implicitly_wait(30)
        self.logger.info("****************** Login successful **********************")

        self.logger.info("****************** Starting Adding Role to a Group **********************")

        self.addGroup = AddGroup(self.driver)
        self.addGroup.clickOnAdministrationMenu()
        self.addGroup.clickOnSecAdminMenu()
        self.addGroup.clickOnGroupsItem()

        self.logger.info("****************** Adding Role to a Group **********************")
        self.searchgroup = SearchGroup(self.driver)
        self.searchgroup.setSearch("Automation Group")
        time.sleep(5)
        status = self.searchgroup.searchGroupByGroupName("Automation Group", "edit")
        time.sleep(5)
#        print("status:" + str(status))

        self.editGroup = EditGroup(self.driver)
        self.editGroup.clickOnAddSystemRole()
        self.editGroup.clickOnSelectRole()
        self.editGroup.clickOnSystemRole()
        self.editGroup.clickOnSaveRole()
        time.sleep(2)
        self.editGroup.clickOnSave()

        self.logger.info("****************** Saving group information **********************")

        self.logger.info("****************** Edit Group validation started **********************")

        self.element = self.driver.find_element(by=By.CLASS_NAME, value="toast-message")

        self.body_tagName = "body"
        self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text
        #        print(self.msg)
        if 'Group successfully saved' in self.msg:
            assert True
            self.logger.info("********* Edit group Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_editGroup_scr.png")  # Screenshot
            self.logger.error("********* Edit group Test Failed ***************")
            assert False

        #        print(self.msg)

        self.driver.close()
        self.logger.info("****************** End Test_008_AddRoleToGroup **********************")