import pytest
import time

from selenium.webdriver.common.by import By
from pageObjects.DocumentsPage import Documents
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_027_PublishDocument:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    @pytest.mark.order(27)
    def test_publishDocument(self, setup):
        self.logger.info("****************** Test_027_PublishDocument **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login successful **********************")

        self.logger.info("****************** Starting Searching a Document **********************")

        self.documents = Documents(self.driver)
        self.documents.clickOnDocsItems()

        self.documents.setDocToSearch("Annex H TTE")
        time.sleep(3)
        self.documents.clickOnSearch()
        time.sleep(1)

        self.logger.info("****************** Publishing a document **********************")

        self.documents.clickOnSelectAll()
        self.documents.clickOnPublish()
        time.sleep(2)
        self.documents.setWSToSearch("Automation Testing")
        time.sleep(2)
        self.documents.clickOnAvailableWS()
        self.documents.clickOnAddToSelWS()
        self.documents.clickOnPublishButton()
        time.sleep(2)

        self.logger.info("****************** Publishing validation started **********************")

        self.body_tagName = "body"
        self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text
#        print(self.msg)
        if 'process has been successful' in self.msg:
            assert True
            self.logger.info("********* Publishing Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_publishDocument.png")    # Screenshot
            self.logger.error("********* Publishing Test Failed ***************")
            assert False

#        print(self.msg)

        self.driver.close()
        self.logger.info("****************** End Test_027_PublishDocument **********************")