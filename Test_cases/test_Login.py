import pytest
from selenium import webdriver
from POM.login_Page import Login_page


class Test_001:
    base_URL = "https://the-internet.herokuapp.com/login"
    username = "tomsmith"
    password = "SuperSecretPassword!"

    def test_login_01(self, setup):
        self.driver = setup
        self.driver.get(self.base_URL)

        actualTitle = self.driver.title
        if actualTitle == "The Internet":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_01.png")
            self.driver.close()
            assert False

    def test_login_02(self, setup):
        self.driver = setup
        self.driver.get(self.base_URL)
        self.lg = Login_page(self.driver)
        self.lg.setUserName(self.username)
        self.lg.setPassword(self.password)
        self.lg.clickLogin()
        if self.lg.logout_button:
            assert True
        else:
            self.driver.save_screenshot("\\Screenshots\\" + "test_login_02.png")
            self.driver.close()
            assert False
