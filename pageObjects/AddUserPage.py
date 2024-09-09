from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class AddUser:
    # Add User Page
    lnkAdministration_menu_linkText = "Administration"
    lnkSecurity_menu_linkText = "Security Administration"
    lnkUsers_menu_linkText = "Users"
    btnAddNewUser_xpath = "//button[contains(@tooltip,'New User')]"
    txtUserName_id = "username"
    drpStatus_name = "status"
    txtFullName_id = "fullname"
    txtPassword_id = "firstPassword"
    txtConfPwd_id = "newPassword"
    drpLocale_cssSelector = "locale-picker.form-control > div:nth-child(1) > div:nth-child(1) > span:nth-child(1) > i:nth-child(3)"
    selectionLocale_linkText = "English (US)"
    drpTimeZone_xpath = "//*[@id='form-add-edit-user']/div/div/form/div[1]/div/div[3]/div[2]/bs-form-group/div/timezone-picker/div/div/span"
    selectionTimeZone_linkText = "GMT-5"
    txtEmail_id = "email"
    btnSaveUser_cssSelector = "button.btn:nth-child(1)"

    def __init__(self, driver):
        self.driver = driver

    def clickOnAdministrationMenu(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkAdministration_menu_linkText).click()

    def clickOnSecAdminMenu(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkSecurity_menu_linkText).click()

    def clickOnUsersItem(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkUsers_menu_linkText).click()

    def clickOnAddNewUser(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddNewUser_xpath).click()

    def setUserName(self, username):
        self.driver.find_element(by=By.ID, value=self.txtUserName_id).send_keys(username)

    def setStatus(self, status):
        self.driver.find_element(by=By.NAME, value=self.drpStatus_name).send_keys(status)

    def setFullName(self, fullname):
        self.driver.find_element(by=By.ID, value=self.txtFullName_id).send_keys(fullname)

    def setPassword(self, password):
        self.driver.find_element(by=By.ID, value=self.txtPassword_id).send_keys(password)

    def setConfPwd(self, confpwd):
        self.driver.find_element(by=By.ID, value=self.txtConfPwd_id).send_keys(confpwd)

    def setLocale(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.drpLocale_cssSelector).click()
        self.driver.find_element(by=By.LINK_TEXT, value=self.selectionLocale_linkText).click()

    def setTimezone(self):
        self.driver.find_element(by=By.XPATH, value=self.drpTimeZone_xpath).click()
        self.driver.find_element(by=By.LINK_TEXT, value=self.selectionTimeZone_linkText).click()

    def setEmail(self, email):
        self.driver.find_element(by=By.ID, value=self.txtEmail_id).send_keys(email)

    def clickOnSave(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.btnSaveUser_cssSelector).click()
