from core.base_page import BasePage
from locators.company_locators import CompanyLocators as L
from playwright.sync_api import expect

class CompanyPage(BasePage):
        
    def verify_company_page_loaded(self):
        expect(self.page.get_by_role("heading", name=L.HEADING)).to_be_visible()
        expect(self.page.get_by_role("button", name=L.ADD_COMPANY_BTN)).to_be_visible()

    def open_add_company_form(self):
        self.page.get_by_role("button", name=L.ADD_COMPANY_BTN).click()

    def add_company(self, data):
        self.type(L.SAP_ID, data["sap_id"])
        self.type(L.MSHA_NAME, data["name"])
        dropdown_option = self.page.locator("li", has_text=data["name"])
        expect(dropdown_option).to_be_visible(timeout=15000)
        dropdown_option.first.click()

        self.type(L.ADDRESS, data["address"])
        
        self.page.select_option(L.STATE, data["state"])

        expect(self.page.locator(L.CITY)).to_be_enabled(timeout=10000)

        self.page.select_option(L.CITY, data["city"])
        self.type(L.ZIP, data["zip"])
        self.type(L.PHONE, data["phone"])
    
        
        self.page.click(L.MODULE_LOCATION)
        self.page.click(L.MODULE_PRODUCTION)
        self.page.click(L.MODULE_ATMOSPHERE)
        # self.page.click(L.MODULE_COMPLIANCE)
        self.page.click(L.MODULE_FORMS)
        
        # open add user form
        self.page.click(L.ADD_CORP_ADMIN_BTN)
        self.page.click(L.FIRSTNAME)
        self.type(L.FIRSTNAME, data["corp_firstname"])
        self.page.click(L.LASTNAME)
        self.type(L.LASTNAME, data["corp_lastname"])
        self.type(L.LASTNAME, data["corp_lastname"])
        self.type(L.EMAIL, data["corp_email"])
        self.type(L.CONFIRM_EMAIL, data["corp_confirm_email"])

        self.click(L.SUBMIT_BTN)
        expect(self.page.get_by_text("Company Added successfully")).to_be_visible()

    def search_company(self, name):
        self.type(L.SEARCH_BOX, name)
        expect(self.page.get_by_text(name)).to_be_visible()
