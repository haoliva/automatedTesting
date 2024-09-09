from selenium.webdriver.common.by import By


class OrgSetup:
    # Configure Org Setup Page
    lnkAdministration_menu_linkText = "Administration"
    lnkOrgAdm_menu_linkText = "Organization Administration"
    lnkOrgSetup_menu_linkText = "Organization Setup"

    drpPagination_xpath = "//*[@id='defaultPageSize']/div/span/i"
#    drpPagination_xpath = "//*[@id='defaultPageSize']/div/span/span[contains(@xpath,'2')]"
#    selPagination_xpath = "//*[@id='ui-select-choices-row-14-3']/a/div/span"
#    selPagination_linkText = "50"
    selPagination_xpath_ini = "//span[contains(text(),'100')]"
    selPagination_xpath = "//span[contains(text(),'250')]"

    btnSave_xpath = "//button[contains(text(),'Save')]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnAdministrationMenu(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkAdministration_menu_linkText).click()

    def clickOnOrgAdmMenu(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkOrgAdm_menu_linkText).click()

    def clickOnOrgSetupItem(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkOrgSetup_menu_linkText).click()

    def setPagination(self):
        self.driver.find_element(by=By.XPATH, value=self.drpPagination_xpath).click()
        self.driver.find_element(by=By.XPATH, value=self.selPagination_xpath_ini).click()
        self.driver.find_element(by=By.XPATH, value=self.drpPagination_xpath).click()
        self.driver.find_element(by=By.XPATH, value=self.selPagination_xpath).click()

    def clickOnSave(self):
        self.driver.find_element(by=By.XPATH, value=self.btnSave_xpath).click()
