import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddUserPage import AddUser
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddUser:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger

    @pytest.mark.sanity
    @pytest.mark.order(3)
    def test_addUser(self, setup):
        self.logger.info("****************** Test_003_AddUser **********************")
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

        self.logger.info("****************** Starting Add User Test **********************")

        self.addUser = AddUser(self.driver)
        self.addUser.clickOnAdministrationMenu()
        self.addUser.clickOnSecAdminMenu()
        self.addUser.clickOnUsersItem()

        self.addUser.clickOnAddNewUser()

        self.logger.info("****************** Providing user information **********************")

        self.vusername = random_generator()
        self.addUser.setUserName(self.vusername)
        self.addUser.setStatus("Active")
        self.addUser.setFullName("Automation User")
        self.addUser.setPassword("Auto2001!")
        self.addUser.setConfPwd("Auto2001!")
        self.addUser.setLocale()
        self.addUser.setTimezone()
        self.vemail = random_generator() + "@email.com"
        self.addUser.setEmail(self.vemail)
        self.addUser.clickOnSave()

        self.logger.info("****************** Saving user information **********************")

        self.logger.info("****************** Add User validation started **********************")

        #self.driver.implicitly_wait(30)
        #        self.msg = self.driver.find_element_by_tag_name("body").text

        #       print(self.msg)

        self.driver.close()
        self.logger.info("****************** End Test_003_AddUser **********************")


def random_generator(size=8, chars=string.ascii_lowercase + string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))
