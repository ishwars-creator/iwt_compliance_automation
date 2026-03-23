from core.base_page import BasePage
from locators.company_user_locators import CompanyUserLocators as L
from playwright.sync_api import expect
from datetime import datetime

class CompanyUserPage(BasePage):
    
    def navigate_to_settings_menu(self):
        self.page.locator(L.SETTINGS_MENU).click()
        expect(self.page.get_by_role("heading", name=L.HEADING)).to_be_visible()
    
    def click_on_company_name(self,company_name):
        self.page.get_by_text(company_name).click()
        expect(self.page.get_by_role("heading", name=company_name)).to_be_visible()
        
    def add_corp_admin(self,data):
        self.page.locator(L.ADD_USER_BTN).click()
        self.type(L.FIRSTNAME, data["corp_admin_firstname"])
        self.type(L.LASTNAME, data["corp_admin_lastname"])
        
        # Generate a unique email using timestamp
        corpadmin_email = f"{data['corp_admin_firstname']}_{data['corp_admin_lastname']}_{datetime.now().timestamp()}@yopmail.com"
        self.type(L.EMAIL, corpadmin_email)
        self.type(L.CONFIRM_EMAIL, corpadmin_email)
        self.page.locator("#role").select_option(label="Corp Admin")  
        self.page.locator(L.ADD_BTN).click()
        self.page.locator(L.ADD_BTN).click()
        self.page.wait_for_timeout(3000)
        expect(self.page.get_by_text("User added successfully")).to_be_visible(timeout=15000)
        
    def add_corp_manager(self,data):
        self.page.locator(L.ADD_USER_BTN).click()
        self.type(L.FIRSTNAME, data["corp_manager_firstname"])
        self.type(L.LASTNAME, data["corp_manager_lastname"])
        corpmanager_email = f"{data['corp_manager_firstname']}_{data['corp_manager_lastname']}_{datetime.now().timestamp()}@yopmail.com"
        self.type(L.EMAIL, corpmanager_email)
        self.type(L.CONFIRM_EMAIL, corpmanager_email)
        self.page.locator("#role").select_option(label="Corp Manager")
        self.page.locator(L.ADD_BTN).click()
        self.page.locator(L.ADD_BTN).click()
        self.page.wait_for_timeout(3000)
        expect(self.page.get_by_text("User added successfully")).to_be_visible(timeout=15000)
        
        
    def add_mine_admin(self,data):
        self.page.locator(L.ADD_USER_BTN).click()
        self.type(L.FIRSTNAME, data["mine_admin_firstname"])
        self.type(L.LASTNAME, data["mine_admin_lastname"])
        mineadmin_email = f"{data['mine_admin_firstname']}_{data['mine_admin_lastname']}_{datetime.now().timestamp()}@yopmail.com"
        self.type(L.EMAIL, mineadmin_email)
        self.type(L.CONFIRM_EMAIL, mineadmin_email)
        self.page.locator("#role").select_option(label="Mine Admin")
        self.page.locator("select[name='mineId']").select_option(value="115") # value =115 ("Montevallo Quarry & Mill ")
        self.page.locator(L.ADD_BTN).click()
        self.page.locator(L.ADD_BTN).click()
        self.page.wait_for_timeout(3000)
        expect(self.page.get_by_text("User added successfully")).to_be_visible(timeout=15000)
        
    def add_mine_manager(self,data):
        self.page.locator(L.ADD_USER_BTN).click()
        self.type(L.FIRSTNAME, data["mine_manager_firstname"])
        self.type(L.LASTNAME, data["mine_manager_lastname"])
        minemanager_email = f"{data['mine_manager_firstname']}_{data['mine_manager_lastname']}_{datetime.now().timestamp()}@yopmail.com"
        self.type(L.EMAIL, minemanager_email)
        self.type(L.CONFIRM_EMAIL, minemanager_email)
        self.page.locator("#role").select_option(label="Mine Manager")
        self.page.locator("select[name='mineId']").select_option(value="115") # value =115 ("Montevallo Quarry & Mill ")
        self.page.locator(L.ADD_BTN).click()
        self.page.locator(L.ADD_BTN).click()
        self.page.wait_for_timeout(3000)
        expect(self.page.get_by_text("User added successfully")).to_be_visible(timeout=15000)
        
    def add_mine_user(self,data):
        self.page.locator(L.ADD_USER_BTN).click()
        self.type(L.FIRSTNAME, data["mine_user_firstname"])
        self.type(L.LASTNAME, data["mine_user_lastname"])
        mineuser_email = f"{data['mine_user_firstname']}_{data['mine_user_lastname']}_{datetime.now().timestamp()}@yopmail.com"
        self.type(L.EMAIL, mineuser_email)
        self.type(L.CONFIRM_EMAIL, mineuser_email)
        self.page.locator("#role").select_option(label="Mine User")
        self.page.locator("select[name='mineId']").select_option(value="115") # value =115 ("Montevallo Quarry & Mill ")
        self.page.locator(L.ADD_BTN).click()
        self.page.locator(L.ADD_BTN).click()
        self.page.wait_for_timeout(3000)
        expect(self.page.get_by_text("User added successfully")).to_be_visible(timeout=15000)           