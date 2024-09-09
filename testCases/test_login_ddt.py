import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    @pytest.mark.order(2)
    def test_login_ddt(self, setup):
        self.logger.info("************* Test_002_DDT_Login  *********************")
        self.logger.info("************* Verifying Login DDT test  *********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(30)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in a Excel:", self.rows)

        lst_status = []  # Empty List variable

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            self.driver.implicitly_wait(20)

            act_title = self.driver.title
            exp_title = "BConView"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.logout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*** Failed ***")
                    #                    self.lp.logout()
                    lst_status.append("Pass")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Failed ***")
                    #                   self.lp.logout()
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** Passed ***")
                    #                   self.lp.logout()
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("****** Login DDT test passed ******")
            self.driver.close()
            assert True
        else:
            self.logger.info("****** Login DDT test failed ******")
            self.driver.close()
            assert False

        self.logger.info("************* End of DDT Login Test *********************")
        self.logger.info("************* Completed Test_002_DDT_Login  *********************")

#        home_ready = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.lp.home()))
#        home_ready = self.lp.home()
#        if home_ready.is_displayed():
#            assert True
#        else:
#            assert False
