from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddRole:
    # Add Role Page
    lnkAdministration_menu_linkText = "Administration"
    lnkSecurity_menu_linkText = "Security Administration"
    lnkRoles_menu_linkText = "Roles"
    btnAddNewRole_xpath = "//button[contains(@tooltip,'New Role')]"
    txtRoleName_id = "name"
    txtRoleDesc_id = "description"
    btnApplication_xpath = "//i[contains(@ng-class, 'row.tree_icon')]"
#    chkAppRead_xpath = "//table[@class='table tree-grid']/tbody/tr[1]/td[2]"    # App Read permission
    chkAppRead_xpath = "//table[@class='table tree-grid']/tbody/tr[1]/td[2]/div/input[@type='checkbox']"  # App Read

    table_xpath = "//table[@class='table tree-grid']/tbody"
    tableRows_xpath = "//table[@class='table tree-grid']/tbody/tr"
    tableColumns_xpath = "//table[@class='table tree-grid']/tbody/tr/td"
    chkDashboardRead_xpath = "//table[@class='table tree-grid']/tbody/tr[2]/td[2]/div/input[@type='checkbox']"  # Dashboard

    btnSaveRole_cssSelector = "button.btn:nth-child(1)"

    def __init__(self, driver):
        self.driver = driver

    def clickOnAdministrationMenu(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkAdministration_menu_linkText).click()

    def clickOnSecAdminMenu(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkSecurity_menu_linkText).click()

    def clickOnRolesItem(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkRoles_menu_linkText).click()

    def clickOnAddNewRole(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddNewRole_xpath).click()

    def setRoleName(self, rolename):
        self.driver.find_element(by=By.ID, value=self.txtRoleName_id).send_keys(rolename)

    def setRoleDesc(self, roledesc):
        self.driver.find_element(by=By.ID, value=self.txtRoleDesc_id).send_keys(roledesc)

    def clickOnApplication(self):
        self.driver.find_element(by=By.XPATH, value=self.btnApplication_xpath).click()

    def clickOnAppReadPermission(self):
        self.driver.find_element(by=By.XPATH, value=self.chkAppRead_xpath).click()

    def clickOnDashboardReadPermission(self):
        self.driver.find_element(by=By.XPATH, value=self.chkDashboardRead_xpath).click()

    def clickOnSave(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.btnSaveRole_cssSelector).click()
