import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys


class ConfigureWorkspace:
    # Configure Workspace Page
    txtSearch_id = "search"
    lnkWorkspace_xpath = "//*[@id='workspace-finder-view']/div/ul/li/a/span"
    lnkConfWksp_linkText = "Configure Workspace"
    lnkWkspComp_menu_xpath = "//a[@ui-sref='.choose_components']"

    lnkManageUsers_menu_xpath = "//a[@ui-sref='.authUser']"
    btnAdd_xpath = "//i[contains(@class,'fa fa-plus')]"
    drpUser_xpath = "/html/body/div[6]/div/div/form/div[2]/div[1]/bs-form-group/div/div[1]/user-picker/div/div"
    txtUser_xpath = "/html/body/div[6]/div/div/form/div[2]/div[1]/bs-form-group/div/div[1]/user-picker/div/input[1]"
    selectionUser_linkText = "Automation User"
    btnSaveAdd_xpath = "//span[contains(text(),'Save')]"

    txtRoleName_id = "name"
    txtRoleDesc_id = "description"
    chkWsWrite_xpath = "//table[@class='table tree-grid']/tbody/tr[1]/td[3]/div/input[@type='checkbox']"  # WS Write
    btnExpandWS_xpath = "//i[contains(@ng-class, 'row.tree_icon')]"
    chkComponentsWrite_xpath = "//table[@class='table tree-grid']/tbody/tr[7]/td[3]/div/input[@type='checkbox']"
    roleTableRows_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr"

    lnkManageGroups_menu_xpath = "//a[@ui-sref='.authGroup']"
    drpGGroup_xpath = "/html/body/div[6]/div/div/form/div[2]/div[1]/bs-form-group/div/div[1]/group-picker/div/div/span"
    txtGGroup_xpath = "/html/body/div[6]/div/div/form/div[2]/div[1]/bs-form-group/div/div[1]/group-picker/div/input[1]"
    drpGGRole_xpath = "/html/body/div[6]/div/div/form/div[2]/div[2]/bs-form-group/div/div[1]/div/span"
    txtGGRole_xpath = "/html/body/div[6]/div/div/form/div[2]/div[2]/bs-form-group/div/div[1]/input[1]"
    btnRemoveGroup_xpath = "//tbody/tr[1]/td[1]/button[1]"
    btnConfirmRemoveG_xpath = "//strong[contains(text(),'Remove')]"

    tabLGroup_xpath = "//tab-heading[contains(text(),'Local Group')]"
    txtLGroupName_id = "groupName"
    txtLGroupDesc_id = "groupDesc"
#    btnAddGrantLG_xpath = "//*[@id='form-admin-ws-edit']/div/div[2]/div[2]/div[1]/div[3]/div/div[1]/div[2]/button/i"
    btnAddGrantLG_xpath = "//button[@tooltip='Grant a Role']"
    btnSaveGrantLG_xpath = "/html/body/div[6]/div/div/div/button[1]/span"
#    btnAddUserLG_xpath = "//*[@id='form-admin-ws-edit']/div/div[2]/div[2]/div[1]/div[4]/div[1]/div[1]/div[2]/button/i"
    btnAddUserLG_xpath = "//button[@tooltip='Manage Users']"
    txtLGUser_xpath = "/html/body/div[6]/div/div/div[2]/div/div/div[1]/div/div/input"
    btnAddMemberLG_xpath = "//span[contains(text(),'Add')]"
    txtAdminRoleLG_xpath = "//div[contains(text(),'Workspace Administrator')]"
    txtEditorRoleLG_xpath = "//div[contains(text(),'Workspace Editor')]"

    btnArchive_xpath = "//span[contains(text(),'Archive')]"
    btnArchiveConfirmation_xpath = "//strong[contains(text(),'Archive')]"
    btnPurge_xpath = "//span[contains(text(),'purge')]"
    btnPurgeConfirmation = "//strong[contains(text(),'purge')]"

    table_components_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody"
    tableRows_components_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr"
    tableColumns_components_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr/td"

    btnAddASection_xpath = "//li[1]/div/div/div[1]/button/i[@class='fa fa-plus']"

    txtOutputSectionName_xpath = "//body[1]/div[7]/div[1]/div[1]/form[1]/div[2]/bs-form-group[1]/div[1]/input[1]"

    drpSectionType_xpath = "//body/div[7]/div[1]/div[1]/form[1]/div[2]/bs-form-group[3]/div[1]/div[1]"
    txtSectionType_xpath = "//body/div[7]/div[1]/div[1]/form[1]/div[2]/bs-form-group[3]/div[1]/div[1]/input[1]"

    txtFilterName_xpath = "//input[@id='name']"
    drpSelResourceType_xpath = "//span[contains(text(),'Select Resource Type')]"
    txtSelResourceType_xpath = "//input[@placeholder='Select Resource Type']"
    btnAddResourceType_xpath = "//i[contains(@tooltip,'Add this Resource Type')]"
    drpSelField_xpath = "//body/div[6]/div[1]/div[1]/form[1]/div[2]/div[2]/div[1]/query-editor-form[1]/fieldset[2]/div[1]/div[1]/bs-form-group[1]/div[1]/div[1]/div[1]/span[1]/i[1]"
    txtSelField_xpath = "//body/div[6]/div[1]/div[1]/form[1]/div[2]/div[2]/div[1]/query-editor-form[1]/fieldset[2]/div[1]/div[1]/bs-form-group[1]/div[1]/div[1]/input[1]"
    btnAddField_xpath = "//i[contains(@tooltip,'Add this field')]"
    drpSelWorkspace_xpath = "//span[contains(text(),'At Current Workspace')]"
    txtSelWorkspace_xpath = "//workspace-picker[1]/div[1]/input[1]"
    btnScope_xpath = "//body[1]/div[6]/div[1]/div[1]/form[1]/div[2]/div[2]/div[1]/query-editor-form[1]/fieldset[3]/div[1]/div[2]/bs-form-group[1]/div[1]/div[1]/a[2]/i[1]"
    optWorkspace_xpath = "//a[contains(@btn-radio,'WS_ONLY')]"
    btnAddCondition_xpath = "//button[contains(@ng-click,'addCondition()')]"
    drpSelFieldOnCondition_xpath = "//where-statement[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/i[1]"
    txtSelFieldOnCondition_xpath = "//where-statement[1]/div[1]/div[2]/div[1]/div[1]/div[1]/input[1]"
    drpSelCondition_xpath = "//select[contains(@ng-model,'rule.condition')]"
    optSelCondition_xpath = "//option[@value='EQ']"
    txtWhereStatement_xpath = "//where-statement[1]/div[1]/div[2]/div[1]/div[3]/input[1]"
    drpSelSortBy_xpath = "//query-editor-form[1]/fieldset[5]/div[1]/div[1]/bs-form-group[1]/div[1]/div[1]/div[1]/span[1]/i[1]"
    txtSelSortByField_xpath = "//query-editor-form[1]/fieldset[5]/div[1]/div[1]/bs-form-group[1]/div[1]/div[1]/input[1]"
    btnAddForSorting_xpath = "//i[contains(@tooltip,'Add for Sorting')]"
    table_filters_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody"
    tableRows_filters_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr"
    tableColumns_filters_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr/td"

    btnSaveFilter_xpath = "//i[@class='fa fa-save']"

    btnCloseSections_cssSelector = ".close > span:nth-child(1)"

    btnSaveWorkspace_cssSelector = ".btn-primary"

    def __init__(self, driver):
        self.driver = driver

    def setSearch(self, search):
        self.driver.find_element(by=By.ID, value=self.txtSearch_id).clear()
        self.driver.find_element(by=By.ID, value=self.txtSearch_id).send_keys(search)

    def contextClick(self):
        action = ActionChains(self.driver)
        workspace = self.driver.find_element(by=By.XPATH, value=self.lnkWorkspace_xpath)
#        action.context_click(workspace)
        action.context_click(on_element=workspace)
        action.perform()

    def clickOnConfigureWorkspace(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.lnkConfWksp_linkText).click()

    def clickOnWorkspaceComponents(self):
        self.driver.find_element(by=By.XPATH, value=self.lnkWkspComp_menu_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(by=By.XPATH, value=self.tableRows_components_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(by=By.XPATH, value=self.tableColumns_components_xpath))

    def searchAndEnableComponent(self, search):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(by=By.XPATH, value=self.table_components_xpath)
            component_cell_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[2]"
            tgl_component_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[7]/span[1]/label[1]"
            component_name = table.find_element(by=By.XPATH, value=component_cell_xpath).text

            if component_name == search:
                self.driver.find_element(by=By.XPATH, value=tgl_component_xpath).click()
                flag = True
                break
        return flag

    def searchAndSelectInputs(self, search):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(by=By.XPATH, value=self.table_components_xpath)
            component_cell_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[2]"
            icon_inputs_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[3]/span/span"
            component_name = table.find_element(by=By.XPATH, value=component_cell_xpath).text

            if component_name == search:
                self.driver.find_element(by=By.XPATH, value=icon_inputs_xpath).click()
                flag = True
                break
        return flag

    def searchAndSelectOutputs(self, search):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(by=By.XPATH, value=self.table_components_xpath)
            component_cell_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[2]"
            icon_outputs_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[4]/span/span[@tooltip='Outputs']"
            component_name = table.find_element(by=By.XPATH, value=component_cell_xpath).text

            if component_name == search:
                self.driver.find_element(by=By.XPATH, value=icon_outputs_xpath).click()
                flag = True
                break
        return flag

    def clickOnAddSection(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddASection_xpath).click()

    def setOutputSectionName(self, osname):
        self.driver.find_element(by=By.XPATH, value=self.txtOutputSectionName_xpath).send_keys(osname)

    def setSecType(self):
        self.driver.find_element(by=By.XPATH, value=self.drpSectionType_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.txtSectionType_xpath).send_keys(Keys.RETURN)

    def clickOnSave(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.btnSaveWorkspace_cssSelector).click()

    def clickOnCloseSections(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.btnCloseSections_cssSelector).click()

    def clickOnManageUsers(self):
        self.driver.find_element(by=By.XPATH, value=self.lnkManageUsers_menu_xpath).click()

    def clickOnAdd(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAdd_xpath).click()

    def setUser(self, username):
        self.driver.find_element(by=By.XPATH, value=self.drpUser_xpath).click()
        self.driver.find_element(by=By.XPATH, value=self.txtUser_xpath).send_keys(username)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=self.txtUser_xpath).send_keys(Keys.RETURN)

    def clickOnSaveGrant(self):
        self.driver.find_element(by=By.XPATH, value=self.btnSaveAdd_xpath).click()

    def clickOnManageGroups(self):
        self.driver.find_element(by=By.XPATH, value=self.lnkManageGroups_menu_xpath).click()

    def setGGroup(self):
        self.driver.find_element(by=By.XPATH, value=self.drpGGroup_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.txtGGroup_xpath).send_keys(Keys.RETURN)

    def setGGRole(self):
        self.driver.find_element(by=By.XPATH, value=self.drpGGRole_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.txtGGRole_xpath).send_keys(Keys.RETURN)

    def setAdminRoleInLGroup(self):
        self.driver.find_element(by=By.XPATH, value=self.drpGGRole_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.txtAdminRoleLG_xpath).click()

    def setEditorRoleInLGroup(self):
        self.driver.find_element(by=By.XPATH, value=self.drpGGRole_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.txtEditorRoleLG_xpath).click()

    def clickOnLocalGroups(self):
        self.driver.find_element(by=By.XPATH, value=self.tabLGroup_xpath).click()

    def setLGroupName(self, localgroupname):
        self.driver.find_element(by=By.ID, value=self.txtLGroupName_id).send_keys(localgroupname)

    def editLGroupName(self, localGroupName):
        self.driver.find_element(by=By.ID, value=self.txtLGroupName_id).clear()
        self.driver.find_element(by=By.ID, value=self.txtLGroupName_id).send_keys(localGroupName)

    def setLGroupDescription(self, localggroupdescription):
        self.driver.find_element(by=By.ID, value=self.txtLGroupDesc_id).send_keys(localggroupdescription)

    def clickOnAddGrantLG(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddGrantLG_xpath).click()

    def clickOnSaveGrantLG(self):
        self.driver.find_element(by=By.XPATH, value=self.btnSaveGrantLG_xpath).click()

    def clickOnAddUserLG(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddUserLG_xpath).click()

    def setLGUser(self):
        self.driver.find_element(by=By.XPATH, value=self.txtLGUser_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.txtLGUser_xpath).send_keys(Keys.RETURN)

    def setUserInLG(self, vuser):
        self.driver.find_element(by=By.XPATH, value=self.txtLGUser_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=vuser).click()

    def clickOnAddMember(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddMemberLG_xpath).click()

    def clickOnRemoveGroup(self):
        self.driver.find_element(by=By.XPATH, value=self.btnRemoveGroup_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.btnConfirmRemoveG_xpath).click()

    def clickOnArchive(self):
        self.driver.find_element(by=By.XPATH, value=self.btnArchive_xpath).click()

    def clickOnArchiveConfirmation(self):
        self.driver.find_element(by=By.XPATH, value=self.btnArchiveConfirmation_xpath).click()

    def clickOnPurge(self):
        self.driver.find_element(by=By.XPATH, value=self.btnPurge_xpath).click()

    def clickOnPurgeConfirmation(self):
        self.driver.find_element(by=By.XPATH, value=self.btnPurgeConfirmation).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(by=By.XPATH, value=self.tableRows_components_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(by=By.XPATH, value=self.tableColumns_components_xpath))

    def setRoleName(self, rolename):
        self.driver.find_element(by=By.ID, value=self.txtRoleName_id).click()
        time.sleep(1)
        self.driver.find_element(by=By.ID, value=self.txtRoleName_id).send_keys(rolename)

    def setRoleDesc(self, roledesc):
        self.driver.find_element(by=By.ID, value=self.txtRoleDesc_id).click()
        time.sleep(1)
        self.driver.find_element(by=By.ID, value=self.txtRoleDesc_id).send_keys(roledesc)

    def clickOnWsWrite(self):
        self.driver.find_element(by=By.XPATH, value=self.chkWsWrite_xpath).click()

    def clickOnExpandWS(self):
        self.driver.find_element(by=By.XPATH, value=self.btnExpandWS_xpath).click()

    def clickOnComponentsWrite(self):
        self.driver.find_element(by=By.XPATH, value=self.chkComponentsWrite_xpath).click()

    def getRoleTableNoOfRows(self):
        return len(self.driver.find_elements(by=By.XPATH, value=self.roleTableRows_xpath))

# Filter Creation ################

    def setFilterName(self, filtername):
        self.driver.find_element(by=By.XPATH, value=self.txtFilterName_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.txtFilterName_xpath).send_keys(filtername)

    def setResourceType(self, resourcetype):
        self.driver.find_element(by=By.XPATH, value=self.drpSelResourceType_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.txtSelResourceType_xpath).send_keys(resourcetype)
        self.driver.find_element(by=By.XPATH, value=self.txtSelResourceType_xpath).send_keys(Keys.RETURN)

    def clickOnAddResType(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddResourceType_xpath).click()

    def setFilterFields(self, filterfield):
        self.driver.find_element(by=By.XPATH, value=self.drpSelField_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.txtSelField_xpath).send_keys(filterfield)
        self.driver.find_element(by=By.XPATH, value=self.txtSelField_xpath).send_keys(Keys.RETURN)
        time.sleep(1)

    def setWorkspace(self, workspace):
        self.driver.find_element(by=By.XPATH, value=self.drpSelWorkspace_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.txtSelWorkspace_xpath).send_keys(workspace)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.txtSelWorkspace_xpath).send_keys(Keys.RETURN)

    def setLookupScope(self):
        self.driver.find_element(by=By.XPATH, value=self.btnScope_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.optWorkspace_xpath).click()

    def clickOnAddCondition(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddCondition_xpath).click()

    def setFieldOnCondition(self, deptid):
        self.driver.find_element(by=By.XPATH, value=self.drpSelFieldOnCondition_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.txtSelFieldOnCondition_xpath).send_keys(deptid)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.txtSelFieldOnCondition_xpath).send_keys(Keys.RETURN)

    def setCondition(self):
        self.driver.find_element(by=By.XPATH, value=self.drpSelCondition_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.optSelCondition_xpath).click()

    def setWhereStatement(self, department):
        self.driver.find_element(by=By.XPATH, value=self.txtWhereStatement_xpath).send_keys(department)

    def clickOnAddFilterField(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddField_xpath).click()

    def setSortByOption(self, lastname):
        self.driver.find_element(by=By.XPATH, value=self.drpSelSortBy_xpath).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=self.txtSelSortByField_xpath).send_keys(lastname)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=self.txtSelSortByField_xpath).send_keys(Keys.RETURN)

    def clickOnAddForSorting(self):
        self.driver.find_element(by=By.XPATH, value=self.btnAddForSorting_xpath).click()

    def clickOnSaveFilter(self):
        self.driver.find_element(by=By.XPATH, value=self.btnSaveFilter_xpath).click()

    def searchFilterByFilterName(self, vsearch):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(by=By.XPATH, value=self.table_filters_xpath)
            filtername_id_cell_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[2]"
            filtername_id = table.find_element(by=By.XPATH, value=filtername_id_cell_xpath).text

            if filtername_id == vsearch:
                flag = True
                filterenable_to_click_xpath = "//table[@class='table table-striped table-hover table-bordered']/tbody/tr[" + str(
                r) + "]/td[6]/span"
                self.driver.find_element(by=By.XPATH, value=filterenable_to_click_xpath).click()
                break
        return flag


