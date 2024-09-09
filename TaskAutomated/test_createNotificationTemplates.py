import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.NotificationPage import Notification
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_CreateNotificationTemplates:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen() # Logger

    path = ".//TasksData/create-notifications.xlsx"

#    @pytest.mark.regression
#    @pytest.mark.order(15)

    def test_createNotificationTemplates(self, setup):
        self.logger.info("****************** CreateNotificationTemplates **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login successful **********************")

        self.rows = XLUtils.getRowCount(self.path, 'notification-templates')
        print("Number of Rows in a Excel:", self.rows)

        for r in range(2, self.rows + 1):
            self.url = XLUtils.readData(self.path, 'notification-templates', r, 1)
            self.title = XLUtils.readData(self.path, 'notification-templates', r, 2)
            self.subject = XLUtils.readData(self.path, 'notification-templates', r, 3)
            self.event = XLUtils.readData(self.path, 'notification-templates', r, 4)
            self.description = XLUtils.readData(self.path, 'notification-templates', r, 5)

            self.logger.info("****************** Open Notifications area by URL **********************")
            self.logger.info("URL: " + self.url)
            self.driver.get(self.url)

            self.notification = Notification(self.driver)
            time.sleep(1)
            self.notification.clickOnNewTemplate()
            time.sleep(2)
            self.notification.setTitle(self.title)
            self.notification.setSubject(self.subject)
            self.notification.setEvent(self.event)
            time.sleep(1)
            self.notification.setDescription(self.description)

            time.sleep(1)
            self.notification.clickOnSave()
            time.sleep(3)

            self.logger.info("*************** Create a Notification Template validation started *******************")
            self.body_tagName = "body"
            self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text

            if 'Template created successfully' in self.msg:
                assert True
                self.logger.info("********* Create a Notification Template Test Passed ***************")
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_createNotificationTemplate_scr.png")  #Screenshot
                self.logger.error("********* Create a Notification Template Failed ***************")
                assert False
                break

        self.driver.close()
        self.logger.info("****************** End Test_Create Notification Templates  **********************")



