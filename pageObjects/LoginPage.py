from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_cssSelector = "input[placeholder='Username']"
    textbox_password_cssSelector = "input[type=password]"
    button_login_xpath = "//button[contains(text(),'Login')]"
    button_avatar_xpath = "//img[@alt='Avatar']"
    link_logout_linkText = "Logout"
    button_confirmLogout_xpath = "//button[@id='bot2-Msg1']"
    link_home_xpath = "//span[contains(text(),'Home')]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.textbox_username_cssSelector).clear()
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.textbox_username_cssSelector).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.textbox_password_cssSelector).clear()
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.textbox_password_cssSelector).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(by=By.XPATH, value=self.button_login_xpath).click()

    def home(self):
        #        self.driver.find_element(by=By.CSS_SELECTOR, value=self.textbox_search_cssSelector).click()
        self.driver.find_element(by=By.XPATH, value=self.link_home_xpath)

    def logout(self):
        self.driver.find_element(by=By.XPATH, value=self.button_avatar_xpath).click()
        self.driver.find_element(by=By.LINK_TEXT, value=self.link_logout_linkText).click()
        self.driver.find_element(by=By.XPATH, value=self.button_confirmLogout_xpath).click()
