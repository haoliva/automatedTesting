import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddRolePage import AddRole
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_010_AddRole:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.order(10)
    def test_addRole(self, setup):
        self.logger.info("****************** Test_010_AddRole **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(45)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("****************** Login successful **********************")

        self.logger.info("****************** Starting Add Role Test **********************")

        self.addRole = AddRole(self.driver)
        self.addRole.clickOnAdministrationMenu()
        self.addRole.clickOnSecAdminMenu()
        self.addRole.clickOnRolesItem()

        self.addRole.clickOnAddNewRole()
        time.sleep(2)

        self.logger.info("****************** Providing role information **********************")

        self.addRole.clickOnAppReadPermission()
        time.sleep(1)
        self.body_tagName = "body"
        self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text
        #        print(self.msg)
        if 'This form has been Updated!' in self.msg:
            assert True
            self.vrolename = random_generator()
            self.addRole.setRoleName(self.vrolename)
            self.addRole.setRoleDesc("Automation Role - App Read Access")

            self.logger.info("****************** Saving role information **********************")
            time.sleep(1)
            self.addRole.clickOnSave()
            self.logger.info("********* Add role Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addRole_scr.png")  # Screenshot
            self.logger.error("********* Add role Test Failed ***************")
            assert False

#        self.logger.info("****************** Add Role validation started **********************")

#        self.driver.implicitly_wait(30)
        #        self.msg = self.driver.find_element_by_tag_name("body").text

        #       print(self.msg)

        self.driver.close()
        self.logger.info("****************** End Test_010_AddRole **********************")


def random_generator(size=8, chars=string.ascii_lowercase + string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))
