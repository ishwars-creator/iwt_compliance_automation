from core.base_page import BasePage
from locators.mine_locator import MineLocators as L
from playwright.sync_api import expect

class MinePage(BasePage):

    def open_company(self, company_name):
        self.page.get_by_text(company_name).click()

    def add_mine(self, data):
        self.page.locator(L.ADD_MINE_BTN).click()
        self.type(L.MSHA_MINE_NAME, data["name"])
        self.page.get_by_text(data["name"]).click()
        self.type(L.TIME_ZONE, data["timezone"])
        self.page.get_by_text(data["timezone"], exact=True).nth(0).click()
        self.page.select_option(L.CITY, data["city"])
        self.type(L.ADDRESS, data["address"])
        self.type(L.ZIP, data["zip"])

        # enter mine admin details
        self.page.locator(L.ADD_MINE_ADMIN_BTN).click()
        self.type(L.FIRSTNAME, data["mine_admin_firstname"])
        self.type(L.LASTNAME, data["mine_admin_lastname"])
        self.type(L.EMAIL, data["mine_admin_email"])
        self.type(L.CONFIRM_EMAIL, data["mine_admin_confirm_email"])
        self.page.locator(L.ADD_BTN).click()
        self.page.get_by_role("button", name="Yes").click()
        expect(self.page.get_by_text("Mine created successfully")).to_be_visible()
        
        
    def edit_mine(self, adress2):
        self.page.locator(L.EDIT_MINE_BTN).click()
        self.type(L.ADDRESS_LINE2, adress2)
        self.page.locator(L.SAVE_BTN).click()
        expect(self.page.get_by_text("Mine updated successfully")).to_be_visible()