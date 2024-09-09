from selenium.webdriver.common.by import By


class AddWorkspace:
    # Add Workspace Page
    lnkAdministration_menu_linkText = "Administration"
    lnkOrgAdm_menu_linkText = "Organization Administration"
    lnkWorkspaces_menu_linkText = "Workspaces"
    btnAddNewWorkspace_xpath = "//button[contains(@tooltip,'New')]"
    txtWorkspaceName_id = "name"
    txtWorkspaceDesc_xpath = "//div[contains(@class,'fr-element fr-view')]"
    drpDateFormat_xpath = "//*[@id='selectedFormat']/div/span"
    selectionDateFormat_linkText = "MM/DD/YYYY"

    btnSaveWorkspace_cssSelector = ".btn-primary"

    def __init__(self, driver):
        self.driver = driver

    def clickOnAdministrationMenu(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkAdministration_menu_linkText).click()

    def clickOnOrgAdmMenu(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkOrgAdm_menu_linkText).click()

    def clickOnWorkspacesItem(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkWorkspaces_menu_linkText).click()

    def clickOnAddNewWorkspace(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddNewWorkspace_xpath).click()

    def setWorkspaceName(self, wsname):
        self.driver.find_element(by=By.ID, value=self.txtWorkspaceName_id).send_keys(wsname)

    def setDescription(self, description):
        self.driver.find_element(by=By.XPATH, value=self.txtWorkspaceDesc_xpath).send_keys(description)

    def setDateFormat(self):
        self.driver.find_element(by=By.XPATH, value=self.drpDateFormat_xpath).click()
        self.driver.find_element(by=By.LINK_TEXT, value=self.selectionDateFormat_linkText).click()

    def clickOnSave(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.btnSaveWorkspace_cssSelector).click()
