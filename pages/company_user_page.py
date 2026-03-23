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
        
    #### Bleow is the one common function to add the all roles user  
    
    def add_user (self, first_name, last_name, role):
        self.page.locator(L.ADD_USER_BTN).click()
        self.type(L.FIRSTNAME, first_name)
        self.type(L.LASTNAME, last_name)
        mineuser_email = f"{first_name}_{last_name}_{datetime.now().timestamp()}@yopmail.com"
        self.type(L.EMAIL, mineuser_email)
        self.type(L.CONFIRM_EMAIL, mineuser_email)
        self.page.locator("#role").select_option(label=role)
        if role in ["Mine Admin","Mine User","Mine Manager"]:
            self.page.locator("select[name='mineId']").select_option(value="115") # value =115 ("Montevallo Quarry & Mill ")
        
        self.page.locator(L.ADD_BTN).click()
        self.page.locator(L.ADD_BTN).click()
        self.page.wait_for_timeout(3000)
        expect(self.page.get_by_text("User added successfully")).to_be_visible(timeout=15000)
            