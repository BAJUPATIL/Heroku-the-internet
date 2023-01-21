from selenium import webdriver
from selenium.webdriver.common.by import By


class Login_page():
    username_ID = "username"
    password_ID = "password"
    login_button = "//i[contains(text(),'Login')]"
    logout_button = "//body/div[2]/div[1]/div[1]/a[1]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.username_ID).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.password_ID).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def logout_Button(self):
        return self.driver.find_element(By.XPATH, self.logout_button).is_Displayed()