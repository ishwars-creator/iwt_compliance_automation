from pages.login_page import LoginPage
from pages.company_user_page import CompanyUserPage
from utils.testdata import COMPANY_USERS
from utils.config import USERNAME, PASSWORD

def test_add_corp_admin(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    cp = CompanyUserPage(page)
    cp.navigate_to_settings_menu()
    cp.click_on_company_name("Lhoist Group")
    cp.add_corp_admin(COMPANY_USERS)
    
    
def test_add_corp_manager(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    cp = CompanyUserPage(page)
    cp.navigate_to_settings_menu()
    cp.click_on_company_name("Lhoist Group")
    cp.add_corp_manager(COMPANY_USERS)    
    
def test_add_mine_admin(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    cp = CompanyUserPage(page)
    cp.navigate_to_settings_menu()
    cp.click_on_company_name("Lhoist Group")
    cp.add_mine_admin(COMPANY_USERS)

def test_add_mine_manager(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    cp = CompanyUserPage(page)
    cp.navigate_to_settings_menu()
    cp.click_on_company_name("Lhoist Group")
    cp.add_mine_manager(COMPANY_USERS)
    
def test_add_mine_user(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    cp = CompanyUserPage(page)
    cp.navigate_to_settings_menu()
    cp.click_on_company_name("Lhoist Group")
    cp.add_mine_user(COMPANY_USERS) 
