import time
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class EditGroup:
    # Edit Group Page
    btnAddGrantSystemRole_xpath = "//button[contains(@tooltip,'Grant a Role')]"
    btnManageUsers_xpath = "//button[contains(@tooltip,'Manage Users')]"

    btnSelectRole_xpath = "//span[contains(@tabindex,'-1')]"
    optSelectRole_xpath = "//div[contains(text(),'System Administrator')]"

    inputSelectUser_xpath = "//input[contains(@placeholder,'Select')]"

    btnAddUser_xpath = "//button[contains(@type,'submit')]"

    btnDeleteGroup_xpath = "//span[contains(text(),'Delete')]"
    btnConfirmDeleteGroup_xpath = "//strong[contains(text(),'Delete')]"

    btnSaveAddRole_xpath = "/html/body/div[6]/div/div/div/button[1]"

    btnSaveGroup_cssSelector = "button.btn:nth-child(2)"

    def __init__(self, driver):
        self.driver = driver

#    ******************************** add a system role to a group ***********************
    def clickOnAddSystemRole(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddGrantSystemRole_xpath).click()

    def clickOnSelectRole(self):
        self.driver.find_element(by=By.XPATH, value=self.btnSelectRole_xpath).click()

    def clickOnSystemRole(self):
        self.driver.find_element(by=By.XPATH, value=self.optSelectRole_xpath).click()

    def clickOnSaveRole(self):
        self.driver.find_element(by=By.XPATH, value=self.btnSaveAddRole_xpath).click()

#    ************************************** add user to a group **************************
    def clickOnManageUsers(self):
        self.driver.find_element(by=By.XPATH, value=self.btnManageUsers_xpath).click()

    def selectUser(self, user):
        self.driver.find_element(by=By.XPATH, value=self.inputSelectUser_xpath).send_keys(user)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=self.inputSelectUser_xpath).send_keys(Keys.ENTER)

    def clickOnAddUser(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddUser_xpath).click()

#    *************************************** delete the Group **********************
    def clickOnDelete(self):
        self.driver.find_element(by=By.XPATH, value=self.btnDeleteGroup_xpath).click()

    def clickOnConfirmDelete(self):
        self.driver.find_element(by=By.XPATH, value=self.btnConfirmDeleteGroup_xpath).click()

#    *************************************** save the Edit Group form **********************
    def clickOnSave(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.btnSaveGroup_cssSelector).click()


