import time
from selenium.webdriver.common.by import By


class SearchRole:
    # Search Role Page
    txtSearch_id = "search"

    table_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody"
    tableRows_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr"
    tableColumns_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setSearch(self, search):
        self.driver.find_element(by=By.ID, value=self.txtSearch_id).clear()
        self.driver.find_element(by=By.ID, value=self.txtSearch_id).send_keys(search)

    def getNoOfRows(self):
        return len(self.driver.find_elements(by=By.XPATH, value=self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(by=By.XPATH, value=self.tableColumns_xpath))

    def searchRoleByRoleDesc(self, vsearch):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(by=By.XPATH, value=self.table_xpath)
            roledesc_id_cell_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[3]"
            roledesc_id = table.find_element(by=By.XPATH, value=roledesc_id_cell_xpath).text
            time.sleep(5)

            if roledesc_id == vsearch:
                flag = True
                roleedit_to_click_xpath = "//*[@id='form-admin-role-list']/div/div[2]/div/div/div[1]/table/tbody[1]/tr[" + str(
                r) + "]/td[1]/div/button[2]/i"
                self.driver.find_element(by=By.XPATH, value=roleedit_to_click_xpath).click()
                break
        return flag
