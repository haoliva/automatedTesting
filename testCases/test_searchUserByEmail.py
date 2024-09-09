import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddUserPage import AddUser
from pageObjects.SearchUserPage import SearchUser
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_SearchUserByEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    @pytest.mark.regression
    @pytest.mark.order(4)
    def test_searchUserByEmail(self, setup):
        self.logger.info("****************** Test_004_SearchUserByEmail **********************")
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

        self.logger.info("****************** Starting Search User By Email **********************")

        self.addUser = AddUser(self.driver)
        self.addUser.clickOnAdministrationMenu()
        self.addUser.clickOnSecAdminMenu()
        self.addUser.clickOnUsersItem()

        self.logger.info("****************** Searching User By Email **********************")
        self.searchuser = SearchUser(self.driver)
        self.searchuser.setSearch("holiva@infusedsolutions.com")
        time.sleep(5)
        status = self.searchuser.searchUserByEmail("holiva@infusedsolutions.com")

        print("status:"+str(status))

        if status:
            assert True
            self.driver.close()
            self.logger.info("************* Searching User By Email is passed *********************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_searchUserByEmail.png")
            self.driver.close()
            self.logger.error("************* Searching User By Email is failed *********************")
            assert False

        self.logger.info("****************** Test_004_SearchUserByEmail Finished **********************")

