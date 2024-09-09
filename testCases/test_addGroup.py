import pytest
import time

from selenium.webdriver.common.by import By
from pageObjects.AddGroupPage import AddGroup
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_006_AddGroup:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.order(6)
    def test_addGroup(self, setup):
        self.logger.info("****************** Test_006_AddGroup **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login successful **********************")

        self.logger.info("****************** Starting Add Group Test **********************")

        self.addGroup = AddGroup(self.driver)
        self.addGroup.clickOnAdministrationMenu()
        self.addGroup.clickOnSecAdminMenu()
        self.addGroup.clickOnGroupsItem()

        self.addGroup.clickOnAddNewGroup()

        self.logger.info("****************** Providing group information **********************")

#        self.vgroupname = random_generator()
        self.vgroupname = "Automation Group"
        self.addGroup.setGroupName(self.vgroupname)
        self.addGroup.setGroupDesc("Group created through automation testing")
        self.addGroup.clickOnSave()

        self.logger.info("****************** Saving group information **********************")

        self.logger.info("****************** Add Group validation started **********************")

        self.element = self.driver.find_element(by=By.CLASS_NAME, value="toast-message")

        self.body_tagName = "body"
        self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text
#        print(self.msg)
        if 'Group successfully saved' in self.msg:
            assert True
            self.logger.info("********* Add group Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addGroup_scr.png")    # Screenshot
            self.logger.error("********* Add group Test Failed ***************")
            assert False

#        print(self.msg)

        self.driver.close()
        self.logger.info("****************** End Test_006_AddGroup **********************")


def random_generator(size=10, chars=string.ascii_lowercase + string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))
