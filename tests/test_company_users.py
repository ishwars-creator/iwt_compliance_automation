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
    cp.add_user(COMPANY_USERS["corp_admin_firstname"],COMPANY_USERS["corp_admin_lastname"],"Corp Admin")

def test_add_corp_manager(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    cp = CompanyUserPage(page)
    cp.navigate_to_settings_menu()
    cp.click_on_company_name("Lhoist Group")
    cp.add_user(COMPANY_USERS["corp_manager_firstname"],COMPANY_USERS["corp_manager_lastname"],"Corp Manager")
    
    
def test_add_mine_admin(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    cp = CompanyUserPage(page)
    cp.navigate_to_settings_menu()
    cp.click_on_company_name("Lhoist Group")
    cp.add_user(COMPANY_USERS["mine_admin_firstname"],COMPANY_USERS["mine_admin_lastname"],"Mine Admin")

def test_add_mine_manager(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    cp = CompanyUserPage(page)
    cp.navigate_to_settings_menu()
    cp.click_on_company_name("Lhoist Group")
    cp.add_user(COMPANY_USERS["mine_manager_firstname"],COMPANY_USERS["mine_manager_lastname"],"Mine Manager")
    
def test_add_mine_user(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    cp = CompanyUserPage(page)
    cp.navigate_to_settings_menu()
    cp.click_on_company_name("Lhoist Group")
    cp.add_user(COMPANY_USERS["mine_user_firstname"],COMPANY_USERS["mine_user_lastname"],"Mine User")        


########################
"""Beow is the block of clode whic adds the all users in one flow 
"""
        
def test_add_compnay_user_flow(page):
    login = LoginPage(page)
    login.open()
    login.login(USERNAME, PASSWORD)
    cp = CompanyUserPage(page)
    cp.navigate_to_settings_menu()
    cp.click_on_company_name("Lhoist Group")
    cp.add_user(COMPANY_USERS["corp_admin_firstname"],COMPANY_USERS["corp_admin_lastname"],"Corp Admin")
    cp.add_user(COMPANY_USERS["corp_manager_firstname"],COMPANY_USERS["corp_manager_lastname"],"Corp Manager")
    cp.add_user(COMPANY_USERS["mine_admin_firstname"],COMPANY_USERS["mine_admin_lastname"],"Mine Admin")
    cp.add_user(COMPANY_USERS["mine_manager_firstname"],COMPANY_USERS["mine_manager_lastname"],"Mine Manager")
    cp.add_user(COMPANY_USERS["mine_user_firstname"],COMPANY_USERS["mine_user_lastname"],"Mine User")