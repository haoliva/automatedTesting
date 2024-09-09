from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddTask:
    # Add Task Page
    lnkTasks_menu_linkText = "Tasks"
    btnAddNewTask_xpath = "//button[contains(@ng-if,'newTask')]"
    txtTaskName_id = "usr"
#    txtTaskDesc_xpath = "//html-content[1]/div[1]/div[3]/div[1]/p[1]"
    btnSaveTask_xpath = "//button[contains(@ng-click,'onSave()')]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnTasksItems(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkTasks_menu_linkText).click()

    def clickOnAddNewTask(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddNewTask_xpath).click()

    def setTaskName(self, taskname):
        self.driver.find_element(by=By.ID, value=self.txtTaskName_id).send_keys(taskname)

 #   def setTaskDesc(self, taskdesc):
 #       self.driver.find_element(by=By.XPATH, value=self.txtTaskDesc_xpath).send_keys(taskdesc)

    def clickOnSave(self):
        self.driver.find_element(by=By.XPATH, value=self.btnSaveTask_xpath).click()
