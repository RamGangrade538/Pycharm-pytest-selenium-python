from selenium import webdriver
from selenium.webdriver.common.by import By


class Login_Page :
        textbox_username_name = "username"
        textbox_password_name = "password"
        button_login_xpath = "//button[@type='submit']"
        def __init__(self,driver):
            self.driver = driver
        def setusername(self, username):
            self.driver.find_element(By.NAME, self.textbox_username_name).send_keys(username)

        def setuserpassword(self, password):
            self.driver.find_element(By.NAME, self.textbox_password_name).send_keys(password)
        def login_click(self):
            self.driver.find_element(By.XPATH, self.button_login_xpath).click()
