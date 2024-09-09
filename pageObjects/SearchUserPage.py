from selenium.webdriver.common.by import By


class SearchUser:
    # Search User Page
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

    def searchUserByEmail(self, search):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(by=By.XPATH, value=self.table_xpath)
            email_cell_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[4]"
            email_id = table.find_element(by=By.XPATH, value=email_cell_xpath).text

            if email_id == search:
                flag = True
                break
        return flag

    def searchUserByUsername(self, search):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(by=By.XPATH, value=self.table_xpath)
            username_id_cell_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[2]"
            username_id = table.find_element(by=By.XPATH, value=username_id_cell_xpath).text

            if username_id == search:
                flag = True
                break
        return flag
