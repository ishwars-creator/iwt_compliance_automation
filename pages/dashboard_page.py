from core.base_page import BasePage
from playwright.sync_api import expect
import os

class dashboardpage(BasePage):

    def goto_compliace_menu(self):
        self.page.get_by_role("link", name="Compliance").click()
        expect(self.page.get_by_text("Compliance").nth(1)).to_be_visible()
        
    def select_company(self, value):
        self.page.get_by_role("combobox").nth(0).select_option(value)
        
    def select_all_mines(self):
        self.page.get_by_role("button", name="Select Mine").click()
        self.page.locator("label", has_text="All Mines").click()
        
        
    def verify_dashboard_loaded(self):
        expect(self.page.get_by_role("heading", name="Top Regulations",exact=True)).to_be_visible()
        expect(self.page.get_by_role("heading", name="S & S Citations Per 100 Inspection Hours",exact=True)).to_be_visible()
        expect(self.page.get_by_role("heading", name="S & S Distribution",exact=True)).to_be_visible()
        expect(self.page.get_by_role("heading", name="S & S by Mines",exact=True)).to_be_visible()  
        expect(self.page.get_by_role("heading",name="% S & S Citations",exact=True)).to_be_visible()
     