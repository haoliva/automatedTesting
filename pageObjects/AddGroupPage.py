from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddGroup:
    # Add Group Page
    lnkAdministration_menu_linkText = "Administration"
    lnkSecurity_menu_linkText = "Security Administration"
    lnkGroups_menu_linkText = "Groups"
    btnAddNewGroup_xpath = "//button[contains(@tooltip,'New Group')]"
    txtGroupName_id = "groupName"
    txtGroupDesc_id = "groupDesc"
    btnSaveGroup_cssSelector = "button.btn:nth-child(1)"

    def __init__(self, driver):
        self.driver = driver

    def clickOnAdministrationMenu(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkAdministration_menu_linkText).click()

    def clickOnSecAdminMenu(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkSecurity_menu_linkText).click()

    def clickOnGroupsItem(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkGroups_menu_linkText).click()

    def clickOnAddNewGroup(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddNewGroup_xpath).click()

    def setGroupName(self, groupname):
        self.driver.find_element(by=By.ID, value=self.txtGroupName_id).send_keys(groupname)

    def setGroupDesc(self, groupdesc):
        self.driver.find_element(by=By.ID, value=self.txtGroupDesc_id).send_keys(groupdesc)

    def clickOnSave(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.btnSaveGroup_cssSelector).click()
