import time
import pytest

from testcases.conftest import setup
from utility.Readproperties import ReadConfig
from pageobjects.Login_page import Login_Page
from utility.Coustom_Logger import LogGen

class Test001_Login:
    config = ReadConfig.getConfig()
    baseurl = config['baseurl']
    username = config['username']
    password = config['password']
    logger = LogGen.loggen()
    @pytest.fixture()
    def setup_driver(self, setup):
        self.logger.info("**************Test001*********")
        self.driver = setup
        yield
        self.driver.quit()

    def test_login_success(self, setup_driver):
        self.driver.get(self.baseurl)
        time.sleep(5)
        self.lp = Login_Page(self.driver)
        self.lp.setusername(self.username)
        self.lp.setuserpassword(self.password)
        self.lp.login_click()
        # assert self.lp.is_login_successful(), "Login was not successful"

    # You can add more test methods here for different scenarios
