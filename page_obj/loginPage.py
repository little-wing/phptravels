from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base import Page
import time

class login(Page):
    '''
    User login page.
    '''

    url = '/'

    # Action
    front_end_loc = (By.XPATH, '/html/body/section[2]/div/div/div[1]/div/div/div[2]/div[2]/div/div[1]/div/a')

    # Enter front end
    def enter_frontend(self):
        self.find_element(*self.front_end_loc).click()