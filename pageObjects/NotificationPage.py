import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys


class Notification:
    # Notification Page

    btnNewTemplate_xpath = "//header/div[1]/template-widget[1]/button[1]/i[1]"
    btnNewNotification_xpath = "//header/div[1]/notification-widget[1]/button[1]/i[1]"
    txtTitle_name = "title"
    txtSubject_name = "subject"
    drpEvent_xpath = "//bs-form-group[1]/div[1]/div[1]/div[1]/span[1]/i[1]"
    drpTemplate_xpath = "//bs-form-group[1]/div[1]/template-picker[1]/div[1]/div[1]/span[1]/i[1]"
    selectionEvent_xpath = ""
    selectionTemplate_xpath = ""
    # event = ""
    # selectionEvent_xpath = "//div[contains(text(),'" + event + "')]"
    # selectionEvent_linkText = "New User Email"
    txtDescription_xpath = "//div[contains(@class,'fr-element fr-view')]"
    btnSave_xpath = "//i[@class='fa fa-save']"

    def __init__(self, driver):
        self.driver = driver

    def clickOnNewTemplate(self):
        self.driver.find_element(by=By.XPATH, value=self.btnNewTemplate_xpath).click()

    def clickOnNewNotification(self):
        self.driver.find_element(by=By.XPATH, value=self.btnNewNotification_xpath).click()

    def setTitle(self, title):
        self.driver.find_element(by=By.NAME, value=self.txtTitle_name).clear()
        self.driver.find_element(by=By.NAME, value=self.txtTitle_name).send_keys(title)

    def setSubject(self, subject):
        self.driver.find_element(by=By.NAME, value=self.txtSubject_name).clear()
        self.driver.find_element(by=By.NAME, value=self.txtSubject_name).send_keys(subject)

    def setEvent(self, event):
        self.driver.find_element(by=By.XPATH, value=self.drpEvent_xpath).click()
        time.sleep(1)
        self.selectionEvent_xpath = "//div[contains(text(),'" + event + "')]"
        #print("Event: ", self.selectionEvent_xpath)
        self.driver.find_element(by=By.XPATH, value=self.selectionEvent_xpath).click()

    def setTemplate(self, template):
        self.driver.find_element(by=By.XPATH, value=self.drpTemplate_xpath).click()
        time.sleep(1)
        self.selectionTemplate_xpath = "//div[contains(text(),'" + template + "')]"
        #print("Event: ", self.selectionEvent_xpath)
        self.driver.find_element(by=By.XPATH, value=self.selectionTemplate_xpath).click()

    def setDescription(self, description):
        #self.driver.find_element(by=By.XPATH, value=self.txtDescription_xpath).click()
        self.driver.find_element(by=By.XPATH, value=self.txtDescription_xpath).send_keys(description)

    def clickOnSave(self):
        self.driver.find_element(by=By.XPATH, value=self.btnSave_xpath).click()
