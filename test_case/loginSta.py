import unittest
import os
import sys
projectDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(projectDir)
from models import myunit
from models import function
from page_obj import loginPage
from page_obj.loginPage import login

class loginTest(myunit.MyTest):
    '''
    User login test.
    '''

    def enter_login_page_verify(self):
        #loginPage.login.front_end_loc()
        #loginPage.login(self.driver).enter_frontend()
        login(self.driver).enter_frontend()

    def test_login(self):
        #self.driver.switch_to.frame(1)
        iframeCount = self.driver.find_elements(By.tagName("iframe")).size()
        print "iframeCount is %s" % iframeCount
        self.enter_login_page_verify()
        print "Good test!"

if __name__ == "__main__":
    unittest.main()
