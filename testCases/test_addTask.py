import pytest
import time

from selenium.webdriver.common.by import By
from pageObjects.AddTaskPage import AddTask
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_026_AddTask:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    @pytest.mark.order(26)
    def test_addTask(self, setup):
        self.logger.info("****************** Test_026_AddTask **********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.driver.implicitly_wait(30)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****************** Login successful **********************")

        self.logger.info("****************** Starting Add Task Test **********************")

        self.addTask = AddTask(self.driver)
        self.addTask.clickOnTasksItems()

        self.addTask.clickOnAddNewTask()

        self.logger.info("****************** Providing task information **********************")

        self.vtaskname = "Automation Task"
        self.addTask.setTaskName(self.vtaskname)
#        time.sleep(2)
#        self.addTask.setTaskDesc("Task created through automation testing")
        self.addTask.clickOnSave()
        time.sleep(2)

        self.logger.info("****************** Saving task information **********************")

        self.logger.info("****************** Add Task validation started **********************")

        self.body_tagName = "body"
        self.msg = self.driver.find_element(by=By.TAG_NAME, value=self.body_tagName).text
#        print(self.msg)
        if 'Task created successfully' in self.msg:
            assert True
            self.logger.info("********* Add Task Test Passed ***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addTask_scr.png")    # Screenshot
            self.logger.error("********* Add task Test Failed ***************")
            assert False

#        print(self.msg)

        self.driver.close()
        self.logger.info("****************** End Test_026_addTask **********************")