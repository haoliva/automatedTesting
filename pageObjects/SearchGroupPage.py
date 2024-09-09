from selenium.webdriver.common.by import By


class SearchGroup:
    # Search Group Page
    txtSearch_id = "search"
    btnEditGroup_xpath = "//i[contains(@class,'fa fa-pencil')]"

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

    def searchGroupByGroupName(self, vsearch, voption):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(by=By.XPATH, value=self.table_xpath)
            groupname_id_cell_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[2]"
            groupname_id = table.find_element(by=By.XPATH, value=groupname_id_cell_xpath).text

            if groupname_id == vsearch and voption == 'edit':
                flag = True
                groupname_to_click_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[2]/a/span"
                self.driver.find_element(by=By.XPATH, value=groupname_to_click_xpath).click()
                break
            elif groupname_id == vsearch and voption == 'remove':
                flag = True
                editgroup_to_click_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[1]/div/button[@tooltip='Edit Group']"
                self.driver.find_element(by=By.XPATH, value=editgroup_to_click_xpath).click()
                break
        return flag
