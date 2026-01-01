from core.base_page import BasePage
from locators.login_locators import LoginLocators as L
from utils.config import URL

class LoginPage(BasePage):
    def open(self):
        self.page.goto(URL, wait_until="domcontentloaded", timeout=60000)

    def login(self, username, password):
        self.type(L.USERNAME, username)
        self.type(L.PASSWORD, password)
        self.click(L.SIGN_IN)
        
