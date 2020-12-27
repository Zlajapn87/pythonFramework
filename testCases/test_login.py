from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

    # creationg of logs

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("************** Test_001_Login "
                         "**************")
        self.logger.info("************** Verifying Home Page Title **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************** Home page title test passed **************")
        else:
            assert False
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("************** Home page title test failed **************")

    def test_login(self, setup):
        self.logger.info("************** Verifying Login test **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword((self.password))
        self.lp.clickOnElement()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("************** Login test passed **************")
        else:
            assert False
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("************** Login test failed **************")

#End of testing
#Comment on a Branch1
