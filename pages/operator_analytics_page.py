from core.base_page import BasePage
from playwright.sync_api import expect

class operatoranalyticspage(BasePage):

    def goto_compliace_menu(self):
        self.page.get_by_role("link", name="Compliance").click()
        expect(self.page.get_by_text("Compliance").nth(1)).to_be_visible()
        
    def select_company(self, value):
        self.page.get_by_role("combobox").nth(0).select_option(value)
        
    def select_all_mines(self):
        self.page.get_by_role("button", name="Select Mine").click()
        self.page.locator("label", has_text="All Mines").click()
        
    def select_all_events(self):
        self.page.get_by_role("button", name="Select Event").click()
        self.page.locator("label", has_text="All Events").click()    
        
        
    def verify_citation_summary(self):
        expect(self.page.get_by_role("heading", name="S & S  Distribution",exact=True)).to_be_visible()
        expect(self.page.get_by_role("heading", name="S & S by Mine",exact=True)).to_be_visible()
        expect(self.page.get_by_role("heading", name="Negligence Distribution",exact=True)).to_be_visible()
        expect(self.page.get_by_role("heading", name=" Negligence by Mine",exact=True)).to_be_visible()  
        expect(self.page.get_by_role("heading",name="Severity Distribution",exact=True)).to_be_visible()
        expect(self.page.get_by_role("heading",name="Severity by Mine",exact=True)).to_be_visible()
        expect(self.page.get_by_role("heading",name="Likelihood Distribution",exact=True)).to_be_visible()
        expect(self.page.get_by_role("heading",name="Likelihood by Mine",exact=True)).to_be_visible()
     