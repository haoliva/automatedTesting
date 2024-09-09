import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddGroupPage import AddGroup
from pageObjects.SearchGroupPage import SearchGroup
from pageObjects.ViewEditGroupPage import EditGroup
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_009_AddUserToGroup:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    @pytest.mark.order(9)
    def test_addUserToGroup(self, setup):
        self.logger.info("****************** Test_009_AddUserToGroup **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login successful **********************")

        self.logger.info("****************** Starting Adding User to a Group **********************")

        self.addGroup = AddGroup(self.driver)
        self.addGroup.clickOnAdministrationMenu()
        self.addGroup.clickOnSecAdminMenu()
        self.addGroup.clickOnGroupsItem()

        self.logger.info("****************** Adding User to a Group **********************")
        self.searchgroup = SearchGroup(self.driver)
        self.searchgroup.setSearch("Automation Group")
        time.sleep(5)
        status = self.searchgroup.searchGroupByGroupName("Automation Group", "edit")
        time.sleep(5)
        #        print("status:" + str(status))

        self.editGroup = EditGroup(self.driver)
        self.editGroup.clickOnManageUsers()
        self.editGroup.selectUser("Automation User")

        self.editGroup.clickOnAddUser()
        time.sleep(2)
        self.editGroup.clickOnSave()
        time.sleep(2)

        self.logger.info("****************** Saving group information **********************")

        self.logger.info("****************** Edit Group validation started **********************")

#        self.element = self.driver.find_element(by=By.CLASS_NAME, value="toast-message")

        self.body_tagName = "body"
        self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text
        #        print(self.msg)
        if 'Group successfully saved' in self.msg:
            assert True
            self.logger.info("********* Add user to G group Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addUserToGroup_scr.png")  # Screenshot
            self.logger.error("********* Add User to G group Test Failed ***************")
            assert False

        self.driver.close()
        self.logger.info("****************** End Test_009_AddUserToGroup **********************")
