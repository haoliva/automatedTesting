from selenium.webdriver.common.by import By


class Documents:
    # Documents Page
    lnkDocuments_menu_linkText = "Documents"
    txtSearch_xpath = "//div[contains(@class,'input-group')]/input"
    btnSearch_xpath = "//div[contains(@class,'input-group')]/button"
    chkSelectAll_xpath = "//div[contains(@ui-grid-one-bind-aria-label,'selection.selectAll')]"
    btnPublish_xpath = "//span[contains(text(),'Publish')]"
    txtSearchWorkspace_xpath = "//input[@ng-model='search']"
    lnkAvailableWorkspaces_xpath = "//option[contains(text(),'Automation Testing')]"
    btnAdd_id = "btnAdd"
    btnPublishDocuments_xpath = "//button[contains(@ng-click,'publishDocuments()')]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnDocsItems(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkDocuments_menu_linkText).click()

    def setDocToSearch(self, documentname):
        self.driver.find_element(by=By.XPATH, value=self.txtSearch_xpath).send_keys(documentname)

    def clickOnSearch(self):
        self.driver.find_element(by=By.XPATH, value=self.btnSearch_xpath).click()

    def clickOnSelectAll(self):
        self.driver.find_element(by=By.XPATH, value=self.chkSelectAll_xpath).click()

    def clickOnPublish(self):
        self.driver.find_element(by=By.XPATH, value=self.btnPublish_xpath).click()

    def setWSToSearch(self, workspacename):
        self.driver.find_element(by=By.XPATH, value=self.txtSearchWorkspace_xpath).send_keys(workspacename)

    def clickOnAvailableWS(self):
        self.driver.find_element(by=By.XPATH, value=self.lnkAvailableWorkspaces_xpath).click()

    def clickOnAddToSelWS(self):
        self.driver.find_element(by=By.ID, value=self.btnAdd_id).click()

    def clickOnPublishButton(self):
        self.driver.find_element(by=By.XPATH, value=self.btnPublishDocuments_xpath).click()
