import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddWorkspacePage import AddWorkspace
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_013_AddWorkspace:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.order(13)
    def test_addWorkspace(self, setup):
        self.logger.info("****************** Test_0013_AddWorkspace **********************")
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

        self.logger.info("****************** Starting Add Workspace Test **********************")

        self.addWorkspace = AddWorkspace(self.driver)
        self.addWorkspace.clickOnAdministrationMenu()
        self.addWorkspace.clickOnOrgAdmMenu()
        self.addWorkspace.clickOnWorkspacesItem()

        self.addWorkspace.clickOnAddNewWorkspace()

        self.logger.info("****************** Providing workspace information **********************")

#        self.vwsname = random_generator()
#        self.addWorkspace.setWorkspaceName(self.vwsname)
        self.addWorkspace.setWorkspaceName("Automation Testing")
        self.addWorkspace.setDescription("Workspace added through Automation Testing")
        self.addWorkspace.setDateFormat()

        self.addWorkspace.clickOnSave()
        time.sleep(2)

        self.logger.info("****************** Saving workspace information **********************")

        self.logger.info("****************** Add Workspace validation started **********************")

        self.element = self.driver.find_element(by=By.CLASS_NAME, value="toast-message")

        self.body_tagName = "body"
        self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text

        if 'Successfully saved workspace' in self.msg:
            assert True
            self.logger.info("********* Add workspace Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addWorkspace_scr.png")  # Screenshot
            self.logger.error("********* Add workspace Test Failed ***************")
            assert False

        self.driver.close()
        self.logger.info("****************** End Test_013_AddWorkspace **********************")


def random_generator(size=8, chars=string.ascii_lowercase + string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))
