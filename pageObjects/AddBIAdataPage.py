from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AddBIAdata:
    # Add BIA data Page
    lnkViewWksp_linkText = "View Workspace"
    btnWorkBIA_xpath = "//*[@id='wid-id-0']/div/div/plan-component-widget/div/div[2]/div[1]/button[1]"
    lnkChangesAnticipated_xpath = "//*[@id='all']/ul/a[5]/span[2]"
    btnNew_xpath = "//button[contains(text(),'New')]"
    btnWorking_xpath = "//a[contains(text(),'Working')]"
    btnWorking1_xpath = "//button[contains(text(),'Working')]"
    btnRelease_xpath = "//button[contains(text(),'Released')]"
    btnRelease1_xpath = "//a[contains(text(),'Released')]"
    btnAddNewRecord_xpath = "//button[contains(text(),'Add')]"
    lnkFilterNotSelected_xpath = "//dynamic-form[1]/ng-form[1]/div[2]/div[1]/div[1]/span[2]/span[1]/resource-filter-select[1]/i[1]/span[1]"
    # ***************************** Select field at Delegations Of Authority *********************************
    lnkFilterNotSelected_xpath1 = "//dynamic-form[1]/ng-form[1]/div[1]/div[1]/div[1]/span[2]/span[1]/resource-filter-select[1]/i[1]/span[1]"
    lnkFilterNotSelected_xpath2 = "//dynamic-form[1]/ng-form[1]/div[4]/div[1]/div[1]/span[2]/span[1]/resource-filter-select[1]/i[1]/span[1]"
    lnkFilterNotSelected_xpath3 = "//dynamic-form[1]/ng-form[1]/div[5]/div[1]/div[1]/span[2]/span[1]/resource-filter-select[1]/i[1]/span[1]"
    lnkFilterNotSelected_xpath4 = "//dynamic-form[1]/ng-form[1]/div[6]/div[1]/div[1]/span[2]/span[1]/resource-filter-select[1]/i[1]/span[1]"
    lnkFilterNotSelected_xpath5 = "//dynamic-form[1]/ng-form[1]/div[3]/div[1]/div[1]/span[2]/span[1]/resource-filter-select[1]/i[1]/span[1]"
    # ********************************************************************************************************
    drpSelectAFilter_xpath = "//span[contains(text(),'Select a filter')]"
    lnkFilter_xpath = "//span[contains(text(),'HR Database')]"
    #lnkFilter_xpath = "//input[contains(text(),'Select a filter')]"
    btnOK_xpath = "//span[contains(text(),'OK')]"
    #btnCloseForm = "//span[contains(text(),'×')]"
    btnCloseForm = "//button[contains(text(),'Cancel')]"

    txtAnticipatedChanges_xpath = "//*[contains(@id,'anticipatedChanges')]"
    txtFinOperBusImpacts_xpath = "//*[contains(@id,'finOperBusinessImpacts')]"
    txtDiscIssues_xpath = "//*[contains(@id,'discussionIssues')]"

    btnSave_xpath = "//button[contains(text(),'Save')]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnViewWorkspace(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkViewWksp_linkText).click()

    def clickOnWorkBIA(self):
        self.driver.find_element(by=By.XPATH, value=self.btnWorkBIA_xpath).click()

    def clickOnNew(self):
        self.driver.find_element(by=By.XPATH, value=self.btnNew_xpath).click()

    def clickOnWorking(self):
        self.driver.find_element(by=By.XPATH, value=self.btnWorking_xpath).click()

    def clickOnWorking1(self):
        self.driver.find_element(by=By.XPATH, value=self.btnWorking1_xpath).click()

    def clickOnReleased(self):
        self.driver.find_element(by=By.XPATH, value=self.btnRelease_xpath).click()

    def clickOnReleased1(self):
        self.driver.find_element(by=By.XPATH, value=self.btnRelease1_xpath).click()

    def clickOnChangesAnticipated(self):
        self.driver.find_element(by=By.XPATH, value=self.lnkChangesAnticipated_xpath).click()

    def clickOnAdd(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddNewRecord_xpath).click()

    def clickOnFilterNotSelected(self):
        self.driver.find_element(by=By.XPATH, value=self.lnkFilterNotSelected_xpath).click()

    def clickOnFilterNotSelected_1(self):
        self.driver.find_element(by=By.XPATH, value=self.lnkFilterNotSelected_xpath1).click()

    def clickOnFilterNotSelected_2(self):
        self.driver.find_element(by=By.XPATH, value=self.lnkFilterNotSelected_xpath2).click()

    def clickOnFilterNotSelected_3(self):
        self.driver.find_element(by=By.XPATH, value=self.lnkFilterNotSelected_xpath3).click()

    def clickOnFilterNotSelected_4(self):
        self.driver.find_element(by=By.XPATH, value=self.lnkFilterNotSelected_xpath4).click()

    def clickOnFilterNotSelected_5(self):
        self.driver.find_element(by=By.XPATH, value=self.lnkFilterNotSelected_xpath5).click()

    def clickOnSelectAFilter(self):
        self.driver.find_element(by=By.XPATH, value=self.drpSelectAFilter_xpath).click()
#        self.driver.find_element(by=By.XPATH, value=self.drpSelectAFilter_xpath).send_keys(Keys.RETURN)

    def clickOnFilter(self):
#        self.driver.find_element(by=By.XPATH, value=self.lnkFilter_xpath).send_keys(Keys.RETURN)
        self.driver.find_element(by=By.XPATH, value=self.lnkFilter_xpath).click()

    def clickOnOk(self):
        self.driver.find_element(by=By.XPATH, value=self.btnOK_xpath).click()

    def clickOnCloseForm(self):
        self.driver.find_element(by=By.XPATH, value=self.btnCloseForm).click()

    def setAnticipatedChanges(self, anticipatedchanges):
        self.driver.find_element(by=By.XPATH, value=self.txtAnticipatedChanges_xpath).clear()
        self.driver.find_element(by=By.XPATH, value=self.txtAnticipatedChanges_xpath).send_keys(anticipatedchanges)

    def setFinOperBusImpacts(self, finoperbusimpacts):
        self.driver.find_element(by=By.XPATH, value=self.txtFinOperBusImpacts_xpath).clear()
        self.driver.find_element(by=By.XPATH, value=self.txtFinOperBusImpacts_xpath).send_keys(finoperbusimpacts)

    def setDiscussionIssues(self, discussionsissues):
        self.driver.find_element(by=By.XPATH, value=self.txtDiscIssues_xpath).clear()
        self.driver.find_element(by=By.XPATH, value=self.txtDiscIssues_xpath).send_keys(discussionsissues)

    def clickOnSave(self):
        self.driver.find_element(by=By.XPATH, value=self.btnSave_xpath).click()
